# cleaning functions
def generate_cleaning_report(df):
    # Example dummy logic for report
    report = {
        "shape": df.shape,
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_rows": df.duplicated().sum()
    }
    return report


def apply_cleaning_options(df, dropna=False, drop_duplicates=False):
    if dropna:
        df = df.dropna()
    if drop_duplicates:
        df = df.drop_duplicates()
    return df
