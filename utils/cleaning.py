# cleaning functions
import pandas as pd
import numpy as np

def generate_cleaning_report(df):
    report = {
        "Total Rows": len(df),
        "Total Columns": len(df.columns),
        "Null Values per Column": df.isnull().sum().to_dict(),
        "Duplicate Rows": int(df.duplicated().sum()),
        "Constant Columns": [col for col in df.columns if df[col].nunique() == 1]
    }
    return report

def apply_cleaning_options(df, drop_nulls, fill_nulls, drop_duplicates, drop_constant):
    df_cleaned = df.copy()

    if drop_nulls:
        df_cleaned.dropna(inplace=True)

    if fill_nulls != "None":
        for col in df_cleaned.columns:
            if df_cleaned[col].isnull().any():
                if df_cleaned[col].dtype in [np.float64, np.int64]:
                    if fill_nulls == "Mean":
                        df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].mean())
                    elif fill_nulls == "Median":
                        df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].median())
                else:
                    if fill_nulls == "Mode":
                        df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].mode()[0])

    if drop_duplicates:
        df_cleaned.drop_duplicates(inplace=True)

    if drop_constant:
        for col in df_cleaned.columns:
            if df_cleaned[col].nunique() == 1:
                df_cleaned.drop(columns=col, inplace=True)

    return df_cleaned
