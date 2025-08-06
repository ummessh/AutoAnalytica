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

def apply_cleaning_options(df, dropna=False, drop_duplicates=False, drop_columns=None, fillna_method=None):
    # Drop rows with missing values
    if dropna:
        df = df.dropna()

    # Drop duplicate rows
    if drop_duplicates:
        df = df.drop_duplicates()

    # Drop specific columns if provided
    if drop_columns and isinstance(drop_columns, list):
        df = df.drop(columns=drop_columns, errors='ignore')

    # Fill missing values with specified method
    if fillna_method == "mean":
        df = df.fillna(df.mean(numeric_only=True))
    elif fillna_method == "median":
        df = df.fillna(df.median(numeric_only=True))
    elif fillna_method == "mode":
        df = df.fillna(df.mode().iloc[0])

    return df

