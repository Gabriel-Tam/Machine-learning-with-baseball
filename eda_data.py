import pandas as pd
#All Data of pitchers 2000 at 2023 
df = pd.read_csv("/home/gabriel/OneDrive/AAAIMX/ICCBR/Data_Baseball/GetData/pitchingData_2000-2023.csv")


# Data are those columns with all values ​​as NaN
#df = pd.read_csv("/home/gabriel/OneDrive/AAAIMX/ICCBR/Data_Baseball/DeleteNaNData/DeleteJunkData.py")


# Data where inecesary object columns are deleted (Like: Age Rng or Dollars)
#df = pd.read_csv("/home/gabriel/OneDrive/AAAIMX/ICCBR/Data_Baseball/DeleteObjectData/pitchingData_DollarsAndAgeRng.csv")

#Data where necesary object columns are remplaced (Like: Team)
df = pd.read_csv("/home/gabriel/OneDrive/AAAIMX/ICCBR/Data_Baseball/DeleteObjectData/pitchingData_TeamCode.csv")



print(df)

