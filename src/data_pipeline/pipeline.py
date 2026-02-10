import pandas as pd
from pathlib import Path

class AcadlyticsPipeline:
    def __init__(self):
        self.raw_path = Path('data/raw')
        self.processed_path = Path('data/processed')
        
    def run(self):
        """Main pipeline execution"""
        df = self.extract()
        df = self.transform(df)
        self.load(df)
        return df
    
    def extract(self):
        # Load all data files
        files = list(self.raw_path.glob('*.csv'))
        dfs = [pd.read_csv(f) for f in files]
        return pd.concat(dfs, ignore_index=True)
    
    def transform(self, df):
        # Clean and standardize
        df['grade'] = df['grade'].str.upper().str.strip()
        df['semester'] = df['semester'].str.upper()
        
        # Calculate derived columns
        grade_points = {'A':5, 'B':4, 'C':3, 'D':2, 'E':1, 'F':0}
        df['grade_point'] = df['grade'].map(grade_points)
        
        return df
    
    def load(self, df):
        # Save to processed folder
        output_file = self.processed_path / 'cleaned_data.csv'
        df.to_csv(output_file, index=False)
        print(f"Saved cleaned data to {output_file}")