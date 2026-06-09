def compare_datasets(
    dataset1,
    dataset2
):

    comparison = {

        "rows_difference":
        dataset2["rows"] - dataset1["rows"],

        "columns_difference":
        dataset2["columns"] - dataset1["columns"],

        "health_difference":
        dataset2["health_score"] -
        dataset1["health_score"]

    }

    return comparison