def generate_correlation(df):

    numeric_df = df.select_dtypes(
        include="number"
    )

    if len(numeric_df.columns) < 2:
        return None

    return numeric_df.corr().round(2)