# Acadlytics — Data Dictionary

## Students.csv

| Column | Meaning | Type |
|------|--------|------|
| student_id | Unique ID | String |
| gender | Student gender | String |
| entry_year | Admission year | Integer |
| cohort | Entry group | String |
| program | Course of study | String |

---

## Enrollments.csv

| Column | Meaning | Type |
|------|--------|------|
| student_id | Student ID | String |
| course_code | Course ID | String |
| session | Academic year | String |
| semester | Term | String |
| score | Exam score | Float |
| grade | Letter grade | String |
| grade_point | Numeric grade | Integer |
| pass | Pass indicator | Boolean |
| credit_units | Course weight | Integer |

---

## Semester_GPA.csv

| Column | Meaning | Type |
|------|--------|------|
| student_id | Student ID | String |
| semester_gpa | GPA | Float |
| credits_attempted | Total units | Float |
| credits_earned | Passed units | Float |
