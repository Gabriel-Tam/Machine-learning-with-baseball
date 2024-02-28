import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv("/home/gabriel/OneDrive/AAAIMX/ICCBR/Data_Baseball/DeleteNaNData/archivo_sin_columnasBasura_V1.csv")

# Calcular la cantidad de NaN en cada columna
cantidad_nan_por_columna = df.isna().sum()

# Ordenar las columnas por cantidad de NaN en orden descendente
columnas_con_mas_nan = cantidad_nan_por_columna.sort_values(ascending=False)

# Seleccionar las primeras 100 columnas con la mayor cantidad de NaN
columnas_top_100_nan = columnas_con_mas_nan.head(100)

# Imprimir las 100 columnas con la mayor cantidad de NaN y sus cantidades
print("100 columnas con la mayor cantidad de NaN:")
print(columnas_top_100_nan)
