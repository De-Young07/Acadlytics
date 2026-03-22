import os
from src.load_data import load_all
from src.clean_data import *
from src.validate_data import *
from src.config import PROCESSED_DATA_PATH

def save(df, name):
    path = os.path.join(PROCESSED_DATA_PATH, f"{name}_clean.csv")
    df.to_csv(path, index=False)
    print(f"Saved: {name}")

def run_pipeline():
    data = load_all()
    
    # Cleaning
    students = clean_students(data["students"])
    courses = clean_courses(data["courses"])
    enrollments = clean_enrollments(data["enrollments"])
    semester_gpa = clean_semester_gpa(data["semester_gpa"])
    resources = clean_resources(data["resources"])
    
    # Validation
    errors = validate_enrollments(enrollments)
    print("Validation Results:", errors)
    
    # Save outputs
    save(students, "students")
    save(courses, "courses")
    save(enrollments, "enrollments")
    save(semester_gpa, "semester_gpa")
    save(resources, "resources")

if __name__ == "__main__":
    run_pipeline()