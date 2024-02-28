from pybaseball import pitching_stats

START = 2000
END = 2023

pitching = pitching_stats(START,END, qual= 30)

pitching.to_csv("pitchingData_2000-2023.csv")
