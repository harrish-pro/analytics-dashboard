import json
import os


HISTORY_FILE = "data/analytics_history.json"


def save_analysis(record):

    if not os.path.exists(HISTORY_FILE):

        with open(HISTORY_FILE, "w") as file:

            json.dump([], file)

    with open(HISTORY_FILE, "r") as file:

        history = json.load(file)

    history.append(record)

    with open(HISTORY_FILE, "w") as file:

        json.dump(
            history,
            file,
            indent=4
        )


def get_history():

    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r") as file:

        return json.load(file)