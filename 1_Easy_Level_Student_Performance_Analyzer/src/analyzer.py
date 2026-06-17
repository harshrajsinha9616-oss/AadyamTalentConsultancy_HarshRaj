import os
import matplotlib.pyplot as plt
import seaborn as sns

def get_output_path(filename, folder="outputs"):
    """
    Returns the correct path for outputting files, relative to the project root.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(base_dir, folder)
    os.makedirs(target_dir, exist_ok=True)
    return os.path.join(target_dir, filename)

def run_descriptive_analysis(df):
    """
    Computes subject means and saves the text summary to outputs/summary_statistics.txt.
    """
    math_avg = df['math score'].mean()
    reading_avg = df['reading score'].mean()
    writing_avg = df['writing score'].mean()
    
    summary_text = (
        "=== Student Performance Analyzer Summary Statistics ===\n"
        f"Total Students: {len(df)}\n"
        f"Math Score Average: {math_avg:.2f}\n"
        f"Reading Score Average: {reading_avg:.2f}\n"
        f"Writing Score Average: {writing_avg:.2f}\n"
        f"Overall Class Average Score: {df['average_score'].mean():.2f}\n"
    )
    
    print("\nDescriptive Analysis Results:")
    print(summary_text)
    
    output_file = get_output_path("summary_statistics.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(summary_text)
    print(f"Summary statistics saved to: {output_file}")
    
    # Save parental education rankings
    edu_ranking = df.groupby('parental level of education')['average_score'].mean().sort_values(ascending=False)
    edu_file = get_output_path("parental_education_ranking.csv")
    edu_ranking.to_csv(edu_file)
    print(f"Parental education rankings saved to: {edu_file}")

def filter_top_performers(df, threshold=95):
    """
    Filters students with an average score higher than the threshold and saves them to csv.
    """
    top_df = df[df['average_score'] > threshold]
    print(f"\nFound {len(top_df)} students with average score > {threshold}.")
    
    output_file = get_output_path("top_performers.csv")
    top_df.to_csv(output_file, index=False)
    print(f"Top performers list saved to: {output_file}")
    return top_df

def generate_plots(df):
    """
    Generates analysis plots and saves them to the visualizations/ directory.
    """
    # Set the style
    sns.set_theme(style="whitegrid")
    
    # 1. Average scores by gender
    gender_group = df.groupby('gender')[['math score', 'reading score', 'writing score']].mean()
    plt.figure(figsize=(10, 6))
    gender_group.plot(kind='bar', figsize=(10, 6))
    plt.title('Average Scores by Gender')
    plt.ylabel('Average Score')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plot1_path = get_output_path("average_scores_by_gender.png", folder="visualizations")
    plt.savefig(plot1_path, dpi=300)
    plt.close()
    print(f"Saved plot: {plot1_path}")
    
    # 2. Average performance by parental education
    top_groups = df.groupby('parental level of education')['average_score'].mean().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_groups.values, y=top_groups.index, hue=top_groups.index, palette='magma', legend=False)
    plt.title('Average Performance by Parental Education Level')
    plt.xlabel('Average Score')
    plt.ylabel('Parental Education Level')
    plt.tight_layout()
    plot2_path = get_output_path("average_performance_by_parental_education.png", folder="visualizations")
    plt.savefig(plot2_path, dpi=300)
    plt.close()
    print(f"Saved plot: {plot2_path}")
    
    # 3. Seaborn Average score by gender
    plt.figure(figsize=(8, 6))
    sns.barplot(x='gender', y='average_score', data=df, palette='muted')
    plt.title('Average Score by Gender (Seaborn)')
    plt.ylabel('Average Score')
    plt.xlabel('Gender')
    plt.tight_layout()
    plot3_path = get_output_path("average_score_by_gender_seaborn.png", folder="visualizations")
    plt.savefig(plot3_path, dpi=300)
    plt.close()
    print(f"Saved plot: {plot3_path}")
