import pandas as pd
df = pd.read_csv("pitchingData_2000-2023.csv")


columnas_todos_nan = df.isna().all()

columnas_eliminar = columnas_todos_nan[columnas_todos_nan].index.tolist()

# Crear una copia del DataFrame original sin las columnas con todos los valores NaN
df_sin_nan_columnas = df.drop(columns=columnas_eliminar)

# Guardar el DataFrame modificado en otro archivo CSV
df_sin_nan_columnas.to_csv("pitchingData_2000-2023_sin_NaN.csv", index=False)

