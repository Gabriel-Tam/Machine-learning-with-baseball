import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv("/home/gabriel/OneDrive/AAAIMX/ICCBR/Data_Baseball/RemplaceNaNData/NaN_at_0.csv")

# Eliminar las columnas especificadas
columnas_a_eliminar = ["Pit+ FO", "Loc+ FO", "Stf+ FO"]
df_sin_columnas = df.drop(columns=columnas_a_eliminar)

# Guardar el DataFrame resultante en un nuevo archivo CSV
nombre_archivo_salida = "archivo_sin_columnasBasura_V1.csv"
df_sin_columnas.to_csv(nombre_archivo_salida, index=False)

print("Se ha guardado el DataFrame sin las columnas especificadas en el archivo:", nombre_archivo_salida)
