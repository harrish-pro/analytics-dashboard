import plotly.express as px


def generate_charts(df):

    charts = []

    numeric_columns = list(
        df.select_dtypes(include="number").columns
    )

    text_columns = list(
        df.select_dtypes(include="object").columns
    )

    # BAR CHART

    if len(text_columns) > 0 and len(numeric_columns) > 0:

        fig = px.bar(
            df,
            x=text_columns[0],
            y=numeric_columns[0],
            title=f"{numeric_columns[0]} by {text_columns[0]}"
        )

        charts.append(
            fig.to_html(full_html=False)
        )

    # HISTOGRAM

    if len(numeric_columns) > 0:

        fig = px.histogram(
            df,
            x=numeric_columns[0],
            title=f"Distribution of {numeric_columns[0]}"
        )

        charts.append(
            fig.to_html(full_html=False)
        )

    # PIE CHART

    if len(text_columns) > 0:

        pie_data = (
            df[text_columns[0]]
            .value_counts()
            .reset_index()
        )

        pie_data.columns = [
            "Category",
            "Count"
        ]

        fig = px.pie(
            pie_data,
            names="Category",
            values="Count",
            title=f"{text_columns[0]} Distribution"
        )

        charts.append(
            fig.to_html(full_html=False)
        )

    return charts