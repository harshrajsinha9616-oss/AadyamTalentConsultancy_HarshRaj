# E-Commerce Sales Analysis 📊🛒

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pandas](https://img.shields.io/badge/Data-Pandas-blueviolet.svg)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Viz-Seaborn-orange.svg)](https://seaborn.pydata.org/)

An end-to-end data science and business intelligence project that generates, cleans, and analyzes transactional sales records for an e-commerce platform. It provides key KPIs, seasonality trends, geographical performance, and category summaries, alongside a trained interactive notebook and strategic business recommendations.

This project is part of the **Data Science Internship** at **Aadyam Talent Consultancy (ATC)**.

---

## 📁 Repository Structure

```
2_Medium_Level_ECommerce_Sales_Analysis/
├── dataset/
│   ├── ecommerce_sales_raw.csv        # Generated raw transaction records (with duplicate/missing anomalies)
│   └── ecommerce_sales_clean.csv      # Cleared and engineered transactional dataset
├── outputs/
│   ├── category_performance.csv       # Summary statistics by product category
│   ├── kpi_summary.txt                # High-level KPIs (Revenue, Profit, Margin, AOV)
│   ├── monthly_sales_trends.csv       # Chronological sales and profit summary
│   ├── regional_performance.csv       # Comparison metrics across geographical regions
│   ├── sales_insights_report.md       # Full executive business report & strategic recommendations
│   ├── subcategory_performance.csv    # Granular product sub-category sales rankings
│   └── top_10_products_sales.csv      # Top 10 revenue-driving products list
├── src/
│   ├── __init__.py                    # Package marker
│   ├── data_generator.py              # Script simulating transactional dataset with anomalies
│   ├── data_cleaner.py                # Preprocessor for duplicates, missing values, date parsing
│   ├── analyzer.py                    # Aggregation and analytics calculation routine
│   └── main.py                        # Orchestrator running the complete pipeline and generating plots
├── visualizations/
│   ├── monthly_sales_trend.png        # Dual-axis sales and profit trends line chart
│   ├── profit_by_region.png           # Sales vs Profit grouped bar chart by region
│   ├── sales_by_category.png          # Donut chart detailing revenue by category
│   └── top_products.png               # Horizontal bar chart displaying top revenue products
├── ECommerce_Sales_Analysis.ipynb      # Interactive Jupyter Notebook for presentation
├── requirements.txt                   # Project dependencies
└── README.md                          # Project-specific documentation (this file)
```

---

## 🚀 Getting Started

### 1. Installation
Clone the repository and install all required python libraries inside your environment:
```bash
pip install -r requirements.txt
```

### 2. Execute Data Pipeline
Run the orchestrator script to automatically generate the raw data, perform the cleaning routine, compute KPIs, and export visualizations:
```bash
python -m src.main
```

### 3. Run Interactive Presentation
Open the Jupyter Notebook to inspect the code cells, dataframes, and plots sequentially:
```bash
jupyter notebook ECommerce_Sales_Analysis.ipynb
```

---

## 📈 Key Analysis Insights Summary

*   **Total Revenue:** `$725,527.44` | **Net Profit:** `$144,857.13` | **Net Margin:** `19.97%`
*   **AOV (Average Order Value):** `$725.53`
*   **Technology Revenue Lead:** Technology is the primary driver, accounting for **58.8% of sales** (`$426.99k`) and **56.5% of total profits** (`$81.92k`).
*   **Q4 Sales Spike:** A heavy retail holiday spike is observed in **November and December**, contributing over **27% of annual sales**, suggesting crucial inventory stocking changes.
*   **Top Region:** The **South** led in total sales (`$194.87k`), whereas the **West** led in overall net profit (`$38.93k`) indicating higher operating margins.

For details on business findings and action items, see the complete [sales_insights_report.md](./outputs/sales_insights_report.md).
