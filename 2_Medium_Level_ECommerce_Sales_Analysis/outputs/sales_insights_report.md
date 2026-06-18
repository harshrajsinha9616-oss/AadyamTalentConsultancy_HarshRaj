# Business Insights & Sales Analysis Report 📈💼

**Date:** June 18, 2026  
**Project:** Level 2 - E-Commerce Sales Analysis  
**Prepared By:** Harsh (Data Science Intern, Aadyam Talent Consultancy)

---

## 1. Executive Summary
This report presents key findings from the comprehensive analysis of a year-long transactional e-commerce dataset containing 1,000 distinct orders. The analysis focuses on overall business health, monthly seasonality, category distributions, and regional performance to support data-driven strategy.

### Key Performance Indicators (KPIs)
*   **Total Revenue (Sales):** `$725,527.44`
*   **Total Net Profit:** `$144,857.13`
*   **Overall Profit Margin:** `19.97%`
*   **Total Orders Fulfilled:** `1,000`
*   **Average Order Value (AOV):** `$725.53`

---

## 2. Data Preprocessing & Integrity Report
To ensure reliable analysis, we designed and executed an automated data cleaning pipeline:
*   **Duplicate Elimination:** Detected and removed **14 duplicate transactions** (exact duplicates across all columns).
*   **Missing Product Names:** Fixed **10 records** containing missing product names by applying an `"Unknown Product"` placeholder to preserve financial figures.
*   **Postal Code Formatting:** Rectified **8 missing postal codes** using a `"00000"` placeholder, and standardized all postal codes to a clean, 5-digit string format (preserving leading zeros, e.g., Massachusetts' `02108`).
*   **Categorical Standardization:** Standardized the `Category` column by stripping trailing whitespaces and converting it to title-case (handling formatting anomalies like `" TECHNOLOGY"` or `"furniture"`).
*   **Feature Engineering:** Engineered chronological dimensions (`Order Month`, `Order Month Num`, `Order Quarter`) and calculated the `Profit Margin` per order.

---

## 3. Deep-Dive Insights

### A. Product Category Performance
The business operations span three primary categories. Technology acts as the massive revenue driver, while Furniture and Office Supplies provide stable, supplementary income.

| Category | Total Sales | Total Profit | Net Profit Margin | Avg. Discount |
| :--- | :---: | :---: | :---: | :---: |
| **Technology** | `$426,991.96` | `$81,915.41` | **15.73%** | 9.82% |
| **Furniture** | `$226,293.70` | `$47,926.85` | **19.15%** | 7.30% |
| **Office Supplies** | `$72,241.78` | `$15,014.87` | **18.81%** | 9.70% |

*   *Observation:* Technology generates **58.8% of total revenue** and **56.5% of total profits**. However, its profit margin (15.73%) is lower than Furniture (19.15%) and Office Supplies (18.81%) due to higher relative product costs and promotional discounts.

### B. Geographical Regional Analysis
Sales performance is well-distributed across the four major US regions, with the South and West leading.

*   **South:** `$194,871.92` (265 orders) | Profit: `$38,108.34`
*   **West:** `$190,603.40` (257 orders) | Profit: `$38,928.39`
*   **East:** `$172,607.06` (232 orders) | Profit: `$32,490.42`
*   **Central:** `$167,445.06` (246 orders) | Profit: `$35,329.98`

*   *Observation:* The West region achieved the highest net profit (`$38,928.39`) despite having slightly lower sales than the South, indicating higher operating efficiency or a more profitable product mix in the West.

### C. Monthly Seasonality & Sales Trends
*   **Peak Period (Q4 Spike):** Sales spike significantly in November and December, representing **27% of annual sales**. This is heavily driven by holiday-season purchasing and year-end corporate inventory clearing.
*   **Spring Dip:** Sales experience a decline in January and February, representing the post-holiday slump, before recovering in March.

---

## 4. Actionable Strategic Recommendations

1.  **Discount Control in Technology:**
    *   *Finding:* Technology sales generate the highest revenue but suffer from margin dilution (15.73% compared to ~19% in other categories).
    *   *Action:* Set strict maximum discount thresholds (e.g., capping discounts at 20% instead of 30%+) for high-demand items (like Phones and Accessories) to boost margins.
2.  **Focus on High-Margin Furniture in the South:**
    *   *Finding:* The South has high overall sales, and Furniture possesses a strong 19.15% margin.
    *   *Action:* Run regional marketing campaigns in the South focusing on high-margin home furnishings to capture more profit.
3.  **Prepare for Q4 Seasonal Surge:**
    *   *Finding:* Over a quarter of the company's revenue is generated in the last two months of the year.
    *   *Action:* Formulate inventory stocking plans by October, especially in the South and West regions, to avoid stockouts on best-selling products during the peak holiday surge.
