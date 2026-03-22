import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed")

DATASETS = {
    "students": "students.csv",
    "courses": "courses.csv",
    "enrollments": "enrollments.csv",
    "semester_gpa": "semester_gpa.csv",
    "resources": "resources.csv"
}