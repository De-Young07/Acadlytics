import pandas as pd
from src.config import RAW_DATA_PATH, DATASETS
import os

def load_dataset(name):
    path = os.path.join(RAW_DATA_PATH, DATASETS[name])
    df = pd.read_csv(path)
    print(f"{name} loaded: {df.shape}")
    return df

def load_all():
    return {name: load_dataset(name) for name in DATASETS.keys()}