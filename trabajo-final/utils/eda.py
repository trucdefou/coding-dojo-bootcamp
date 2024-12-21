
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

def get_numeric_columns(df): #retorna columns numericas
    return df.select_dtypes(include=[np.number]).columns.tolist()


def get_categoric_columns(df): #retorna columns categoricas (basado en su tipo)
    return df.select_dtypes(include=['string', 'object', 'category']).columns.tolist()

def normalize_string(input_string): #normaliza strings
    if isinstance(input_string, str):
        input_string = input_string.lower()
        input_string = input_string.strip()

        return input_string
    return input_string

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
def check_bool(x):
    if x in [0, 0.0, "false", "no", "No","no", "N", "n"]:
        return False

    if x in [1, 1.0, "true", "yes", "Yes", "si", "Y", "y"]:
        return True

    return x


def convert_bolean_columns(df):
    columns = df.columns.tolist()

    converted_columns = []

    boolean_patterns = [
        [0, 1],
        [0.0, 1.0],
        ["false", "true"],
        ["No", "Yes"],
        ["no", "yes"],
        ["no", "si"],
        ["N", "Y"],
        ["n", "y"],
    ]
    for column in columns:
        unique_values = df[column].dropna().unique()

        is_boolean = False

        if len(unique_values) == 2 and column !="sex":
            for pattern in boolean_patterns:
                if set(unique_values) == set(pattern):
                    df[column] = df[column].apply(check_bool)
                    df[column] = df[column].astype("bool")
                    is_boolean = True
                    break

        if is_boolean:
            converted_columns.append(column)

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
    _, ax = plt.subplots(nrows=3, ncols=1, figsize=figsize)
    sns.heatmap(
        pearson,
        annot=True,
        cmap=cmap[0],
        center=0,
        ax=ax[0],
    )
    sns.heatmap(
        spearmann,
        annot=True,
        cmap=cmap[1],
        center=0,
        ax=ax[1],
    )
    sns.heatmap(
        kendall,
        annot=True,
        cmap=cmap[2],
        center=0,
        ax=ax[2],
    )
    ax[0].set_title("Pearson Method")
    ax[1].set_title("Spearmann Method")
    ax[2].set_title("Kendall Method")

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
    print("\nValores inválidos en la column", column, "\n")
    for i in range(len(df)):
        if (not isfloat(df.iloc[i,22]) and not isInt(df.iloc[i,22])): # se verifica si es float y en caso de no serlo, se visualiza para evaluar cómo repararlo
            print(f"El valor de la fila [{i}], column [{column}] es [{df.iloc[i,22]}]")
            cantidad += 1
            finvalido.append(i)
    print("Se encontraron ", cantidad, "valores inválidos en las filas ,", finvalido)

def get_descriptive_statistics(df, decimal_numbers=None):
    numeric_fields = get_numeric_columns(df)

    estadistics = df[[*numeric_fields]].agg(
        [
            "min",
            "max",
            "mean",
            "std",
            "median",
            variation_coefficient,
        ]
    )

    if decimal_numbers is not None:
        estadistics = estadistics.round(2)

    return estadistics

def clean_string(string_to_clean):
    if isinstance(string_to_clean, str):
        string_to_clean = string_to_clean.lower()
        string_to_clean = string_to_clean.strip()

        return string_to_clean
    return string_to_clean

def graph_scaterplot(
    df, columns_x, column_y, nro_columns=3, figsize=(14, 10), hue=None, palette=None
):
    row_num = int(len(columns_x) / nro_columns)
    left = len(columns_x) % nro_columns

    if left > 0:
        row_num += 1

    _, axes = plt.subplots(nrows=row_num, ncols=nro_columns, figsize=figsize)

    i_actual = 0
    j_actual = 0

    for column in columns_x:
        if row_num == 1:
            ax = axes[j_actual]
        else:
            ax = axes[i_actual][j_actual]

        sns.scatterplot(df, x=column, y=column_y, ax=ax, hue=hue, palette=palette)

        ax.set_title(f"Dispersión {column} vs {column_y}")
        ax.set_xlabel(column)
        ax.set_ylabel(column_y)

        j_actual += 1

        if j_actual >= nro_columns:
            i_actual += 1
            j_actual = 0

    plt.tight_layout()
    plt.show()

def graph_barplot(
    df, columns_x, column_y, num_columns=3, figsize=(14, 10)
):
    row_num = int(len(columns_x) / num_columns)
    left = len(columns_x) % num_columns

    if left > 0:
        row_num += 1

    _, axes = plt.subplots(nrows=row_num, ncols=num_columns, figsize=figsize)

    i_actual = 0
    j_actual = 0

    for column in columns_x:
        df["counts"] = np.zeros(len(df))
        df_gouped = df.groupby([column,
                                  column_y],
                                  observed=False)["counts"].count().reset_index()
        if row_num == 1:
            ax = axes[j_actual]
        else:
            ax = axes[i_actual][j_actual]

        sns.barplot(df_gouped, x=column, y="counts", hue=column_y, ax=ax, palette="Set2")

        ax.set_title(f"{column} vs {column_y}")
        ax.set_xlabel(column)
        ax.set_ylabel("Cant")

        j_actual += 1

        if j_actual >= num_columns:
            i_actual += 1
            j_actual = 0

        df.drop("counts", axis=1, inplace=True)

    plt.tight_layout()
    plt.show()

def charges_2_cat(x):
    if 0 <= x <= 10_000:
        return "0-10.000"

    if 10_000 <= x <= 20_000:
        return "10.000-20.000"

    if 20_000 <= x <= 30_000:
        return "20.000-30.000"

    if 30_000 <= x <= 40_000:
        return "30.000-40.000"

    if 40_000 <= x <= 50_000:
        return "40.000-50.000"

    return "50.000+"



def convert_categoric_columns(df):
    columns = get_categoric_columns(df)
    for column in columns:
        df[column] = df[column].astype("category")

def graph_confusion_matrixes(
    conf_matrixes,
    confusion_matrix_names=None,
    labels=None,
    column_num=3,
    figsize=(10, 8),
):
    row_num = int(len(conf_matrixes) / column_num)
    remanente = len(conf_matrixes) % column_num

    if remanente > 0:
        row_num += 1

    _, axes = plt.subplots(nrows=row_num, ncols=column_num, figsize=figsize)
    if row_num == 1 and column_num == 1:
        axes = [[axes]]  # Convertir a una matriz 2D
    elif row_num == 1:
        axes = [axes]  # Convertir a una matriz 2D con una fila
    elif column_num == 1:
        axes = [[ax] for ax in axes]  # Convertir a una matriz 2D con una columna

    i_actual = 0
    j_actual = 0

    for matrix_confusion in conf_matrixes:
        ax = axes[i_actual][j_actual]

        sns.heatmap(
            matrix_confusion,
            annot=True,
            cmap='Blues',
            center=0,
            ax=ax,
        )
        ax.set_xlabel("Predicción")
        ax.set_ylabel("Valores Reales")
        if labels is not None:
            ax.set_xticks(ticks=ax.get_xticks(), labels=labels)
            ax.set_yticks(ticks=ax.get_yticks(), labels=labels)

        if confusion_matrix_names is not None:
            nombre = confusion_matrix_names[i_actual * column_num +
                                            j_actual]
            ax.set_title(f"Matriz de Confusión {nombre}")
        else:
            ax.set_title("Matriz de Confusión")

        j_actual += 1

        if j_actual >= column_num:
            i_actual += 1
            j_actual = 0

    plt.tight_layout()
    plt.show()