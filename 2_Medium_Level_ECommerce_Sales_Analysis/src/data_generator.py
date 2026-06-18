import os
import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_mock_data(output_path, num_records=1000):
    # Ensure reproducibility
    np.random.seed(42)
    random.seed(42)

    # Categories and Sub-categories mapping
    categories = {
        'Furniture': ['Chairs', 'Bookcases', 'Tables', 'Furnishings'],
        'Office Supplies': ['Storage', 'Art', 'Labels', 'Paper', 'Binders', 'Appliances'],
        'Technology': ['Phones', 'Accessories', 'Copiers', 'Machines']
    }

    # Sample products per sub-category
    products = {
        'Chairs': ['HON 5400 Series Task Chair', 'Harbour Executive Leather Armchair', 'Novimex Swivel Chair', 'Global Stack Chair'],
        'Bookcases': ['Atlantic Metal 4-Shelf Bookcase', 'Bush Somerset 3-Shelf Bookcase', 'O\'Sullivan 2-Door Bookcase'],
        'Tables': ['Beverage Air Work Table', 'Bienna Executive Dining Table', 'Balt Training Table'],
        'Furnishings': ['Eldon Desktop Organizer', 'DAX Black Wood Picture Frame', 'Luxo Task Lamp', 'Floor Mat'],
        'Storage': ['Tenex File Box', 'Fellowes Bankers Box', 'Stur-D-Stor Shelving', 'Sterilite Plastic Tubs'],
        'Art': ['Dixon Ticonderoga Pencils', 'Crayola Markers 8ct', 'Fiskars Scissors', 'Sharpie Highlighter Set'],
        'Labels': ['Avery Mailing Labels', 'Dymo Address Labels', 'Brother Label Tape'],
        'Paper': ['Xerox 228 Premium Copy Paper', 'Hammermill Color Copy Paper', 'Southworth Fine Parchment Paper'],
        'Binders': ['Wilson Jones Ring Binder', 'GBC ComboBind Spines', 'Avery Durable View Binder'],
        'Appliances': ['Hoover WindTunnel Vacuum', 'Krups 12-Cup Coffee Maker', 'Avanti Compact Refrigerator'],
        'Phones': ['iPhone 15 Pro Max', 'Samsung Galaxy S24 Ultra', 'Google Pixel 8 Pro', 'Motorola Edge 50'],
        'Accessories': ['Logitech MX Master 3S Mouse', 'Anker USB-C Hub 8-in-1', 'SanDisk 128GB Flash Drive', 'Keychron K2 Mechanical Keyboard'],
        'Copiers': ['Canon ImageClass Laser Copier', 'Hewlett Packard LaserJet Copier', 'Brother Multifunction Copier'],
        'Machines': ['Star Micronics Receipt Printer', 'Dymo LabelWriter 450 Turbo', '3M Laminating Machine']
    }

    # Regions and States mapping
    regions_states = {
        'West': [('California', 'Los Angeles', '90036'), ('Washington', 'Seattle', '98103'), ('Oregon', 'Portland', '97201'), ('Arizona', 'Phoenix', '85001')],
        'East': [('New York', 'New York City', '10011'), ('Massachusetts', 'Boston', '02108'), ('Pennsylvania', 'Philadelphia', '19104'), ('Ohio', 'Columbus', '43215')],
        'Central': [('Texas', 'Houston', '77002'), ('Illinois', 'Chicago', '60611'), ('Michigan', 'Detroit', '48201'), ('Minnesota', 'Minneapolis', '55401')],
        'South': [('Florida', 'Miami', '33101'), ('Georgia', 'Atlanta', '30303'), ('North Carolina', 'Charlotte', '28202'), ('Tennessee', 'Nashville', '37203')]
    }

    ship_modes = ['Standard Class', 'Second Class', 'First Class', 'Same Day']
    segments = ['Consumer', 'Corporate', 'Home Office']

    data = []

    # Time frame: Entire year of 2025
    start_date = datetime(2025, 1, 1)

    for i in range(num_records):
        # Generate Order & Ship Dates
        # Seasonality: Higher probability of order date in November & December (holidays)
        month_probabilities = [0.06, 0.05, 0.07, 0.06, 0.07, 0.07, 0.08, 0.08, 0.09, 0.10, 0.13, 0.14]
        month = np.random.choice(range(1, 13), p=month_probabilities)
        day = random.randint(1, 28)
        order_date = datetime(2025, month, day)

        ship_days = random.choices([1, 2, 3, 4, 5, 6, 7], weights=[10, 20, 30, 20, 10, 5, 5])[0]
        ship_date = order_date + timedelta(days=ship_days)

        order_id = f"CA-2025-{100000 + i}"
        ship_mode = random.choices(ship_modes, weights=[60, 20, 15, 5])[0]
        segment = random.choices(segments, weights=[50, 30, 20])[0]

        # Customer ID and Name
        cust_num = random.randint(10000, 99999)
        customer_id = f"{segment[:2].upper()}-{cust_num}"
        customer_name = f"Customer {cust_num}"

        # Region, State, City, Zip
        region = random.choice(list(regions_states.keys()))
        state, city, zip_code = random.choice(regions_states[region])

        # Category and Product details
        category = random.choices(list(categories.keys()), weights=[30, 50, 20])[0]
        sub_cat = random.choice(categories[category])
        prod_name = random.choice(products[sub_cat])
        prod_id = f"{category[:3].upper()}-{sub_cat[:2].upper()}-{10000000 + i}"

        # Price, Quantity, Discount, Sales, Profit calculation
        # Technology is more expensive, Office Supplies is cheaper
        if category == 'Technology':
            base_price = round(random.uniform(100, 1500), 2)
        elif category == 'Furniture':
            base_price = round(random.uniform(50, 600), 2)
        else: # Office Supplies
            base_price = round(random.uniform(2, 120), 2)

        qty = random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], weights=[30, 25, 20, 10, 7, 3, 2, 1, 1, 1])[0]
        discount = random.choices([0.0, 0.1, 0.2, 0.3, 0.5], weights=[60, 10, 15, 10, 5])[0]

        sales = round((base_price * qty) * (1 - discount), 2)

        # Margin: standard sales profit margin between -20% and 50%
        # High discount usually means negative profit (loss)
        if discount >= 0.3:
            profit_margin = random.uniform(-0.35, -0.05)
        else:
            profit_margin = random.uniform(0.05, 0.45)

        profit = round(sales * profit_margin, 2)

        data.append([
            order_id,
            order_date.strftime('%Y-%m-%d'),
            ship_date.strftime('%Y-%m-%d'),
            ship_mode,
            customer_id,
            customer_name,
            segment,
            city,
            state,
            zip_code,
            region,
            prod_id,
            category,
            sub_cat,
            prod_name,
            sales,
            qty,
            discount,
            profit
        ])

    # Convert to DataFrame
    columns = [
        'Order ID', 'Order Date', 'Ship Date', 'Ship Mode', 'Customer ID',
        'Customer Name', 'Segment', 'City', 'State', 'Postal Code', 'Region',
        'Product ID', 'Category', 'Sub-Category', 'Product Name', 'Sales',
        'Quantity', 'Discount', 'Profit'
    ]
    df = pd.DataFrame(data, columns=columns)

    # --- Introduce anomalies for demonstrating cleaning capabilities ---
    
    # 1. Introduce 15 exact duplicate records
    dup_indices = random.sample(range(num_records), 15)
    duplicates = df.iloc[dup_indices].copy()
    df = pd.concat([df, duplicates], ignore_index=True)

    # 2. Introduce missing values in 'Product Name' (10 rows)
    missing_prod_idx = random.sample(range(len(df)), 10)
    df.loc[missing_prod_idx, 'Product Name'] = np.nan

    # 3. Introduce missing values in 'Postal Code' (8 rows)
    missing_zip_idx = random.sample(range(len(df)), 8)
    df.loc[missing_zip_idx, 'Postal Code'] = np.nan

    # 4. Introduce string formatting issues in Category (e.g. trailing whitespaces, mixed cases)
    dirty_cat_idx = random.sample(range(len(df)), 12)
    df.loc[dirty_cat_idx, 'Category'] = df.loc[dirty_cat_idx, 'Category'].apply(
        lambda x: x.upper() if random.random() > 0.5 else f" {x}  "
    )

    # Create directories if they do not exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save to CSV
    df.to_csv(output_path, index=False)
    print(f"Dataset generated with {len(df)} records (including duplicates/anomalies) at: {output_path}")

if __name__ == "__main__":
    generate_mock_data("dataset/ecommerce_sales_raw.csv")
