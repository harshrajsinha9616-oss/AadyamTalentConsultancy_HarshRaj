# Compensation & HR Statistical Analysis Report 📊💼

**Date:** June 27, 2026  
**Project:** Level 3 - Employee Salary Analysis  
**Prepared For:** Aadyam Talent Consultancy (ATC)  
**Prepared By:** Harsh (Data Science Intern, Aadyam Talent Consultancy)

---

## 1. Executive Summary
This report details the statistical findings from our employee compensation analysis based on a dataset of 1,000 records. Using descriptive statistics, correlation matrices, and ordinary least squares (OLS) linear regression, we modeled the relationship between experience and compensation. This analysis helps ATC optimize hiring salary packages, evaluate pay equity, and design structured compensation bands.

### Key Demographics & Salary KPIs (Excluding Outliers)
*   **Total Headcount:** `999`
*   **Average Salary:** `$110,035.85`
*   **Median Salary:** `$103,773.06`
*   **Average Experience:** `7.78 years`
*   **AOV (Average Age):** `38.19 years`

---

## 2. Preprocessing & Data Integrity Audit
To build a reliable statistical model, we executed a robust data cleaning pipeline:
*   **Duplicate Removal:** Identified and eliminated **14 identical duplicate records**.
*   **Department Casing:** Normalized inconsistent case and trailing spacing issues (e.g. `"hr"`, `"  Engineering  "`).
*   **Experience Imputation:** Resolved **12 missing entries** in "Years of Experience" by imputing values based on age and average graduation times (e.g., age minus 22 for Bachelor's degree holders).
*   **Negative Values Correction:** Corrected **2 negative experience** entries and **3 negative salaries** by converting them to absolute positive values (handling keying/data-entry errors).
*   **Statistical Outlier Flagging:** Identified **2 extreme salaries** ($1.2M and $950K) as outliers. These were flagged and excluded from the statistical model training to prevent coefficient distortion, while retaining them in the overall clean database.

---

## 3. Compensation Regression Model & Statistical Insights

### A. Experience vs. Salary Regression
We fitted a Simple Linear Regression model to predict salary based on years of experience. The model is represented by the following formula:

$$\text{Salary} = \$79,209.46 + (\$3,960.54 \times \text{Years of Experience})$$

*   **Model Fit ($R^2$):** `0.6466`
    *   *Interpretation:* **64.66% of the variance in employee salaries** is explained by their years of experience. This shows a very strong, statistically significant linear relationship.
*   **Annual Experience Increment (Slope):** `$3,960.54`
    *   *Interpretation:* For each additional year of experience, an employee's salary increases by an average of `$3,960.54`.
*   **Base Entry Salary (Intercept):** `$79,209.46`
    *   *Interpretation:* The starting salary for an employee with 0 years of experience averages `$79,209.46` across all departments.

### B. Correlation Analysis
The Pearson correlation coefficients ($r$) reveal strong relationships:
*   **Years of Experience & Salary:** `0.804` (Very strong positive correlation)
*   **Age & Salary:** `0.334` (Moderate positive correlation)
*   **Performance Rating & Salary:** `0.112` (Weak positive correlation, indicating that base experience/role determines salary scale rather than ratings)

---

## 4. Group Comparison Analyses

### A. Departmental Pay Scale
The average and median salaries vary by department, with technical and leadership roles leading:

*   **Executive:** Average `$164,991.83` | Median `$159,771.20`
*   **Engineering:** Average `$117,056.47` | Median `$111,296.01`
*   **Data Science:** Average `$112,403.33` | Median `$105,504.33`
*   **Finance:** Average `$104,835.33` | Median `$99,416.29`
*   **Sales:** Average `$103,461.96` | Median `$100,703.20`
*   **HR:** Average `$97,308.80` | Median `$92,327.37`

### B. Education Premium
Higher education levels correspond to higher average salaries, indicating a clear "education premium":
*   **PhD:** `$125,388.47` (Average)
*   **Master's:** `$112,392.82` (Average)
*   **Bachelor's:** `$107,360.68` (Average)
*   **High School:** `$104,852.81` (Average)

### C. Pay Equity Audit (Gender)
Analyzing salaries across genders shows a well-balanced distribution with no systemic pay gap:
*   **Female:** Average `$111,615.43` | Headcount: 452
*   **Male:** Average `$108,488.23` | Headcount: 512
*   **Non-binary:** Average `$112,276.09` | Headcount: 35

---

## 5. Strategic Recommendations for ATC Clients

1.  **Standardize compensation packages using the regression model**:
    *   Use the baseline formula: $\text{Base} + \$3,960 \times \text{Experience}$ as a benchmark for job offers to minimize bidding wars and maintain equity.
2.  **Define Structured Job-Bandings**:
    *   *Junior (0-3 yrs):* `$79,200` to `$91,000`
    *   *Mid-Level (4-8 yrs):* `$95,000` to `$111,000`
    *   *Senior (9+ yrs):* `$115,000+`
3.  **Implement Standardized Education Adjustments**:
    *   Apply standard salary premiums over the base package: **+$5,000** for a Master's degree, and **+$18,000** for a PhD.
