import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    res = students.dropna(subset=['name'])
    return res