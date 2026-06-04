import pandas as pd


def generate_statistics(df):

    stats = {}

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    for column in numeric_columns:

        stats[column] = {

            "mean": round(df[column].mean(), 2),

            "max": round(df[column].max(), 2),

            "min": round(df[column].min(), 2),

            "sum": round(df[column].sum(), 2)

        }

    return stats 