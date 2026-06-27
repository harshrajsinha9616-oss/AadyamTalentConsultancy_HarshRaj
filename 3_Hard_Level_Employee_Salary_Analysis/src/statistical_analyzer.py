import os
import json
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def run_statistical_analysis(df, outputs_dir):
    print("Running HR Statistical Analysis...")
    
    # Split outliers for model training
    df_model = df[df['Is_Outlier'] == False]
    df_outliers = df[df['Is_Outlier'] == True]
    
    # 1. Descriptive Statistics on non-outliers
    descriptive_stats = df_model[['Age', 'Years of Experience', 'Salary']].describe()
    skewness = df_model[['Age', 'Years of Experience', 'Salary']].skew()
    
    # Write summary stats to file
    with open(f"{outputs_dir}/salary_stats_summary.txt", "w") as f:
        f.write("=== Employee Demographics & Salary Summary (Excl. Outliers) ===\n\n")
        f.write(descriptive_stats.to_string())
        f.write("\n\n=== Data Distribution Skewness ===\n")
        for col, val in skewness.items():
            f.write(f"{col}: {val:.4f}\n")
    print("Saved salary descriptive stats to file.")

    # 2. Correlation Matrix
    corr_matrix = df_model[['Age', 'Years of Experience', 'Salary', 'Performance Rating']].corr()
    corr_matrix.to_csv(f"{outputs_dir}/correlation_matrix.csv")
    print("Saved correlation matrix to CSV.")

    # 3. Simple Linear Regression: Salary = f(Experience)
    X = df_model[['Years of Experience']].values
    y = df_model['Salary'].values

    model = LinearRegression()
    model.fit(X, y)
    
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    rmse = np.sqrt(mse)
    
    intercept = model.intercept_
    coef = model.coef_[0]

    regression_results = {
        'Formula': f"Salary = {intercept:.2f} + ({coef:.2f} * Years of Experience)",
        'R_squared': round(r2, 4),
        'Mean_Squared_Error': round(mse, 2),
        'Root_Mean_Squared_Error': round(rmse, 2),
        'Slope_Coefficient (per year increase)': round(coef, 2),
        'Intercept ($)': round(intercept, 2)
    }

    with open(f"{outputs_dir}/regression_metrics.json", "w") as f:
        json.dump(regression_results, f, indent=4)
    print("Saved regression formulas and evaluation metrics to JSON.")

    # 4. Department Performance (Averages)
    dept_performance = df_model.groupby('Department').agg(
        Average_Salary=('Salary', 'mean'),
        Median_Salary=('Salary', 'median'),
        Average_Experience=('Years of Experience', 'mean'),
        Headcount=('Employee ID', 'count')
    ).sort_values('Average_Salary', ascending=False).reset_index()
    dept_performance.to_csv(f"{outputs_dir}/department_performance.csv", index=False)

    # 5. Education Level Performance (Averages)
    edu_performance = df_model.groupby('Education Level').agg(
        Average_Salary=('Salary', 'mean'),
        Median_Salary=('Salary', 'median'),
        Headcount=('Employee ID', 'count')
    ).sort_values('Average_Salary', ascending=False).reset_index()
    edu_performance.to_csv(f"{outputs_dir}/education_performance.csv", index=False)

    # 6. Gender Pay Performance (Averages)
    gender_performance = df_model.groupby('Gender').agg(
        Average_Salary=('Salary', 'mean'),
        Median_Salary=('Salary', 'median'),
        Headcount=('Employee ID', 'count')
    ).reset_index()
    gender_performance.to_csv(f"{outputs_dir}/gender_performance.csv", index=False)
    
    print("Saved group average performance metrics to CSVs.")
    return descriptive_stats, corr_matrix, regression_results, dept_performance, edu_performance, gender_performance

if __name__ == "__main__":
    df = pd.read_csv("dataset/cleaned_employee_salaries.csv")
    os.makedirs("outputs", exist_ok=True)
    run_statistical_analysis(df, "outputs")
