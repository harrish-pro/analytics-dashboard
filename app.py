from flask import Flask, render_template

from analytics.charts import (
    create_task_chart,
    create_productivity_chart,
    create_employee_chart
)

from analytics.summary import generate_summary

app = Flask(__name__)


@app.route("/")
def home():

    task_chart = create_task_chart()

    productivity_chart = create_productivity_chart()

    employee_chart = create_employee_chart()

    summary = generate_summary()

    return render_template(
        "dashboard.html",

        task_chart=task_chart,

        productivity_chart=productivity_chart,

        employee_chart=employee_chart,

        summary=summary
    )


if __name__ == "__main__":
    app.run(debug=True)