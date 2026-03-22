# Acadlytiics — Metrics & Statistical Definitions

## 1. Purpose
This document defines all statistical metrics used in the system to ensure consistency, interpretability, and reproducibility.

---

## 2. Student Metrics

### Semester GPA
**Definition:** Academic performance within a semester  
**Formula:** GPA = Σ(Grade Point × Credit Units) / Σ(Credit Units)  
**Interpretation:** Higher values indicate better performance  
**Limitation:** Does not account for course difficulty  

---

### Cumulative GPA (CGPA)
**Definition:** Overall academic performance  
**Formula:** CGPA = Σ(Grade Points × Credits) / Total Credits  
**Limitation:** Early poor performance persists over time  

---

### Credit Completion Rate
**Definition:** Percentage of successfully completed credits  
**Formula:** (Credits Earned / Credits Attempted) × 100  

---

### Performance Trend
**Definition:** Change in GPA between semesters  
**Formula:** GPA(t) − GPA(t-1)  

---

## 3. Course Metrics

### Pass Rate
**Formula:** (Number Passed / Total Students) × 100  

---

### Average Score
**Formula:** Σ(Scores) / N  

---

### Score Variance
**Formula:** Σ(X − μ)² / N  

---

### Course Difficulty Indicator
**Definition:** Composite difficulty measure  
**Formula:** Difficulty = (1 − Pass Rate) + Variance  

---

## 4. Lecturer Metrics

### Class Performance Average
Mean score of students taught  

### Pass Rate per Lecturer
Percentage of students passing  

### Student Improvement Rate
(Change in average student performance over time)  

---

## 5. Early Warning Indicators

- GPA drop between semesters  
- Multiple course failures  
- Low performance in foundational courses  

---

## 6. Derived Indicators

### At-Risk Student
- GPA < 2.0 OR declining trend OR repeated failures  

### At-Risk Course
- Low pass rate + low average score  

### Course Bottleneck
- High failure rate in prerequisite courses  

---

## 7. Metric-to-Data Mapping

| Metric | Dataset | Columns |
|------|--------|--------|
| GPA | enrollments | grade_point, credit_units |
| Pass Rate | enrollments | pass |
| Difficulty | enrollments + courses | pass, score |