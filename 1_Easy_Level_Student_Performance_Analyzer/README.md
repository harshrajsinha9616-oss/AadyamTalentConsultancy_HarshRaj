# Student Performance Analyzer 📊

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange.svg)](https://scikit-learn.org/)

An end-to-end data analytics and predictive modeling project that investigates demographic impacts (gender, ethnicity, parental education level, lunch type, and test prep) on student academic performance. The project includes modularized Python analysis scripts, automated visualizations, and a regression model pipeline that predicts student average scores based on demographics.

---

## 📁 Repository Structure

```
1_Easy_Level_Student_Performance_Analyzer/
├── dataset/
│   └── StudentsPerformance.csv       # Raw Kaggle student dataset
├── models/
│   └── student_performance_model.pkl  # Trained Ridge Regression pipeline
├── outputs/
│   ├── evaluation_metrics.json       # Model accuracy metrics (MSE, R2)
│   ├── parental_education_ranking.csv # Parental education rankings summary
│   ├── summary_statistics.txt        # Class overall statistics summary
│   └── top_performers.csv            # Filtered list of students with avg score > 95
├── src/
│   ├── __init__.py                   # Package identifier
│   ├── utils.py                      # Data loader and preprocessor helper
│   ├── analyzer.py                   # Exploratory analysis and visual plotting routines
│   ├── train.py                      # Ridge regression training and evaluation
│   └── main.py                       # Orchestrator running the complete pipeline
├── visualizations/
│   ├── average_performance_by_parental_education.png
│   ├── average_score_by_gender_seaborn.png
│   └── average_scores_by_gender.png
├── .gitignore                        # Python git exclusions
├── README.md                         # Main repository index documentation
├── requirements.txt                  # PIP project dependencies
└── StudentPerformanceAnalyze.ipynb   # Interactive analysis notebook
```

---

## 🚀 Getting Started

### 1. Installation
Clone this repository and install the required dependencies using python:
```bash
pip install -r requirements.txt
```

### 2. Running the Data Pipeline
Execute the orchestrator script to run data loading, cleaning, analysis, plot saving, and model training in one command:
```bash
python -m src.main
```

### 3. Interactive Notebook
To play around with the data or inspect the charts interactively, launch your Jupyter environment:
```bash
jupyter notebook StudentPerformanceAnalyze.ipynb
```

---

## 📈 Analysis & Insights Summary

### Overall Statistics
- **Total Students Analyzed**: 1,000
- **Math Score Average**: 66.09
- **Reading Score Average**: 69.17
- **Writing Score Average**: 68.05
- **Overall Class Average**: 67.77

### Parental Education Rankings (Highest to Lowest Score)
1. **Master's Degree** (Avg: 73.60)
2. **Bachelor's Degree** (Avg: 71.92)
3. **Associate's Degree** (Avg: 69.57)
4. **Some College** (Avg: 68.48)
5. **Some High School** (Avg: 65.11)
6. **High School** (Avg: 63.10)

---

## 🤖 Predictive Model Details

We built and trained a machine learning regression model to predict student overall average scores based on their demographic variables (`gender`, `race/ethnicity`, `parental level of education`, `lunch type`, and `test preparation course`). 

- **Algorithm**: Ridge Regression (L2 regularization to prevent overfitting)
- **Feature Preprocessing**: Categorical features are encoded using `OneHotEncoder`.
- **Model Storage**: Saved as a scikit-learn Pipeline at `models/student_performance_model.pkl`.
- **Evaluation Outputs**: Metrics (Mean Squared Error and R-squared score) are outputted to `outputs/evaluation_metrics.json`.

---

## 📄 License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
