import pandas as pd
import numpy as np

def clean_data(input_path, output_path):
    print("Starting Data Cleaning Process...")
    
    # Load raw dataset
    df = pd.read_csv(input_path)
    initial_shape = df.shape
    print(f"Loaded raw dataset with shape: {initial_shape}")
    
    # 1. Handle Duplicates
    num_duplicates = df.duplicated().sum()
    if num_duplicates > 0:
        df = df.drop_duplicates()
        print(f"Removed {num_duplicates} exact duplicate rows. New shape: {df.shape}")
    else:
        print("No duplicate rows found.")
        
    # 2. Standardize Categorical Columns (Mixed cases and trailing whitespaces)
    # Strip spaces and title-case the 'Category' column
    df['Category'] = df['Category'].astype(str).str.strip().str.title()
    print("Standardized 'Category' column formatting.")

    # 3. Handle Missing Values
    # Product Name is key. If missing, we can fill with "Unknown Product" or drop.
    # Let's fill with "Unknown Product" so we don't lose the transactional sales data.
    missing_prods = df['Product Name'].isna().sum()
    if missing_prods > 0:
        df['Product Name'] = df['Product Name'].fillna('Unknown Product')
        print(f"Handled {missing_prods} missing Product Names by filling with 'Unknown Product'.")

    # Postal Code missing values and formatting
    missing_zips = df['Postal Code'].isna().sum()
    df['Postal Code'] = df['Postal Code'].fillna(0).astype(int).astype(str).str.zfill(5)
    if missing_zips > 0:
        print(f"Handled {missing_zips} missing Postal Codes by filling with '00000' placeholder.")
    print("Cleaned and standardized Postal Codes to 5-digit string format.")

    # 4. Standardize and Parse Dates
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    print("Parsed 'Order Date' and 'Ship Date' to datetime objects.")

    # 5. Feature Engineering / Adding Calculated Columns
    # Add date features
    df['Order Year'] = df['Order Date'].dt.year
    df['Order Month Num'] = df['Order Date'].dt.month
    df['Order Month'] = df['Order Date'].dt.strftime('%B')
    df['Order Quarter'] = 'Q' + df['Order Date'].dt.quarter.astype(str)
    
    # Add Profit Margin
    # Avoid division by zero by replacing 0 sales with a small number or handling safely
    df['Profit Margin'] = np.where(df['Sales'] > 0, round(df['Profit'] / df['Sales'], 4), 0.0)
    print("Added calculated columns: Order Year, Order Month Num, Order Month, Order Quarter, and Profit Margin.")

    # Save cleaned dataset
    df.to_csv(output_path, index=False)
    print(f"Cleaned dataset saved successfully to: {output_path}. Final shape: {df.shape}")
    return df

if __name__ == "__main__":
    clean_data("dataset/ecommerce_sales_raw.csv", "dataset/ecommerce_sales_clean.csv")
