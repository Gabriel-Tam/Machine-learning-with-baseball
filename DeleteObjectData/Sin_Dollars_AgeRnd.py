import pandas as pd

df = pd.read_csv("pitchingData_2000-2023_sin_NaN.csv")

columns_objetcs = df.select_dtypes(exclude=['number']).columns


# Eliminar las columnas "Dollars" y "Age Rng" del DataFrame
df.drop(columns=["Dollars", "Age Rng"], inplace=True)

# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv("pitchingData_2000-2023_sin_NaN_modificado.csv", index=False)

