import streamlit as st
import pandas as pd
from src.analytics.metrics import AcademicMetrics

# Page config
st.set_page_config(page_title="Acadlytics", layout="wide")
st.title("📊 Acadlytics - FUTMinna Statistics Dashboard")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('data/processed/cleaned_data.csv')

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
selected_course = st.sidebar.selectbox("Select Course", df['course_code'].unique())
selected_semester = st.sidebar.selectbox("Select Semester", df['semester'].unique())

# Calculate metrics
metrics = AcademicMetrics()
pass_rate = metrics.pass_rate(df, selected_course, selected_semester)

# Display metrics
col1, col2, col3 = st.columns(3)
col1.metric("Pass Rate", f"{pass_rate:.1%}")
col2.metric("Total Students", len(df))
col3.metric("Courses", df['course_code'].nunique())

# Visualization
st.subheader("Grade Distribution")
grade_dist = metrics.grade_distribution(df[df['course_code'] == selected_course])
st.bar_chart(grade_dist)