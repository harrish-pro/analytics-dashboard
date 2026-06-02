import pandas as pd


def create_dataset_profile(df):

    profile = {}

    profile["rows"] = df.shape[0]

    profile["columns"] = df.shape[1]

    profile["column_names"] = list(df.columns)

    profile["missing_values"] = int(
        df.isnull().sum().sum()
    )

    profile["duplicates"] = int(
        df.duplicated().sum()
    )

    numeric_columns = list(
        df.select_dtypes(
            include=["number"]
        ).columns
    )

    text_columns = list(
        df.select_dtypes(
            include=["object"]
        ).columns
    )

    profile["numeric_columns"] = numeric_columns

    profile["text_columns"] = text_columns

    return profile