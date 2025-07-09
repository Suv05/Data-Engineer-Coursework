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
- Imported raw CSV into Databricks using the FileStore/DBFS.
- Inferred schema and read as a Spark DataFrame.

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

### ✅ 4. Data Storage
- Saved the cleaned and transformed dataset in **Parquet format** for optimized performance and storage.

### ✅ 5. Interactive Dashboards (Visual Analytics)
Used Databricks dashboards to visualize insights and monitor key performance metrics:

---

## 📊 Dashboards & Insights

### 🧮 Customer Lifetime Value vs Number of Orders
![Customer lifetime value vs number of orders](/image/image.png)

---

### 🚚 Shipping Status Distribution
![Shipping status distribution](/image/image-1.png)

---

### 🌍 Shipping Performance by Country and Status
![Shipping performance by country and status](/image/image-2.png)

---

### 🔁 Customer Order Frequency Distribution
![Customer order frequency distribution](/image/image-3.png)

---

### 📅 Daily Sales with 7-Day Moving Average
![Daily sales with 7-day moving average](/image/image-4.png)

---

### 💰 Revenue by Customer Segment
![Revenue by customer segment](/image/image-5.png)

---

### 🌐 Order Distribution by Country
![Order distribution By country](/image/image-6.png)

---

### 📈 Order Trends Over Time
![Order trends over time](/image/image-7.png)

---

### 🕒 Daily Sales (Smoothed View)
![Daily sales with 7-day moving avg ](/image/image-8.png)

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
