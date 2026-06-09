from flask import (
    Flask,
    render_template,
    send_file,
    request
)
from datetime import datetime

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
    generate_charts,
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

from analytics.analytics_score import (
    calculate_health_score
)

from analytics.correlation import (
    generate_correlation
)

from analytics.insights import (
    generate_insights
)

from analytics.recommendations import (
    generate_recommendations
)
from analytics.history_manager import (
    save_analysis,
    get_history
)
from analytics.comparison import (
    compare_datasets
)
from analytics.trends import (
    generate_trend_chart
)
from analytics.risk_detector import (
    detect_dataset_risk
)
from analytics.scorecard import (
    generate_scorecard
)
from analytics.chatbot import (
    answer_question
)
app = Flask(__name__)

# STORE LATEST ANALYSIS

latest_report_data = {}
latest_profile = {}

latest_health_score = 0

latest_risk_report = {}

latest_scorecard = {}

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
   
    global latest_profile

    global latest_health_score

    global latest_risk_report

    global latest_scorecard

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

        # PROFILE

        profile = create_dataset_profile(df)

        # STATISTICS

        statistics = generate_statistics(df)

        # CORRELATION

        correlation = generate_correlation(df)

        # HEALTH SCORE

        health_score = calculate_health_score(
            profile
        )
        risk_report = detect_dataset_risk(
    profile,
    health_score
)
        scorecard = generate_scorecard(
    health_score,
    risk_report
)
        latest_profile = profile
        latest_health_score = health_score
        latest_risk_report = risk_report
        latest_scorecard = scorecard
         
        # INSIGHTS

        insights = generate_insights(
            profile,
            statistics,
            correlation
        )

        # RECOMMENDATIONS

        recommendations = generate_recommendations(
            profile,
            health_score
        )

        # SUMMARY

        summary = generate_summary(
            profile,
            statistics
        )

        # CHARTS

        charts = generate_charts(df)
        chart_image = save_chart_image(df)

        print(
            "Number of charts:",
            len(charts)
        )

        # STORE REPORT DATA

        latest_report_data = prepare_report_data(
            profile,
            statistics,
            summary,
            health_score,
            insights,
            recommendations,
            chart_image
        )
        save_analysis({

    "dataset": file.filename,

    "rows": profile["rows"],

    "columns": profile["columns"],

    "health_score": health_score,

    "date": datetime.now().strftime(
        "%Y-%m-%d %H:%M"
    )

})

        return render_template(
            "analysis.html",
            profile=profile,
            statistics=statistics,
            summary=summary,
            charts=charts,
            health_score=health_score,
            correlation=correlation,
            insights=insights,
            recommendations=recommendations,
            risk_report=risk_report,
            scorecard=scorecard
        )

    return render_template(
        "upload.html"
    )
     

# PDF DOWNLOAD

@app.route("/download/pdf")
def download_pdf():

    global latest_report_data

    if not latest_report_data:
        return "Please upload a dataset first."

    file_path = os.path.join(
        "reports",
        "analytics_report.pdf"
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

    global latest_report_data

    if not latest_report_data:
        return "Please upload a dataset first."

    file_path = os.path.join(
        "reports",
        "analytics_report.docx"
    )

    create_docx_report(
        latest_report_data,
        file_path
    )

    return send_file(
        file_path,
        as_attachment=True
    )
@app.route("/history")
def history():

    records = get_history()

    return render_template(
        "history.html",
        records=records
    )
    
    
@app.route("/compare")
def compare():

    records = get_history()

    if len(records) < 2:

        return "Need at least 2 datasets"

    dataset1 = records[-2]

    dataset2 = records[-1]

    comparison = compare_datasets(
        dataset1,
        dataset2
    )

    return render_template(
        "compare.html",
        dataset1=dataset1,
        dataset2=dataset2,
        comparison=comparison
    )
    
@app.route("/trends")
def trends():

    records = get_history()

    chart = generate_trend_chart(
        records
    )

    return render_template(
        "trends.html",
        chart=chart
    )
    
@app.route(
    "/ask",
    methods=["GET", "POST"]
)
def ask_ai():

    answer = None

    if request.method == "POST":

        question = request.form["question"]

        answer = answer_question(
            question,
            latest_profile,
            latest_health_score,
            latest_risk_report,
            latest_scorecard
        )

    return render_template(
        "chatbot.html",
        answer=answer
    )
if __name__ == "__main__":

    app.run(
        debug=True
    )