import pandas as pd

def run_analysis(df, outputs_dir):
    print("Running Data Analysis...")
    
    # 1. Key Performance Indicators (KPIs)
    total_sales = round(df['Sales'].sum(), 2)
    total_profit = round(df['Profit'].sum(), 2)
    overall_margin = round((total_profit / total_sales) * 100, 2) if total_sales > 0 else 0.0
    total_orders = df['Order ID'].nunique()
    avg_order_value = round(total_sales / total_orders, 2) if total_orders > 0 else 0.0
    
    kpis = {
        'Total Sales ($)': total_sales,
        'Total Profit ($)': total_profit,
        'Overall Profit Margin (%)': overall_margin,
        'Total Orders': total_orders,
        'Average Order Value ($)': avg_order_value
    }
    
    # Write KPIs to a summary text file
    with open(f"{outputs_dir}/kpi_summary.txt", "w") as f:
        f.write("=== E-Commerce Key Performance Indicators (KPIs) ===\n")
        for k, v in kpis.items():
            f.write(f"{k}: {v:,}\n")
    print("Saved KPI summary to file.")

    # 2. Monthly Sales & Profit Trends
    monthly_trends = df.groupby(['Order Month Num', 'Order Month']).agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum'),
        Order_Count=('Order ID', 'nunique')
    ).reset_index()
    # Sort chronologically by Month Number
    monthly_trends = monthly_trends.sort_values('Order Month Num')
    monthly_trends.to_csv(f"{outputs_dir}/monthly_sales_trends.csv", index=False)
    print("Saved monthly sales and profit trends to CSV.")

    # 3. Product Performance Analysis (Top 10 by Sales)
    top_products_sales = df.groupby('Product Name').agg(
        Total_Sales=('Sales', 'sum'),
        Total_Quantity=('Quantity', 'sum'),
        Total_Profit=('Profit', 'sum')
    ).sort_values('Total_Sales', ascending=False).head(10).reset_index()
    top_products_sales.to_csv(f"{outputs_dir}/top_10_products_sales.csv", index=False)
    print("Saved top 10 products by sales to CSV.")

    # 4. Sales and Profit by Category
    category_performance = df.groupby('Category').agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum'),
        Average_Discount=('Discount', 'mean'),
        Profit_Margin=('Profit Margin', 'mean')
    ).sort_values('Total_Sales', ascending=False).reset_index()
    
    # Format profit margin percentage
    category_performance['Profit_Margin_%'] = round(category_performance['Profit_Margin'] * 100, 2)
    category_performance.to_csv(f"{outputs_dir}/category_performance.csv", index=False)
    print("Saved category performance to CSV.")

    # 5. Sales and Profit by Sub-Category
    subcategory_performance = df.groupby(['Category', 'Sub-Category']).agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum'),
        Total_Quantity=('Quantity', 'sum')
    ).sort_values('Total_Sales', ascending=False).reset_index()
    subcategory_performance.to_csv(f"{outputs_dir}/subcategory_performance.csv", index=False)
    print("Saved sub-category performance to CSV.")

    # 6. Regional Performance
    regional_performance = df.groupby('Region').agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum'),
        Order_Count=('Order ID', 'nunique')
    ).sort_values('Total_Sales', ascending=False).reset_index()
    regional_performance.to_csv(f"{outputs_dir}/regional_performance.csv", index=False)
    print("Saved regional performance to CSV.")

    return kpis, monthly_trends, top_products_sales, category_performance, subcategory_performance, regional_performance

if __name__ == "__main__":
    import os
    df = pd.read_csv("dataset/ecommerce_sales_clean.csv")
    os.makedirs("outputs", exist_ok=True)
    run_analysis(df, "outputs")
