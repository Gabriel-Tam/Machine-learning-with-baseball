import pandas as pd

def search_row(df :pd.DataFrame , columns: list, value:str):
    result = df[df[columns].apply(lambda row: any(value in str(cell) for cell in row), axis=1)]

    return result