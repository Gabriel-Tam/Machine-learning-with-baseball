import pandas as pd

df = pd.read_csv("/home/gabriel/OneDrive/AAAIMX/ICCBR/Data_Baseball/DeleteObjectData/pitchingData_DollarsAndAgeRng.csv")

df["Team"] = df["Team"].astype("category").cat.codes

# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv("/home/gabriel/OneDrive/AAAIMX/ICCBR/Data_Baseball/DeleteObjectData/pitchingData_TeamCode.csv", index=False)
