# Employee Salary Analysis 📊💼

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange.svg)](https://scikit-learn.org/)
[![Seaborn](https://img.shields.io/badge/Viz-Seaborn-blueviolet.svg)](https://seaborn.pydata.org/)

An end-to-end HR analytics and statistical modeling project that investigates the impact of demographic indicators, years of experience, education levels, and job titles on employee annual compensation. This project includes modular preprocessing pipelines (imputing missing experience fields, resolving sign typos, filtering executive outliers) and OLS linear regression modeling to build predictive compensation baselines.

This project is part of the **Data Science Internship** at **Aadyam Talent Consultancy (ATC)**.

---

## 📁 Repository Structure

```
3_Hard_Level_Employee_Salary_Analysis/
├── dataset/
│   ├── raw_employee_salaries.csv       # Simulated employee compensation dataset with HR anomalies
│   └── cleaned_employee_salaries.csv   # Cleaned, standardized, and engineered HR dataset
├── outputs/
│   ├── correlation_matrix.csv          # Pearson correlation coefficients between numerical metrics
│   ├── department_performance.csv      # Mean and median salary and experience figures by department
│   ├── education_performance.csv       # Mean and median salaries grouped by highest degree achieved
│   ├── gender_performance.csv          # Salary distribution statistics by gender (Pay Equity audit)
│   ├── hr_insights_report.md           # Executive compensation analysis report & strategic advice
│   ├── regression_metrics.json         # Linear Regression evaluation outputs (R2, coefficients, formula)
│   └── salary_stats_summary.txt        # High-level statistical summaries & distribution skewness
├── src/
│   ├── __init__.py                     # Package marker
│   ├── data_generator.py               # Script simulating HR transactions with formula and anomalies
│   ├── data_cleaner.py                 # cleaner dropping duplicates, imputing experience, fixing signs
│   ├── statistical_analyzer.py         # Module performing correlation, regression, group averages
│   └── main.py                         # Orchestrator running the complete pipeline and generating plots
├── visualizations/
│   ├── correlation_matrix.png          # Correlation coefficient heatmap
│   ├── experience_vs_salary.png        # Scatter plot displaying OLS regression line and confidence interval
│   ├── salary_by_department.png        # Grouped bar chart comparing departmental averages
│   ├── salary_by_education.png         # Box plot showing salary distributions by degree level
│   └── salary_distribution.png         # Histogram + KDE detailing overall salary skewness
├── Employee_Salary_Analysis.ipynb      # Interactive Jupyter Notebook for presentation
├── requirements.txt                   # Project package dependencies
└── README.md                          # Project documentation guide (this file)
```

---

## 🚀 Getting Started

### 1. Installation
Install the necessary python dependencies:
```bash
pip install -r requirements.txt
```

### 2. Running the Data Pipeline
Execute the orchestrator script to generate the raw HR data, clean it, run statistical algorithms, and export the output plots:
```bash
python -m src.main
```

### 3. Running the Jupyter Notebook
Open the interactive presentation notebook to step through code cells and visualizations:
```bash
jupyter notebook Employee_Salary_Analysis.ipynb
```

---

## 📈 Key Statistical Findings

*   **Total Headcount:** `999` (after duplicate cleanup)
*   **Average Compensation:** `$110,035.85` | **Median Compensation:** `$103,773.06`
*   **Regression Formula:**
    $$\text{Salary} = \$79,209.46 + (\$3,960.54 \times \text{Years of Experience})$$
*   **Goodness of Fit ($R^2$):** `0.6466`
    *   *Interpretation:* **64.66% of the variance in employee compensation** is explained solely by their years of experience, showing a highly significant linear relationship.
*   **Annual Raise Value:** `$3,960.54` per year of experience.
*   **Entry-Level baseline (0 years experience):** `$79,209.46`.
*   **Pay Equity Audit:** No systemic gender pay gap observed (Female average salary: `$111,615.43` | Male average salary: `$108,488.23`).

For a detailed breakdown of findings and hiring compensation frameworks, refer to the full [hr_insights_report.md](./outputs/hr_insights_report.md).
