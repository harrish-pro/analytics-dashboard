def generate_summary(profile, statistics):

    summary = []

    summary.append(
        f"The dataset contains {profile['rows']} rows and {profile['columns']} columns."
    )

    summary.append(
        f"There are {profile['missing_values']} missing values and {profile['duplicates']} duplicate records."
    )

    for column, values in statistics.items():

        summary.append(
            f"{column} has an average value of {values['mean']} and a maximum value of {values['max']}."
        )

    return " ".join(summary)