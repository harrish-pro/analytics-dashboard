def dataset_summary(df):

    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": df.isnull().sum().sum(),
        "duplicates": df.duplicated().sum()
    }