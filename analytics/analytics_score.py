def calculate_health_score(profile):

    rows = profile["rows"]

    missing = profile["missing_values"]

    duplicates = profile["duplicates"]

    score = 100

    if rows > 0:

        score -= (missing / rows) * 50

        score -= (duplicates / rows) * 50

    score = round(score)

    if score < 0:
        score = 0

    return score