import os
import pandas as pd

def load_data(filepath="dataset/StudentsPerformance.csv"):
    """
    Loads student performance dataset from the given path.
    """
    if not os.path.exists(filepath):
        # Fallback to absolute paths if running from subdirs
        alt_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), filepath)
        if os.path.exists(alt_path):
            filepath = alt_path
        else:
            raise FileNotFoundError(f"Dataset not found at {filepath} or {alt_path}")
            
    print(f"Loading dataset from: {filepath}")
    df = pd.read_csv(filepath)
    return df

def preprocess_data(df):
    """
    Checks for missing values and calculates the average score for each student.
    """
    # Check for missing values
    missing_vals = df.isnull().sum()
    print("Checking for missing values:")
    for col, count in missing_vals.items():
        print(f" - {col}: {count} missing value(s)")
        
    # Calculate average score across the three subjects
    df['average_score'] = (df['math score'] + df['reading score'] + df['writing score']) / 3
    print("Calculated 'average_score' for all students.")
    return df
