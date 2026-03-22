import pandas as pd

def clean_students(df):
    df = df.drop_duplicates()
    df = df.dropna(subset=["student_id"])
    return df

def clean_enrollments(df):
    df = df.drop_duplicates()
    
    # Fix ranges
    df = df[(df["score"] >= 0) & (df["score"] <= 100)]
    
    # Handle missing
    df["grade_point"] = df["grade_point"].fillna(0)
    
    return df

def clean_semester_gpa(df):
    df = df.drop_duplicates()
    df = df[(df["semester_gpa"] >= 0) & (df["semester_gpa"] <= 5)]
    return df

def clean_courses(df):
    return df.drop_duplicates()

def clean_resources(df):
    return df.drop_duplicates()