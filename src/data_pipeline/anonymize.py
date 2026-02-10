def anonymize_data(raw_df):
    """Create safe, shareable version for GitHub"""
    
    # Remove any PII columns
    if 'student_name' in raw_df.columns:
        safe_df = raw_df.drop(columns=['student_name', 'matric_number'])
    
    # Hash student IDs consistently
    if 'student_id' in raw_df.columns:
        safe_df['student_hash'] = raw_df['student_id'].apply(
            lambda x: hashlib.md5(str(x).encode()).hexdigest()[:8]
        )
        safe_df = safe_df.drop(columns=['student_id'])
    
    # Save processed version (can be shared)
    safe_df.to_csv('data/processed/anonymized_grades.csv', index=False)
    return safe_df