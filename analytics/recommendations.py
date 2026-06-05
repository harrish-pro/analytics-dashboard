def generate_recommendations(
    profile,
    health_score
):

    recommendations = []

    if health_score >= 90:

        recommendations.append(
            "Dataset quality is excellent."
        )

    elif health_score >= 70:

        recommendations.append(
            "Dataset quality is acceptable but should be reviewed."
        )

    else:

        recommendations.append(
            "Dataset quality requires improvement."
        )

    if profile["missing_values"] > 0:

        recommendations.append(
            "Review missing values before business decisions."
        )

    if profile["duplicates"] > 0:

        recommendations.append(
            "Remove duplicate records for better accuracy."
        )

    recommendations.append(
        "Continue monitoring KPI trends regularly."
    )

    return recommendations