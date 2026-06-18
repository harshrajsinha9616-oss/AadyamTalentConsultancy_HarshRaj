import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.data_generator import generate_mock_data
from src.data_cleaner import clean_data
from src.analyzer import run_analysis

def configure_plots():
    # Set premium plotting style
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Helvetica', 'Arial', 'DejaVu Sans']
    plt.rcParams['figure.titlesize'] = 16
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 11
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['grid.alpha'] = 0.3
    plt.rcParams['grid.linestyle'] = '--'

def generate_plots(df, monthly_trends, top_products, category_perf, regional_perf, viz_dir):
    configure_plots()
    os.makedirs(viz_dir, exist_ok=True)
    print("Generating visualizations...")

    # Color Palette: Premium slate, teal, coral, gold
    colors = {
        'primary': '#1A365D',     # Deep Navy
        'secondary': '#0D9488',   # Teal
        'accent': '#F59E0B',      # Gold
        'danger': '#EF4444',      # Coral Red
        'neutral_light': '#F3F4F6' # Warm grey
    }
    sns.set_palette([colors['primary'], colors['secondary'], colors['accent'], colors['danger']])

    # 1. Monthly Sales & Profit Trend (Dual Axis Line Chart)
    fig, ax1 = plt.subplots(figsize=(10, 5.5))
    ax2 = ax1.twinx()

    # Plot Sales on Y1 (Navy)
    line1 = ax1.plot(monthly_trends['Order Month'], monthly_trends['Total_Sales'], 
                     color=colors['primary'], marker='o', linewidth=2.5, label='Monthly Sales ($)')
    # Plot Profit on Y2 (Teal)
    line2 = ax2.plot(monthly_trends['Order Month'], monthly_trends['Total_Profit'], 
                     color=colors['secondary'], marker='s', linewidth=2.0, linestyle='--', label='Monthly Profit ($)')

    ax1.set_xlabel('Month', fontweight='bold', labelpad=10)
    ax1.set_ylabel('Total Sales ($)', color=colors['primary'], fontweight='bold')
    ax2.set_ylabel('Total Profit ($)', color=colors['secondary'], fontweight='bold')

    ax1.tick_params(axis='y', labelcolor=colors['primary'])
    ax2.tick_params(axis='y', labelcolor=colors['secondary'])
    ax1.set_xticklabels(monthly_trends['Order Month'], rotation=30, ha='right')

    # Align legends
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left', frameon=True, facecolor='white', edgecolor='none')

    plt.title('Monthly Sales and Profit Performance Trends (2025)', fontweight='bold', pad=15)
    ax1.grid(True)
    plt.tight_layout()
    plt.savefig(f"{viz_dir}/monthly_sales_trend.png", dpi=150)
    plt.close()
    print("Saved Monthly Sales Trend plot.")

    # 2. Top 10 Best-Selling Products (Horizontal Bar Chart)
    plt.figure(figsize=(10, 6))
    top_products_sorted = top_products.sort_values('Total_Sales', ascending=True)
    
    # Plotting horizontal bars using a palette gradient
    bar_plot = sns.barplot(
        x='Total_Sales', 
        y='Product Name', 
        data=top_products_sorted, 
        palette=sns.color_palette("Blues_d", n_colors=10)
    )

    # Annotate the values on the bars
    for index, value in enumerate(top_products_sorted['Total_Sales']):
        bar_plot.text(value + (df['Sales'].max()*0.01), index, f"${value:,.0f}", 
                     va='center', fontweight='semibold', color='#374151')

    plt.title('Top 10 Best-Selling Products by Sales Revenue', fontweight='bold', pad=15)
    plt.xlabel('Total Sales Revenue ($)', fontweight='bold')
    plt.ylabel('Product Name', fontweight='bold')
    plt.grid(axis='x')
    plt.tight_layout()
    plt.savefig(f"{viz_dir}/top_products.png", dpi=150)
    plt.close()
    print("Saved Top Products plot.")

    # 3. Sales Distribution by Category (Premium Donut Chart)
    plt.figure(figsize=(6.5, 6.5))
    donut_colors = [colors['primary'], colors['secondary'], colors['accent']]
    
    # Plot Pie Chart
    wedges, texts, autotexts = plt.pie(
        category_perf['Total_Sales'],
        labels=category_perf['Category'],
        autopct='%1.1f%%',
        startangle=140,
        colors=donut_colors,
        pctdistance=0.75,
        textprops=dict(color='#111827', fontweight='semibold')
    )
    
    # Change color of text inside pie to white for contrast
    for autotext in autotexts:
        autotext.set_color('white')

    # Draw Center Circle to make it a Donut
    centre_circle = plt.Circle((0,0), 0.55, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.title('Sales Revenue Distribution by Product Category', fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(f"{viz_dir}/sales_by_category.png", dpi=150)
    plt.close()
    print("Saved Sales by Category plot.")

    # 4. Regional Profit & Sales Distribution (Grouped Bar Chart)
    # Melting dataset to easily plot group bar using seaborn
    regional_melt = pd.melt(
        regional_perf, 
        id_vars=['Region'], 
        value_vars=['Total_Sales', 'Total_Profit'],
        var_name='Metric', 
        value_name='Value'
    )
    # Rename metrics for cleaner labels
    regional_melt['Metric'] = regional_melt['Metric'].replace({
        'Total_Sales': 'Sales Revenue',
        'Total_Profit': 'Net Profit'
    })

    plt.figure(figsize=(9, 5.5))
    bar_plot = sns.barplot(
        x='Region', 
        y='Value', 
        hue='Metric', 
        data=regional_melt,
        palette=[colors['primary'], colors['secondary']]
    )

    # Annotate bars with currency format
    for container in bar_plot.containers:
        # Avoid clutter by only formatting values above 1k
        labels = [f"${v.get_height()/1000:,.0f}k" if v.get_height() >= 1000 else f"${v.get_height():,.0f}" for v in container]
        bar_plot.bar_label(container, labels=labels, label_type='edge', padding=3, fontweight='semibold', color='#374151')

    plt.title('Sales Revenue vs Net Profit by Geographical Region', fontweight='bold', pad=15)
    plt.xlabel('Region', fontweight='bold')
    plt.ylabel('Value ($)', fontweight='bold')
    plt.grid(axis='y')
    plt.legend(frameon=True, facecolor='white', edgecolor='none')
    plt.tight_layout()
    plt.savefig(f"{viz_dir}/profit_by_region.png", dpi=150)
    plt.close()
    print("Saved Profit by Region plot.")


def main():
    print("=== Starting E-Commerce Sales Analysis Pipeline ===")
    
    # 1. Paths configuration
    raw_data_path = "dataset/ecommerce_sales_raw.csv"
    clean_data_path = "dataset/ecommerce_sales_clean.csv"
    outputs_dir = "outputs"
    viz_dir = "visualizations"
    
    os.makedirs(outputs_dir, exist_ok=True)
    
    # 2. Step 1: Generate Mock Data (if not already existing or to refresh)
    generate_mock_data(raw_data_path, num_records=1000)
    
    # 3. Step 2: Clean Data
    cleaned_df = clean_data(raw_data_path, clean_data_path)
    
    # 4. Step 3: Run analysis and write CSV outputs
    kpis, monthly_trends, top_products, category_perf, subcategory_perf, regional_perf = run_analysis(cleaned_df, outputs_dir)
    
    # 5. Step 4: Generate visualization charts
    generate_plots(cleaned_df, monthly_trends, top_products, category_perf, regional_perf, viz_dir)
    
    print("=== Pipeline Completed Successfully! ===")

if __name__ == "__main__":
    main()
