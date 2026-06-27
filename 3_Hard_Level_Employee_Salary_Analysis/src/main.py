import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from src.data_generator import generate_employee_data
from src.data_cleaner import clean_salary_data
from src.statistical_analyzer import run_statistical_analysis

def configure_plots():
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Helvetica', 'Arial', 'DejaVu Sans']
    plt.rcParams['figure.titlesize'] = 16
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 11
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['grid.alpha'] = 0.3
    plt.rcParams['grid.linestyle'] = '--'

def generate_plots(df, corr_matrix, dept_perf, edu_perf, viz_dir):
    configure_plots()
    os.makedirs(viz_dir, exist_ok=True)
    print("Generating visualizations...")

    # Color Palette: Deep Blue, Teal, Amber/Gold, Gray
    colors = {
        'navy': '#1E3A8A',
        'teal': '#0F766E',
        'gold': '#D97706',
        'gray': '#4B5563',
        'light_gray': '#F3F4F6'
    }

    # Filter out outliers for cleaner visualizations (so extreme salaries don't compress scale)
    df_model = df[df['Is_Outlier'] == False]

    # 1. Salary Distribution (Histogram + KDE)
    plt.figure(figsize=(9, 5.5))
    sns.histplot(df_model['Salary'], kde=True, color=colors['navy'], bins=30, alpha=0.7)
    
    mean_sal = df_model['Salary'].mean()
    median_sal = df_model['Salary'].median()
    
    plt.axvline(mean_sal, color=colors['gold'], linestyle='--', linewidth=2, label=f"Mean: ${mean_sal:,.0f}")
    plt.axvline(median_sal, color=colors['teal'], linestyle=':', linewidth=2, label=f"Median: ${median_sal:,.0f}")
    
    plt.title('Employee Salary Distribution & Spread (Excl. Outliers)', fontweight='bold', pad=15)
    plt.xlabel('Annual Salary ($)', fontweight='bold')
    plt.ylabel('Employee Count', fontweight='bold')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{viz_dir}/salary_distribution.png", dpi=150)
    plt.close()
    print("Saved Salary Distribution plot.")

    # 2. Experience vs Salary (Scatter Plot with Regression Line)
    plt.figure(figsize=(9.5, 6))
    # Use seaborn regplot for regression line and 95% confidence interval
    sns.regplot(
        x='Years of Experience', 
        y='Salary', 
        data=df_model, 
        scatter_kws={'alpha': 0.5, 'color': colors['navy'], 's': 25},
        line_kws={'color': colors['gold'], 'linewidth': 2.5, 'label': 'Regression Trend'}
    )
    plt.title('Influence of Experience on Annual Compensation', fontweight='bold', pad=15)
    plt.xlabel('Years of Experience', fontweight='bold')
    plt.ylabel('Salary ($)', fontweight='bold')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{viz_dir}/experience_vs_salary.png", dpi=150)
    plt.close()
    print("Saved Experience vs Salary plot.")

    # 3. Salary by Education Level (Box Plot)
    plt.figure(figsize=(8.5, 5.5))
    edu_order = ['High School', "Bachelor's", "Master's", 'PhD']
    sns.boxplot(
        x='Education Level', 
        y='Salary', 
        data=df_model, 
        order=edu_order,
        palette=[colors['gray'], colors['navy'], colors['teal'], colors['gold']]
    )
    plt.title('Salary Ranges & Spread by Highest Education Level', fontweight='bold', pad=15)
    plt.xlabel('Education Level', fontweight='bold')
    plt.ylabel('Salary ($)', fontweight='bold')
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.savefig(f"{viz_dir}/salary_by_education.png", dpi=150)
    plt.close()
    print("Saved Salary by Education plot.")

    # 4. Salary by Department (Grouped Bar Chart)
    # Melting department average vs median for grouped plotting
    dept_melted = pd.melt(
        dept_perf,
        id_vars=['Department'],
        value_vars=['Average_Salary', 'Median_Salary'],
        var_name='Salary Metric',
        value_name='Value'
    )
    dept_melted['Salary Metric'] = dept_melted['Salary Metric'].replace({
        'Average_Salary': 'Average Salary',
        'Median_Salary': 'Median Salary'
    })

    plt.figure(figsize=(10, 6))
    bar_plot = sns.barplot(
        x='Department',
        y='Value',
        hue='Salary Metric',
        data=dept_melted,
        palette=[colors['navy'], colors['teal']]
    )
    
    # Annotate bars
    for container in bar_plot.containers:
        labels = [f"${v.get_height()/1000:,.0f}k" for v in container]
        bar_plot.bar_label(container, labels=labels, label_type='edge', padding=3, fontweight='semibold', color='#374151', fontsize=9)

    plt.title('Departmental Salary Comparison (Mean vs. Median)', fontweight='bold', pad=15)
    plt.xlabel('Department', fontweight='bold')
    plt.ylabel('Salary ($)', fontweight='bold')
    plt.grid(True, axis='y')
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.savefig(f"{viz_dir}/salary_by_department.png", dpi=150)
    plt.close()
    print("Saved Salary by Department plot.")

    # 5. Correlation Heatmap
    plt.figure(figsize=(7, 6))
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".3f",
        cmap='Blues',
        vmin=-1,
        vmax=1,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": .8}
    )
    plt.title('Statistical Correlation Matrix Heatmap', fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(f"{viz_dir}/correlation_matrix.png", dpi=150)
    plt.close()
    print("Saved Correlation Matrix Heatmap plot.")


def main():
    print("=== Starting HR Salary Analysis Pipeline ===")
    
    raw_data_path = "dataset/raw_employee_salaries.csv"
    clean_data_path = "dataset/cleaned_employee_salaries.csv"
    outputs_dir = "outputs"
    viz_dir = "visualizations"
    
    os.makedirs(outputs_dir, exist_ok=True)
    
    # 1. Generate data
    generate_employee_data(raw_data_path, num_records=1000)
    
    # 2. Clean data
    cleaned_df = clean_salary_data(raw_data_path, clean_data_path)
    
    # 3. Analyze data
    descriptive_stats, corr_matrix, regression_results, dept_perf, edu_perf, gender_perf = run_statistical_analysis(cleaned_df, outputs_dir)
    
    # 4. Generate plots
    generate_plots(cleaned_df, corr_matrix, dept_perf, edu_perf, viz_dir)
    
    print("=== HR Salary Analysis Pipeline Completed Successfully! ===")

if __name__ == "__main__":
    main()
