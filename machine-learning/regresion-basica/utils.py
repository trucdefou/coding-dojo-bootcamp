
import matplotlib.pyplot as plt
import seaborn as sns
def analisis_exploratorio(df):
    print(df.info())
    print(df.describe())
    print(df.isnull().sum())
    print(df.duplicated().sum())

def graficar_boxplots(df, columnas, cantidad_columnas=3, figsize=(14, 10)):
    nro_filas = int(len(columnas) / cantidad_columnas)
    remanente = len(columnas) % cantidad_columnas

    if remanente > 0:
        nro_filas += 1

    _, axes = plt.subplots(nrows=nro_filas, ncols=cantidad_columnas, figsize=figsize)

    i_actual = 0
    j_actual = 0

    for columna in columnas:
        ax = axes[i_actual][j_actual]

        sns.boxplot(df[columna], ax=ax)

        ax.set_title(f"Boxplot {columna}")

        j_actual += 1

        if j_actual >= cantidad_columnas:
            i_actual += 1
            j_actual = 0

    plt.tight_layout()
    plt.show()