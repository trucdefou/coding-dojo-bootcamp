
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def variation_coefficient(series):
    return series.std() / series.mean()
def get_nulll_data_info(df): #obtiene los datos nulos en el dataset
    qsna = df.shape[0] - df.isnull().sum(axis=0)
    qna = df.isnull().sum(axis=0)
    ppna = round(100 * (df.isnull().sum(axis=0) / df.shape[0]), 2)
    aux = {'datos sin NAs en q': qsna, 'Na en q': qna, 'Na en %': ppna}
    na = pd.DataFrame(data=aux)

    return na.sort_values(by='Na en %', ascending=False)

def clean_not_float_values(x):
    try:
        return float(x)
    except ValueError:
        return np.nan

def get_numeric_columns(df): #retorna columnas numericas
    return df.select_dtypes(include=[np.number]).columns.tolist()


def get_categoric_columns(df): #retorna columnas categoricas (basado en su tipo)
    return df.select_dtypes(include=['string', 'object', 'category']).columns.tolist()

def normalize_string(input_string): #normaliza strings
    if isinstance(input_string, str):
        input_string = input_string.lower()
        input_string = input_string.strip()

        return input_string
    return input_string

def graph_histogram( #grafica histogramas
    df,
    columns_df,
    columns_number=3,
    bins=5,
    kde=False,
    rotations=None,
    figsize=(14, 10),
    title="Histogramas"):
    row_number = int(len(columns_df) / columns_number)
    left = len(columns_df) % columns_number

    if left > 0:
        row_number += 1

    _, axes = plt.subplots(nrows=row_number, ncols=columns_number, figsize=figsize)

    i_actual = 0
    j_actual = 0

    for column in columns_df:
        if row_number == 1:
            ax = axes[j_actual]
        else:
            ax = axes[i_actual][j_actual]

        sns.histplot(data=df, kde=kde, bins=bins, ax=ax, x=column)

        ax.set_title(f"Histograma {column}")
        ax.set_xlabel(column)
        ax.set_ylabel("Freq.")

        if rotations is not None and column in rotations:
            ax.tick_params(axis='x', rotation=rotations[column])

        j_actual += 1

        if j_actual >= columns_number:
            i_actual += 1
            j_actual = 0
    plt.suptitle(title, fontsize=16) 
    plt.tight_layout()
    plt.show()

def get_outliers_data(df):
    num_columns = get_numeric_columns(df)

    df_outliers = pd.DataFrame()

    for column in num_columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1

        lim_min = Q1 - 1.5 * IQR
        lim_max = Q3 + 1.5 * IQR

        outliers = df[(df[column] < lim_min) |
                      (df[column] > lim_max)][column]

        num_outliers = outliers.count()
        percentage_outliers = (outliers.count() / df[column].count()) * 100

        df_outliers[column] = {
            "N° Outliers": num_outliers,
            "% Outliers": percentage_outliers,
            "Lim. mix": lim_min,
            "Lim. max": lim_max
        }

    return df_outliers

def graph_boxplot(df, columns, num_columns=3, figsize=(14, 10), title="Gráfico de cajas"):
    num_rows = int(len(columns) / num_columns)
    left = len(columns) % num_columns

    if left > 0:
        num_rows += 1

    _, axes = plt.subplots(nrows=num_rows, ncols=num_columns, figsize=figsize)

    i_actual = 0
    j_actual = 0

    for column in columns:
        ax = axes[i_actual][j_actual]

        sns.boxplot(df[column], ax=ax)

        ax.set_title(f"Boxplot {column}")

        j_actual += 1

        if j_actual >= num_columns:
            i_actual += 1
            j_actual = 0
    plt.suptitle(title, fontsize=16) 
    plt.tight_layout()
    plt.show()

def graph_correlations(pearson, spearmann, kendall, title, cmap=['coolwarm', 'viridis', 'plasma'], figsize=(20, 8)): #grafica de correlaciones
    _, ax = plt.subplots(nrows=2, ncols=2, figsize=figsize)
    mask = [np.triu(np.ones_like(pearson.corr(), dtype=np.bool)), np.triu(np.ones_like(spearmann.corr(), dtype=np.bool)), np.triu(np.ones_like(kendall.corr(), dtype=np.bool))]
    sns.heatmap(
        pearson,
        annot=True,
        cmap=cmap[0],
        center=0,
        ax=ax[0,0],
        mask=mask[0]
    )
    sns.heatmap(
        spearmann,
        annot=True,
        cmap=cmap[1],
        center=0,
        ax=ax[0,1],
        mask=mask[1]
    )
    sns.heatmap(
        kendall,
        annot=True,
        cmap=cmap[2],
        center=0,
        ax=ax[1,0],
        mask=mask[2]
    )
    ax[0,0].set_title("Pearson Method")
    ax[0,1].set_title("Spearmann Method")
    ax[1,0].set_title("Kendall Method")

    plt.suptitle(title, fontsize=16)
    plt.show()

def isfloat(num): #esta función verifica si el valoor ingresado es de tipo float
            try:
                float(num)
                return True
            except ValueError:
                return False
def isInt(num): #esta función verifica si el valoor ingresado es de tipo float
    try:
        int(num)
        return True
    except ValueError:
        return False

def check_if_column_is_numeric(df, column):
    cantidad = 0
    finvalido = []
    print("\nValores inválidos en la columna", column, "\n")
    for i in range(len(df)):
        if (not isfloat(df.iloc[i,22]) and not isInt(df.iloc[i,22])): # se verifica si es float y en caso de no serlo, se visualiza para evaluar cómo repararlo
            print(f"El valor de la fila [{i}], columna [{column}] es [{df.iloc[i,22]}]")
            cantidad += 1
            finvalido.append(i)
    print("Se encontraron ", cantidad, "valores inválidos en las filas ,", finvalido)

def get_descriptive_statistics(df, num_decimales=None):
    campos_numericos = get_numeric_columns(df)

    estadisticas = df[[*campos_numericos]].agg(
        [
            "min",
            "max",
            "mean",
            "std",
            "median",
            variation_coefficient,
        ]
    )

    if num_decimales is not None:
        estadisticas = estadisticas.round(2)

    return estadisticas