import pandas as pd
import os

def load_data(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".csv":

        try:
            return pd.read_csv(file_path)

        except UnicodeDecodeError:
            return pd.read_csv(
                file_path,
                encoding="latin1"
            )

    elif extension in [".xlsx", ".xls"]:

        return pd.read_excel(file_path)

    else:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )