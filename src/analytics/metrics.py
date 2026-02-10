import pandas as pd

class AcademicMetrics:
    @staticmethod
    def pass_rate(df, course_code=None, semester=None):
        """Calculate pass rate (A-E = pass, F = fail)"""
        subset = df.copy()
        if course_code:
            subset = subset[subset['course_code'] == course_code]
        if semester:
            subset = subset[subset['semester'] == semester]
        
        total = len(subset)
        passes = len(subset[subset['grade'] != 'F'])
        return passes / total if total > 0 else 0
    
    @staticmethod
    def grade_distribution(df):
        """Return grade frequency"""
        return df['grade'].value_counts(normalize=True).sort_index()
    
    @staticmethod  
    def course_difficulty_index(df):
        """Course difficulty = 1 - (average grade points / 5)"""
        avg_points = df.groupby('course_code')['grade_point'].mean()
        return 1 - (avg_points / 5)