def validate_ranges(df, column, min_val, max_val):
    invalid = df[(df[column] < min_val) | (df[column] > max_val)]
    return len(invalid)

def validate_enrollments(df):
    errors = {}
    
    errors["score_errors"] = validate_ranges(df, "score", 0, 100)
    errors["grade_point_errors"] = validate_ranges(df, "grade_point", 0, 5)
    
    return errors