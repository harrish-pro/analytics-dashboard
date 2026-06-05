def generate_insights(
    profile,
    statistics,
    correlation
):

    insights = []

    # DATA QUALITY

    if profile["missing_values"] == 0:

        insights.append(
            "Dataset quality is excellent with no missing values."
        )

    else:

        insights.append(
            f"Dataset contains {profile['missing_values']} missing values."
        )

    # DUPLICATES

    if profile["duplicates"] > 0:

        insights.append(
            f"Dataset contains {profile['duplicates']} duplicate records."
        )

    # STATISTICS

    for column, values in statistics.items():

        insights.append(
            f"{column} average value is {values['mean']}."
        )

    # CORRELATION

    if correlation is not None:

        cols = correlation.columns

        for i in range(len(cols)):

            for j in range(i + 1, len(cols)):

                value = correlation.iloc[i, j]

                if abs(value) >= 0.7:

                    insights.append(
                        f"{cols[i]} and {cols[j]} have a strong relationship ({value})."
                    )

    return insights