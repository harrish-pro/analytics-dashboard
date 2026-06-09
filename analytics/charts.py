import os
import plotly.express as px


def generate_charts(df):

    charts = []

    numeric_columns = list(
        df.select_dtypes(include="number").columns
    )

    text_columns = list(
        df.select_dtypes(include="object").columns
    )

    if len(text_columns) > 0 and len(numeric_columns) > 0:

        fig = px.bar(
            df,
            x=text_columns[0],
            y=numeric_columns[0]
        )

        charts.append(
            fig.to_html(full_html=False)
        )

    if len(numeric_columns) > 0:

        fig = px.histogram(
            df,
            x=numeric_columns[0]
        )

        charts.append(
            fig.to_html(full_html=False)
        )

    return charts


def save_chart_image(df):

    os.makedirs(
        "reports/charts",
        exist_ok=True
    )

    numeric_columns = list(
        df.select_dtypes(include="number").columns
    )

    text_columns = list(
        df.select_dtypes(include="object").columns
    )

    if len(numeric_columns) == 0:
        return None

    if len(text_columns) > 0:

        fig = px.bar(
            df,
            x=text_columns[0],
            y=numeric_columns[0]
        )

    else:

        fig = px.histogram(
            df,
            x=numeric_columns[0]
        )

    image_path = "reports/charts/main_chart.png"

    try:
        fig.write_image(image_path)
        return image_path

    except Exception:
        return None