from pybaseball import pitching_stats

START = 2009
END = 2023

# Obtener estadísticas de lanzadores
pitching = pitching_stats(START, END, qual=45)

# Filtrar lanzadores que hayan tenido al menos una temporada en Grandes Ligas
pitching_filtered = pitching.groupby("IDfg").filter(lambda x: x.shape[0] > 1)

# Guardar los datos filtrados en un nuevo archivo CSV
pitching_filtered.to_csv("pitchingData_2009-2023.csv", index=False)
