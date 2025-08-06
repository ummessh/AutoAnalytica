# cleaning functions
import pandas as pd

def generate_cleaning_report(df):
    report = {
        "Shape": df.shape,
        "Column Names": list(df.columns),
        "Data Types": df.dtypes.apply(str).to_dict(),
        "Missing Values": df.isnull().sum().to_dict(),
        "Duplicate Rows": int(df.duplicated().sum())
    }
    return report

def apply_cleaning_options(df, dropna=False, drop_duplicates=False):
    if dropna:
        df = df.dropna()
    if drop_duplicates:
        df = df.drop_duplicates()
    return df

