import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def get_nulll_data_info(df):
    qsna = df.shape[0] - df.isnull().sum(axis=0)
    qna = df.isnull().sum(axis=0)
    ppna = round(100 * (df.isnull().sum(axis=0) / df.shape[0]), 2)
    aux = {'datos sin NAs en q': qsna, 'Na en q': qna, 'Na en %': ppna}
    na = pd.DataFrame(data=aux)

    return na.sort_values(by='Na en %', ascending=False)

def get_numeric_columns(df):
    return df.select_dtypes(include=[np.number]).columns.tolist()


def get_categoric_columns(df):
    return df.select_dtypes(include=['string', 'object', 'category']).columns.tolist()

def normalize_string(input_string):
    if isinstance(input_string, str):
        input_string = input_string.lower()
        input_string = input_string.strip()

        return input_string
    return input_string

def set_column_dtype(df, column_dtype_to_set):
    for column, tipo in column_dtype_to_set.items():
        if column in df.columns:
            try:
                if tipo.startswith("datetime"):
                    df[column] = pd.to_datetime(df[column], errors='coerce')
                else:
                    df[column] = df[column].astype(tipo)
            except Exception as e:
                print(
                    f"Error al convertir la columna '{column}' a '{tipo}': {e}"
                )
    return df

def boxplot_graph(df, columns_df, columns_number=3, figsize=(14, 10)):
    row_number = int(len(columns_df) / columns_number)
    left = len(columns_df) % columns_number
    
    if left > 0:
        row_number += 1

    _, axes = plt.subplots(nrows=row_number, ncols=columns_number, figsize=figsize)

    i_actual = 0
    j_actual = 0

    for column in columns_df:
        ax = axes[i_actual][j_actual]

        sns.boxplot(df[column], ax=ax)

        ax.set_title(f"Boxplot {column}")

        j_actual += 1

        if j_actual >= columns_number:
            i_actual += 1
            j_actual = 0

    plt.tight_layout()
    plt.show()

def boxplot_graph_multi_elements(df, columns_df, columns_number=3, figsize=(14, 10)):
    row_number = int(len(columns_df) / columns_number)
    left = len(columns_df) % columns_number
    
    if left > 0:
        row_number += 1

    _, axes = plt.subplots(nrows=row_number, ncols=columns_number, figsize=figsize)

    i_actual = 0
    j_actual = 0

    for column in columns_df:
        ax = axes[i_actual][j_actual]

        sns.boxplot(y = df[column], ax=ax, hue = df['type'], palette=sns.color_palette(('#722F37', '#dbdd46')))

        ax.set_title(f"Boxplot {column}")

        j_actual += 1

        if j_actual >= columns_number:
            i_actual += 1
            j_actual = 0

    plt.tight_layout()
    plt.show()

def graph_histogram(
    df,
    columns_df,
    columns_number=3,
    bins=5,
    kde=False,
    rotations=None,
    figsize=(14, 10),
):
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

        sns.histplot(data=df, kde=kde, bins=bins, ax=ax, x=column, hue="type", palette=sns.color_palette(('#722F37', '#dbdd46')))

        ax.set_title(f"Histograma {column}")
        ax.set_xlabel(column)
        ax.set_ylabel("Freq.")

        if rotations is not None and column in rotations:
            ax.tick_params(axis='x', rotation=rotations[column])

        j_actual += 1

        if j_actual >= columns_number:
            i_actual += 1
            j_actual = 0

    plt.tight_layout()
    plt.show()

def graph_histogram(
    df,
    columns_df,
    columns_number=3,
    bins=5,
    kde=False,
    rotations=None,
    figsize=(14, 10),
):
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

        sns.histplot(data=df, kde=kde, bins=bins, ax=ax, x=column, hue="type", palette=sns.color_palette(('#722F37', '#dbdd46')))

        ax.set_title(f"Histograma {column}")
        ax.set_xlabel(column)
        ax.set_ylabel("Freq.")

        if rotations is not None and column in rotations:
            ax.tick_params(axis='x', rotation=rotations[column])

        j_actual += 1

        if j_actual >= columns_number:
            i_actual += 1
            j_actual = 0

    plt.tight_layout()
    plt.show()

def graph_comparison_histogram(df, kde=False, bins=5, rotations=None, figsize=(14, 10), column=None):
    sns.histplot(data=df, kde=kde, bins=bins, x=column, hue="type", palette=sns.color_palette(('#722F37', '#dbdd46')))
    plt.tight_layout()
    plt.show()


def graph_correlations(corr_red, corr_white, title, cmap='viridis'):
    _, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))
    sns.heatmap(
        corr_red,
        annot=True,
        cmap=cmap,
        center=0,
        ax=ax[0],
    )
    sns.heatmap(
        corr_white,
        annot=True,
        cmap=cmap,
        center=0,
        ax=ax[1],
    )
    ax[0].set_title("Correlaciones Red Wine")
    ax[1].set_title("Correlaciones White Wine")
    plt.suptitle(title, fontsize=16)
    plt.show()


