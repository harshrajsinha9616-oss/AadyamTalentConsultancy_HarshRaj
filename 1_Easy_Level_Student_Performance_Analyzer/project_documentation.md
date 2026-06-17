# Project Documentation: Student Performance Analyzer

## 1. Project Overview & Objectives
The purpose of this project is to analyze a dataset of student performance records (containing exam scores across Math, Reading, and Writing) and understand the impact of various demographic and social indicators. Additionally, we train a predictive model to estimate student academic success based on these categorical features.

### Objectives:
*   Identify demographic factors (gender, ethnicity, parental education level) that correlate with higher academic scores.
*   Quantify the impact of school lunch programs and test preparation courses on final performance.
*   Establish a clean, modular Python codebase separating data pipelines, visualization routines, and model training.
*   Build a pipeline regression model to predict overall average scores based on user features.

---

## 2. Dataset Description
The dataset contains **1,000 student records** with the following 8 columns:
*   `gender` (Categorical): Gender of the student (`male`, `female`).
*   `race/ethnicity` (Categorical): Group category (`group A`, `group B`, `group C`, `group D`, `group E`).
*   `parental level of education` (Categorical): Parents' highest education (`some high school`, `high school`, `some college`, `associate's degree`, `bachelor's degree`, `master's degree`).
*   `lunch` (Categorical): School lunch standard (`standard`, `free/reduced`).
*   `test preparation course` (Categorical): Status of test prep completion (`completed`, `none`).
*   `math score` (Numeric): Score out of 100.
*   `reading score` (Numeric): Score out of 100.
*   `writing score` (Numeric): Score out of 100.

---

## 3. Methodology & Implementation

### A. Data Preprocessing & Cleaning
*   **Missing Values**: The dataset is verified for completeness. No null or missing entries were found.
*   **Feature Engineering**: Added the `average_score` variable to represent the overall mean across all three subjects:
    $$\text{Average Score} = \frac{\text{Math Score} + \text{Reading Score} + \text{Writing Score}}{3}$$

### B. Exploratory Data Analysis (EDA)
*   **Gender Averages**: Investigated averages by gender showing that female students generally outperform male students in reading and writing, whereas male students score slightly higher in math on average.
*   **Parental Education Impact**: Students whose parents have earned Master's or Bachelor's degrees achieve the highest average scores, indicating a strong positive correlation between parental education and student academic outcomes.
*   **Outliers/Top Performers**: Filtered out students who have exceptional averages (> 95) to inspect demographic traits of high achievers.

### C. Machine Learning Pipeline
*   **Target Variable**: `average_score` (Numeric)
*   **Input Features**: `gender`, `race/ethnicity`, `parental level of education`, `lunch`, `test preparation course` (All categorical).
*   **Pipeline Setup**:
    1.  **ColumnTransformer / OneHotEncoder**: Encodes all categorical input features into binary dummy variables.
    2.  **Ridge Regressor**: Standard linear regression with L2 regularization ($alpha = 1.0$) to avoid coefficients overfitting to small groups.
*   **Data Split**: 80/20 train-test split (800 train samples, 200 test samples).

---

## 4. Key Findings & Results

### Summary Statistics
*   **Overall Average Score**: 67.77
*   **Math Mean**: 66.09
*   **Reading Mean**: 69.17
*   **Writing Mean**: 68.05

### Model Performance
*   **Mean Squared Error (MSE)**: 179.74
*   **R-squared Score ($R^2$)**: 0.1615

*Note: The $R^2$ score shows that demographic indicators account for roughly 16% of the variance in student performance, showing that while demographics play a significant role, other individual or environment variables contribute to the final grades.*
