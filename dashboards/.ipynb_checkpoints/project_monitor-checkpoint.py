import streamlit as st
import pandas as pd
import json
import os

BASE_PATH = "data"

st.set_page_config(page_title="Acadlytiics Monitor", layout="wide")

st.title("📊 Acadlytiics — Project Monitoring Dashboard")

# -------------------------
# Load Meta Data
# -------------------------
def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

progress = load_json(os.path.join(BASE_PATH, "meta", "progress.json"))
pipeline = load_json(os.path.join(BASE_PATH, "meta", "pipeline_status.json"))

# -------------------------
# PROJECT PROGRESS
# -------------------------
st.header("📌 Project Progress")

for phase, details in progress.items():
    st.subheader(phase.replace("_", " ").title())
    st.progress(details["completion"] / 100)
    st.write(f"Status: {details['status']}")

# -------------------------
# PIPELINE STATUS
# -------------------------
st.header("⚙️ Pipeline Status")

col1, col2, col3 = st.columns(3)

col1.metric("Raw Data Loaded", "✅" if pipeline["raw_data_loaded"] else "❌")
col2.metric("Data Cleaned", "✅" if pipeline["data_cleaned"] else "❌")
col3.metric("Validation Passed", "✅" if pipeline["validation_passed"] else "❌")

st.write(f"Last Pipeline Run: {pipeline['last_run']}")

# -------------------------
# DATASET HEALTH CHECK
# -------------------------
st.header("📂 Dataset Overview")

processed_path = os.path.join(BASE_PATH, "processed")

if os.path.exists(processed_path):
    files = os.listdir(processed_path)

    for file in files:
        df = pd.read_csv(os.path.join(processed_path, file))

        with st.expander(f"{file}"):
            st.write("Shape:", df.shape)
            st.write("Missing Values:", df.isnull().sum().sum())

else:
    st.warning("No processed data available yet.")

# -------------------------
# SIMPLE INSIGHT (LIVE)
# -------------------------
st.header("📈 Quick Insight")

try:
    enrollments = pd.read_csv("data/processed/enrollments_clean.csv")

    pass_rate = enrollments["pass"].mean() * 100

    st.metric("Overall Pass Rate", f"{pass_rate:.2f}%")

except:
    st.info("Processed enrollment data not available yet.")