import pandas as pd
import numpy as np

def clean_salary_data(input_path, output_path):
    print("Starting HR Data Cleaning Process...")
    df = pd.read_csv(input_path)
    initial_shape = df.shape
    print(f"Loaded raw dataset with shape: {initial_shape}")

    # 1. Drop Duplicates
    num_duplicates = df.duplicated().sum()
    if num_duplicates > 0:
        df = df.drop_duplicates()
        print(f"Removed {num_duplicates} exact duplicate rows. New shape: {df.shape}")

    # 2. Standardize Department Strings
    # Strip spaces and standard case. Handle acronym 'HR' separately.
    df['Department'] = df['Department'].astype(str).str.strip().str.title()
    df['Department'] = df['Department'].replace({'Hr': 'HR'})
    print("Standardized Department formatting.")

    # 3. Handle Negative Experience Outliers (e.g., -2.0)
    neg_exp_mask = df['Years of Experience'] < 0
    num_neg_exp = neg_exp_mask.sum()
    if num_neg_exp > 0:
        df.loc[neg_exp_mask, 'Years of Experience'] = df.loc[neg_exp_mask, 'Years of Experience'].abs()
        print(f"Corrected {num_neg_exp} negative experience values by converting to absolute positive numbers.")

    # 4. Impute Missing Values in 'Years of Experience'
    # Imputation formula based on Age and average graduation age by Education level
    grad_ages = {
        'High School': 18,
        "Bachelor's": 22,
        "Master's": 24,
        'PhD': 27
    }

    missing_exp_mask = df['Years of Experience'].isna()
    num_missing_exp = missing_exp_mask.sum()
    if num_missing_exp > 0:
        for idx in df[missing_exp_mask].index:
            edu = df.loc[idx, 'Education Level']
            age = df.loc[idx, 'Age']
            grad_age = grad_ages.get(edu, 22) # fallback to 22
            imputed_val = max(0.0, float(age - grad_age))
            df.loc[idx, 'Years of Experience'] = round(imputed_val, 1)
        print(f"Imputed {num_missing_exp} missing 'Years of Experience' values based on Education graduation age.")

    # 5. Handle Negative Salary Outliers
    neg_salary_mask = df['Salary'] < 0
    num_neg_salary = neg_salary_mask.sum()
    if num_neg_salary > 0:
        df.loc[neg_salary_mask, 'Salary'] = df.loc[neg_salary_mask, 'Salary'].abs()
        print(f"Corrected {num_neg_salary} negative Salary values to positive numbers.")

    # 6. Flag Extreme Salary Outliers (e.g., CEO compensation > $500k)
    # Adding a boolean flag for statistical analysis separation
    salary_threshold = 500000.00
    df['Is_Outlier'] = df['Salary'] > salary_threshold
    num_outliers = df['Is_Outlier'].sum()
    print(f"Flagged {num_outliers} extreme salary outliers (compensation > ${salary_threshold:,}).")

    # Save cleaned file
    df.to_csv(output_path, index=False)
    print(f"Cleaned dataset saved successfully to: {output_path}. Final shape: {df.shape}")
    return df

if __name__ == "__main__":
    clean_salary_data("dataset/raw_employee_salaries.csv", "dataset/cleaned_employee_salaries.csv")
