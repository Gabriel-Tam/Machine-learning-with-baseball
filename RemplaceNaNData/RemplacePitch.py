import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv("/home/gabriel/OneDrive/AAAIMX/ICCBR/Data_Baseball/DeleteObjectData/pitchingData_TeamCode.csv")

# Lista de todas las columnas relacionadas con lanzamientos
columnas_lanzamientos = [
    'FB%', 'FBv', 'SL%', 'SLv', 'CT%', 'CTv', 'CB%', 'CBv', 'CH%', 'CHv', 
    'SF%', 'SFv', 'KN%', 'KNv', 'wFB', 'wSL', 'wCT', 'wCB', 'wCH', 'wSF', 'wKN', 
    'wFB/C', 'wSL/C', 'wCT/C', 'wCB/C', 'wCH/C', 'wSF/C', 'wKN/C', 
    'FA% (sc)', 'FT% (sc)', 'FC% (sc)', 'FS% (sc)', 'FO% (sc)', 'SI% (sc)', 
    'SL% (sc)', 'CU% (sc)', 'KC% (sc)', 'EP% (sc)', 'CH% (sc)', 'SC% (sc)', 'KN% (sc)', 
    'vFA (sc)', 'vFT (sc)', 'vFC (sc)', 'vFS (sc)', 'vFO (sc)', 'vSI (sc)', 
    'vSL (sc)', 'vCU (sc)', 'vKC (sc)', 'vEP (sc)', 'vCH (sc)', 'vSC (sc)', 'vKN (sc)',
    'FA-X (sc)', 'FT-X (sc)', 'FC-X (sc)', 'FS-X (sc)', 'FO-X (sc)', 'SI-X (sc)', 
    'SL-X (sc)', 'CU-X (sc)', 'KC-X (sc)', 'EP-X (sc)', 'CH-X (sc)', 'SC-X (sc)', 'KN-X (sc)', 
    'FA-Z (sc)', 'FT-Z (sc)', 'FC-Z (sc)', 'FS-Z (sc)', 'FO-Z (sc)', 'SI-Z (sc)', 
    'SL-Z (sc)', 'CU-Z (sc)', 'KC-Z (sc)', 'EP-Z (sc)', 'CH-Z (sc)', 'SC-Z (sc)', 'KN-Z (sc)', 
    'wFA (sc)', 'wFT (sc)', 'wFC (sc)', 'wFS (sc)', 'wFO (sc)', 'wSI (sc)', 
    'wSL (sc)', 'wCU (sc)', 'wKC (sc)', 'wEP (sc)', 'wCH (sc)', 'wSC (sc)', 'wKN (sc)', 
    'wFA/C (sc)', 'wFT/C (sc)', 'wFC/C (sc)', 'wFS/C (sc)', 'wFO/C (sc)', 'wSI/C (sc)', 
    'wSL/C (sc)', 'wCU/C (sc)', 'wKC/C (sc)', 'wEP/C (sc)', 'wCH/C (sc)', 'wSC/C (sc)', 'wKN/C (sc)'
]

# Lista de columnas relevantes que deseas conservar
columnas_relevantes = [
    'FB%', 'FBv', 'SL%', 'SLv', 'CT%', 'CTv', 'CB%', 'CBv', 
    'CH%', 'CHv', 'SF%', 'SFv', 'KN%', 'KNv', 
    'wFB', 'wSL', 'wCT', 'wCB', 'wCH', 'wSF', 'wKN',
    'wFB/C', 'wSL/C', 'wCT/C', 'wCB/C', 'wCH/C', 'wSF/C', 'wKN/C'
]

# Eliminar las columnas que no son relevantes de la lista de lanzamientos
columnas_a_eliminar = [col for col in columnas_lanzamientos if col not in columnas_relevantes]
df_modificado = df.drop(columns=columnas_a_eliminar)

# Cambiar NaN por 0 en las columnas relevantes conservadas
df_modificado[columnas_relevantes] = df_modificado[columnas_relevantes].fillna(0)


#print(df_modificado.head())
# Guardar el DataFrame modificado
df_modificado.to_csv('/home/gabriel/OneDrive/AAAIMX/ICCBR/Data_Baseball/RemplaceNaNData/NaN_at_0.csv', index=False)
