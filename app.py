from flask import (
    Flask,
    render_template,
    send_file,
    request
)

import os

from analytics.data_loader import load_data
from analytics.data_cleaner import clean_data

from analytics.dataset_profile import (
    create_dataset_profile
)

from analytics.statistics_engine import (
    generate_statistics
)

from analytics.summary import (
    generate_summary
)

from analytics.charts import (
    generate_chart,
    save_chart_image
)

from analytics.report_data import (
    prepare_report_data
)

from analytics.pdf_report import (
    create_pdf_report
)

from analytics.docx_report import (
    create_docx_report
)

app = Flask(__name__)

# STORE LATEST ANALYSIS

latest_report_data = {}

# CREATE REQUIRED FOLDERS

os.makedirs("uploads", exist_ok=True)
os.makedirs("reports", exist_ok=True)


# HOME PAGE

@app.route("/")
def home():

    return render_template(
        "dashboard.html"
    )


# DATASET UPLOAD

@app.route("/upload", methods=["GET", "POST"])
def upload_dataset():

    global latest_report_data

    if request.method == "POST":

        if "dataset" not in request.files:
            return "No file uploaded"

        file = request.files["dataset"]

        if file.filename == "":
            return "No file selected"

        file_path = os.path.join(
            "uploads",
            file.filename
        )

        file.save(file_path)

        # LOAD DATA

        df = load_data(file_path)

        # CLEAN DATA

        df = clean_data(df)

        # DATASET PROFILE

        profile = create_dataset_profile(df)

        # STATISTICS

        statistics = generate_statistics(df)

        # SUMMARY

        summary = generate_summary(
            profile,
            statistics
        )

        # CHART

        chart = generate_chart(df)

        # SAVE CHART IMAGE

        chart_image = save_chart_image(df)

        # STORE REPORT DATA

        latest_report_data = prepare_report_data(
            profile,
            statistics,
            summary,
            chart_image
        )

        return render_template(
            "analysis.html",
            profile=profile,
            statistics=statistics,
            summary=summary,
            chart=chart
        )

    return render_template(
        "upload.html"
    )


# PDF DOWNLOAD

@app.route("/download/pdf")
def download_pdf():

    file_path = os.path.join(
        "reports",
        "report.pdf"
    )

    create_pdf_report(
        latest_report_data,
        file_path
    )

    return send_file(
        file_path,
        as_attachment=True
    )


# DOCX DOWNLOAD

@app.route("/download/docx")
def download_docx():

    file_path = os.path.join(
        "reports",
        "report.docx"
    )

    create_docx_report(
        latest_report_data,
        file_path
    )

    return send_file(
        file_path,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)