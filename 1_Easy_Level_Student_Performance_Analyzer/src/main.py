import sys
import os

# Ensure project root is in python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import load_data, preprocess_data
from src.analyzer import run_descriptive_analysis, filter_top_performers, generate_plots
from src.train import train_predictor_model

def main():
    print("==================================================")
    print("Starting Student Performance Analyzer Pipeline")
    print("==================================================")
    
    # 1. Load data
    df = load_data()
    
    # 2. Preprocess data
    df = preprocess_data(df)
    
    # 3. Descriptive statistical analysis
    run_descriptive_analysis(df)
    
    # 4. Filter top performers
    filter_top_performers(df, threshold=95)
    
    # 5. Generate and save analysis plots
    generate_plots(df)
    
    # 6. Train and evaluate predictive ML model
    train_predictor_model(df)
    
    print("\n==================================================")
    print("Pipeline Execution Completed Successfully!")
    print("All visualizations, models, and outputs generated.")
    print("==================================================")

if __name__ == "__main__":
    main()
