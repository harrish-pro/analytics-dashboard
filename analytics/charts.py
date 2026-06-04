import plotly.express as px


def generate_chart(df):

    numeric_columns = list(
        df.select_dtypes(include="number").columns
    )

    text_columns = list(
        df.select_dtypes(include="object").columns
    )

    if len(numeric_columns) == 0:
        return None

    if len(text_columns) > 0:

        x_col = text_columns[0]
        y_col = numeric_columns[0]

        fig = px.bar(
            df,
            x=x_col,
            y=y_col,
            title=f"{y_col} by {x_col}"
        )

    else:

        y_col = numeric_columns[0]

        fig = px.histogram(
            df,
            x=y_col,
            title=f"Distribution of {y_col}"
        )

    return fig.to_html(full_html=False)


def save_chart_image(df):

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

    image_path = "report_images/chart.png"

    fig.write_image(image_path)

    return image_path