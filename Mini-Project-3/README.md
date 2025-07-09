# 🧠 Retail Orders Data Engineering & Analytics Project (Databricks)

This project demonstrates a complete data engineering and analytics pipeline using **Apache Spark in Databricks**. The goal was to simulate a **real-world retail data workflow**, including:

- Data ingestion
- Data validation
- Cleaning and transformation
- Efficient storage
- Advanced visual analytics

All tasks were performed **entirely within the Databricks environment**, making use of PySpark and interactive dashboards.

---

## 📦 Dataset Overview

The dataset mimics a **retail e-commerce orders system** with the following features:

- 25+ columns including order metadata, customer segmentation, product pricing, discounts, promotions, delivery dates, and ratings.
- Complexities such as:
  - Missing and null values
  - Invalid formats (e.g., `INVALID_DATE`)
  - Duplicate rows
  - Inconsistent schemas (booleans as strings, negative prices, etc.)

---

## 🔄 Project Workflow

### ✅ 1. Data Ingestion
- Imported raw CSV into Databricks using the databricks/volume.
- StructType schema and read as a Spark DataFrame.

### ✅ 2. Data Validation
- Detected missing/null fields across critical columns.
- Checked for:
  - Negative or zero pricing
  - Out-of-bound ratings
  - Invalid dates
  - Duplicated rows
  - Blank or NULL `ProductID`, `CustomerID`, `OrderDate`

### ✅ 3. Data Cleaning & Transformation
- Cleaned and cast date fields to `DateType`.
- Replaced invalid/NULL entries with default values or averages.
- Standardized boolean fields (`TRUE` / `FALSE` → `True` / `False`).
- Calculated new fields:
  - `TotalPrice = Quantity * UnitPrice`
  - `DeliveryTimeDays = DeliveryDate - OrderDate`
  - `IsDelayedDelivery`
- Extracted time-based features (Year, Month).

### ✅ 4. AGGREGATIONS AND BUSINESS METRICS
- SALES PERFORMANCE ANALYSIS
- Sales by country
- Product Performance Analysis
- Customer Segment Analysis
- Payment Method Analysis

### ✅ 5. Data Storage
- Saved the cleaned and transformed dataset in **Parquet format** for optimized performance and storage.

### ✅ 6. Interactive Dashboards (Visual Analytics)
Used Databricks dashboards to visualize insights and monitor key performance metrics:

---

## 📊 Dashboards & Insights

### 🧮 Customer Lifetime Value vs Number of Orders
![image](https://github.com/user-attachments/assets/7e4710bc-d19c-455c-b4c2-523731afc98e)


---

### 🚚 Shipping Status Distribution
![image](https://github.com/user-attachments/assets/3b8def00-f302-4e18-b097-4ebf0f087dfd)


---

### 🌍 Shipping Performance by Country and Status
![image](https://github.com/user-attachments/assets/c16cd71d-75a0-4ec9-895f-6361b2c4954f)


---

### 🔁 Customer Order Frequency Distribution
![image](https://github.com/user-attachments/assets/30fc4768-2714-44bf-a49a-bb91d349abf3)


---

### 📅 Daily Sales with 7-Day Moving Average
![Screenshot 2025-07-10 012856](https://github.com/user-attachments/assets/9af97fde-a21c-4670-bd01-0f74530c6e48)

---

### 💰 Revenue by Customer Segment
![Screenshot 2025-07-10 012720](https://github.com/user-attachments/assets/23d3029c-baa2-412b-a66d-73c3df9811d5)


---

### 🌐 Order Distribution by Country
![Screenshot 2025-07-10 012545](https://github.com/user-attachments/assets/37a1634f-62ed-4e82-89c0-0681177a3a45)


---

### 📈 Order Trends Over Time
![Screenshot 2025-07-10 012502](https://github.com/user-attachments/assets/8c9d926a-b2c4-4b57-a560-2e15646a20d3)


---

### 🕒 Daily Sales (Smoothed View)
![image](https://github.com/user-attachments/assets/4a67ec19-192e-4914-a01a-c75e55362a9d)


---

## 🛠️ Tools Used
- **Apache Spark (PySpark)** — scalable data processing
- **Databricks Notebook** — unified development environment
- **Databricks SQL & Dashboards** — for visual analytics
- **Parquet Format** — optimized data storage

---

## 🏁 Outcomes
- 🚀 Complete hands-on practice in a near-production setup
- ✅ Cleaned & transformed retail dataset using PySpark
- 📈 Multiple business insights generated via dashboards
- 🔄 Ready for integration with BigQuery or Power BI

---

## 📚 Future Scope
- Integrate BigQuery for warehousing
- Build Power BI reports using cleaned data
- Extend dataset to support ML (churn prediction, CLTV modeling)
