# E-commerce Sales Analysis Dashboard

## Project Overview
This project focuses on analyzing e-commerce sales data in order to extract useful business insights and visualize key performance indicators (KPIs).

The goal of this project is to explore sales performance, customer behavior, product trends, and regional distribution using **Python (Pandas)** for data preparation and **Power BI** for dashboard creation.

---

## Objectives
The main objectives of this project were:

- Clean and prepare the raw sales dataset
- Explore the structure and quality of the data
- Calculate key business KPIs
- Analyze sales performance by:
  - category
  - year
  - month
  - product
  - state
  - customer segment
- Build an interactive dashboard to support decision-making

---

## Tools & Technologies
- **Python**
- **Pandas**
- **Power BI**
- **CSV dataset**

---

## Dataset Information
The dataset contains transactional e-commerce data, including:

- Order information
- Customer details
- Product details
- Categories and sub-categories
- Sales values
- Shipping and geographic information

### Main columns used:
- `Order Date`
- `Customer ID`
- `Customer Name`
- `Category`
- `Sub-Category`
- `Product Name`
- `Sales`
- `State`
- `Segment`

---

## Data Preparation
The data preparation was done in Python using Pandas.

### Main preprocessing steps:
- Loaded the dataset from CSV
- Converted `Order Date` to datetime format
- Created new time-based columns:
  - `Year`
  - `Month`
  - `Month Name`
- Checked missing values and data types
- Exported cleaned data for Power BI

---

## Key KPIs
The following KPIs were calculated:

- **Total Sales:** 2.26M
- **Total Orders:** 4,922
- **Total Customers:** 793
- **Average Sales:** 230.77

---

## Main Insights

### 1. Sales by Category
- **Technology** generated the highest sales
- Followed by **Furniture**
- Then **Office Supplies**

### 2. Sales by Year
- Sales showed an overall **upward trend**
- **2018** was the best-performing year

### 3. Sales by Month
- Higher sales were observed toward the **end of the year**
- **November** and **December** showed strong performance

### 4. Top Products
- A small number of products contributed significantly to revenue
- High-value products had a strong impact on total sales

### 5. Top States
- **California**, **New York**, and **Texas** were among the strongest markets

### 6. Sales by Segment
- The **Consumer** segment represented the largest share of sales

---

## Dashboard
The Power BI dashboard includes the following visualizations:

- KPI Cards
- Sales by Category
- Sales by Year
- Sales by Month
- Top 10 Products
- Top 10 States
- Sales by Segment

---

## Project Files
This project includes:

- `analysis.py` → Python script used for data analysis and preprocessing
- `train.csv` → original dataset
- `ecommerce_cleaned.csv` → cleaned dataset for Power BI
- Power BI dashboard file (`.pbix`)
- Dashboard screenshot

---

## Conclusion
This project helped me practice the full workflow of a data analysis project:

- data cleaning
- exploratory analysis
- KPI extraction
- business interpretation
- dashboard creation

It also allowed me to strengthen my skills in **Python**, **Pandas**, and **Power BI** while working on a realistic business dataset.

---

## Author
**Aya Dayi**
Master’s student in Computer Science  
Interested in **Data Analysis**, **AI**, and **Business Intelligence**
