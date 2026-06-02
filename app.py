from flask import (
    Flask,
    render_template,
    send_file,
    request
)

import os

from analytics.charts import (
    create_task_chart,
    create_productivity_chart,
    create_employee_chart
)

from analytics.summary import generate_summary
from analytics.dataset_profile import create_dataset_profile
from analytics.pdf_report import create_pdf_report

from analytics.docx_report import create_docx_report
from analytics.data_loader import load_data
from analytics.data_cleaner import clean_data
from analytics.analyzer import dataset_summary
from analytics.insight_engine import generate_insights

app = Flask(__name__)

# CREATE REQUIRED FOLDERS

os.makedirs("uploads", exist_ok=True)
os.makedirs("reports", exist_ok=True)


# DASHBOARD

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


# DATASET UPLOAD

@app.route("/upload", methods=["GET", "POST"])
def upload_dataset():

    if request.method == "POST":

        file = request.files["dataset"]

        file_path = os.path.join(
            "uploads",
            file.filename
        )

        file.save(file_path)

        df = load_data(file_path)

        df = clean_data(df)

        profile = create_dataset_profile(df)

        return render_template(
            "analysis.html",
            profile=profile
        )

    return render_template("upload.html")


# PDF DOWNLOAD

@app.route("/download/pdf")
def download_pdf():

    file_path = os.path.join(
        "reports",
        "analytics_report.pdf"
    )

    create_pdf_report(file_path)

    return send_file(
        file_path,
        as_attachment=True
    )


# DOCX DOWNLOAD

@app.route("/download/docx")
def download_docx():

    file_path = os.path.join(
        "reports",
        "analytics_report.docx"
    )

    create_docx_report(file_path)

    return send_file(
        file_path,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)