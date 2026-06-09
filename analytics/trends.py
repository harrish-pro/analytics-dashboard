import plotly.express as px
import pandas as pd


def generate_trend_chart(records):

    if len(records) == 0:
        return None

    df = pd.DataFrame(records)

    fig = px.line(
        df,
        x="date",
        y="health_score",
        markers=True,
        title="Dataset Health Score Trend"
    )

    fig.update_layout(
        template="plotly_dark"
    )

    return fig.to_html(
        full_html=False
    )