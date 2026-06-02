def generate_insights(df):

    insights = []

    if df.isnull().sum().sum() > 0:
        insights.append(
            "Dataset contains missing values."
        )

    if len(df) > 10000:
        insights.append(
            "Large dataset suitable for trend analysis."
        )

    return insights