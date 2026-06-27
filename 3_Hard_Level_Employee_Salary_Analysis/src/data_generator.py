import os
import random
import pandas as pd
import numpy as np

def generate_employee_data(output_path, num_records=1000):
    # Set seed for reproducibility
    np.random.seed(42)
    random.seed(42)

    departments = {
        'Engineering': ['Software Engineer', 'Senior Engineer', 'Tech Lead', 'Engineering Manager'],
        'Data Science': ['Data Analyst', 'Data Scientist', 'Senior Data Scientist', 'Data Science Manager'],
        'HR': ['HR Associate', 'HR Specialist', 'HR Manager'],
        'Sales': ['Sales Associate', 'Sales Representative', 'Sales Manager'],
        'Finance': ['Financial Analyst', 'Senior Finance Analyst', 'Finance Manager'],
        'Executive': ['Director', 'Vice President']
    }

    education_levels = ['High School', "Bachelor's", "Master's", 'PhD']
    genders = ['Male', 'Female', 'Non-binary']
    remote_statuses = ['Remote', 'Hybrid', 'On-site']

    data = []

    for i in range(num_records):
        emp_id = f"EMP-{1000 + i}"
        gender = random.choices(genders, weights=[48, 48, 4])[0]
        education = random.choices(education_levels, weights=[10, 55, 25, 10])[0]

        # Determine age (normally between 21 and 65)
        age = int(np.clip(np.random.normal(38, 10), 21, 65))

        # Select department and job title
        # Executive department is reserved for older/more experienced employees
        if age > 40 and random.random() < 0.15:
            dept = 'Executive'
        else:
            dept = random.choice([d for d in departments.keys() if d != 'Executive'])

        job_title = random.choice(departments[dept])

        # Experience calculation based on age and education graduation times
        grad_age = 18
        if education == "Bachelor's":
            grad_age = 22
        elif education == "Master's":
            grad_age = 24
        elif education == "PhD":
            grad_age = 27

        max_possible_exp = max(0, age - grad_age)
        if max_possible_exp > 0:
            exp = round(random.uniform(0, max_possible_exp), 1)
        else:
            exp = 0.0

        # Formula-based Salary with realistic parameters
        base_salary = 45000
        exp_multiplier = 4200 * exp
        
        # Education premium
        edu_premium = 0
        if education == "Bachelor's":
            edu_premium = 8000
        elif education == "Master's":
            edu_premium = 20000
        elif education == "PhD":
            edu_premium = 35000

        # Department bonus
        dept_bonus = 0
        if dept == 'Engineering':
            dept_bonus = 15000
        elif dept == 'Data Science':
            dept_bonus = 18000
        elif dept == 'Finance':
            dept_bonus = 8000
        elif dept == 'Sales':
            dept_bonus = 5000
        elif dept == 'Executive':
            dept_bonus = 40000

        # Role modifier (Managers/Leads earn more)
        role_modifier = 0
        if any(keyword in job_title for keyword in ['Manager', 'Lead', 'Director', 'Vice President']):
            role_modifier = 25000

        # Performance rating (1 to 5)
        perf_rating = int(np.clip(np.random.normal(3.2, 0.8), 1, 5))
        perf_bonus = (perf_rating - 3) * 3000  # positive bonus for 4 or 5, penalty for 1 or 2

        # Random noise (standard deviation $6,000)
        noise = np.random.normal(0, 6000)

        # Calculate final salary
        salary = base_salary + exp_multiplier + edu_premium + dept_bonus + role_modifier + perf_bonus + noise
        salary = round(max(30000, salary), 2)  # minimum salary floor

        remote_status = random.choices(remote_statuses, weights=[35, 45, 20])[0]

        data.append([
            emp_id,
            age,
            gender,
            education,
            dept,
            job_title,
            exp,
            salary,
            perf_rating,
            remote_status
        ])

    columns = [
        'Employee ID', 'Age', 'Gender', 'Education Level', 'Department',
        'Job Title', 'Years of Experience', 'Salary', 'Performance Rating', 'Work Mode'
    ]
    df = pd.DataFrame(data, columns=columns)

    # --- Introduce anomalies to demonstrate cleaning capabilities ---

    # 1. 15 duplicate rows
    dup_indices = random.sample(range(num_records), 15)
    df = pd.concat([df, df.iloc[dup_indices]], ignore_index=True)

    # 2. Missing values in Years of Experience (12 rows)
    missing_exp_idx = random.sample(range(len(df)), 12)
    df.loc[missing_exp_idx, 'Years of Experience'] = np.nan

    # 3. Inconsistent spacing/casing in Department names (15 rows)
    dirty_dept_idx = random.sample(range(len(df)), 15)
    for idx in dirty_dept_idx:
        dept_val = df.loc[idx, 'Department']
        if random.random() > 0.5:
            df.loc[idx, 'Department'] = f"   {dept_val}  "
        else:
            df.loc[idx, 'Department'] = dept_val.lower()

    # 4. Outliers: Negative Salary (3 rows)
    neg_sal_idx = random.sample(range(len(df)), 3)
    df.loc[neg_sal_idx, 'Salary'] = df.loc[neg_sal_idx, 'Salary'] * -1.0

    # 5. Outliers: Negative Experience (2 rows)
    neg_exp_idx = random.sample(range(len(df)), 2)
    df.loc[neg_exp_idx, 'Years of Experience'] = -2.0

    # 6. Outliers: Extreme Salaries (2 rows)
    extreme_sal_idx = random.sample(range(len(df)), 2)
    df.loc[extreme_sal_idx[0], 'Salary'] = 1200000.00
    df.loc[extreme_sal_idx[1], 'Salary'] = 950000.00

    # Save to directory
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Mock HR dataset generated successfully at: {output_path} with shape {df.shape}")

if __name__ == "__main__":
    generate_employee_data("dataset/raw_employee_salaries.csv")
