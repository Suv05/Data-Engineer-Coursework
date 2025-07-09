# PySpark E-commerce Data Analysis - Complete Practice Session
# ================================================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("E-commerce Data Analysis") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .getOrCreate()

print("Spark Session Created Successfully!")
print(f"Spark Version: {spark.version}")

# ================================================================
# 1. DATA LOADING AND SCHEMA DEFINITION
# ================================================================

# Define schema for better performance and data validation
schema = StructType([
    StructField("OrderID", StringType(), True),
    StructField("CustomerID", StringType(), True),
    StructField("ProductID", StringType(), True),
    StructField("ProductName", StringType(), True),
    StructField("Quantity", IntegerType(), True),
    StructField("UnitPrice", DecimalType(10, 2), True),  
    StructField("OrderDate", StringType(), True),       # Load as string first
    StructField("Country", StringType(), True),
    StructField("PaymentMethod", StringType(), True),
    StructField("ShippingStatus", StringType(), True),
    StructField("CustomerSegment", StringType(), True),
    StructField("DiscountCode", StringType(), True),
    StructField("PromotionApplied", StringType(), True), # Load as string first
    StructField("CustomerRating", IntegerType(), True),
    StructField("DeliveryDate", StringType(), True),     # Load as string first
    StructField("Notes", StringType(), True),
    StructField("ReturnReason", StringType(), True)
])

# Load the CSV data
df = spark.read.csv("ecommerce_data.csv", header=True, schema=schema)

print("Data loaded successfully!")
print(f"Total records: {df.count()}")
print(f"Total columns: {len(df.columns)}")

# Display basic info about the dataset
df.printSchema()
df.show(5, truncate=False)

# ================================================================
# 2. DATA EXPLORATION AND QUALITY ASSESSMENT
# ================================================================

print("\n" + "="*50)
print("DATA EXPLORATION AND QUALITY ASSESSMENT")
print("="*50)

# Check data types and basic statistics
print("\nColumn Data Types:")
for col_name, col_type in df.dtypes:
    print(f"{col_name}: {col_type}")

# Check for missing values
print("\nMissing Values Analysis:")
missing_counts = df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns])
missing_counts.show()

# Check for duplicate records
print(f"\nDuplicate Records: {df.count() - df.dropDuplicates().count()}")

# Basic statistics for numeric columns
print("\nNumeric Columns Statistics:")
numeric_cols = ['Quantity', 'UnitPrice', 'CustomerRating']
df.select(numeric_cols).describe().show()

# Check unique values for categorical columns
print("\nUnique Values in Categorical Columns:")
categorical_cols = ['Country', 'PaymentMethod', 'ShippingStatus', 'CustomerSegment']
for col_name in categorical_cols:
    unique_count = df.select(col_name).distinct().count()
    print(f"{col_name}: {unique_count} unique values")
    df.groupBy(col_name).count().orderBy(desc("count")).show(10)

# ================================================================
# 3. DATA CLEANING AND QUALITY ISSUES IDENTIFICATION
# ================================================================

print("\n" + "="*50)
print("DATA CLEANING")
print("="*50)

# Identify and handle data quality issues

# 1. Invalid dates
print("\nChecking for invalid dates:")
df_with_date_check = df.withColumn("is_valid_date", 
    when(col("OrderDate").rlike(r'^\d{4}-\d{2}-\d{2}$'), True).otherwise(False))

invalid_dates = df_with_date_check.filter(col("is_valid_date") == False)
print(f"Records with invalid dates: {invalid_dates.count()}")
invalid_dates.select("OrderID", "OrderDate").show()

# 2. Negative prices
print("\nChecking for negative prices:")
negative_prices = df.filter(col("UnitPrice") < 0)
print(f"Records with negative prices: {negative_prices.count()}")
negative_prices.select("OrderID", "ProductName", "UnitPrice").show()

# 3. Null payment methods
print("\nChecking for null payment methods:")
null_payments = df.filter(col("PaymentMethod").isNull())
print(f"Records with null payment methods: {null_payments.count()}")

# 4. Duplicate orders (same OrderID, ProductID combination)
print("\nChecking for potential duplicate line items:")
duplicate_items = df.groupBy("OrderID", "ProductID").count().filter(col("count") > 1)
print(f"Duplicate line items: {duplicate_items.count()}")
duplicate_items.show()

# ================================================================
# 4. DATA TRANSFORMATION AND CLEANING
# ================================================================

print("\n" + "="*50)
print("DATA TRANSFORMATION")
print("="*50)

# Create cleaned dataset
df_clean = df.filter(
    (col("OrderDate").rlike(r'^\d{4}-\d{2}-\d{2}$')) &  # Valid dates only
    (col("UnitPrice") >= 0) &  # Non-negative prices
    (col("Quantity") > 0)  # Positive quantities
)

print(f"Records after basic cleaning: {df_clean.count()}")

# Convert date strings to proper date types with error handling
df_clean = df_clean.withColumn("OrderDate", 
    when(col("OrderDate").rlike(r"^\d{4}-\d{2}-\d{2}$"), 
         to_date(col("OrderDate"), "yyyy-MM-dd")).otherwise(None))

# Handle missing payment methods
df_clean = df_clean.withColumn("PaymentMethod",
    when(col("PaymentMethod").isNull(), "Unknown").otherwise(col("PaymentMethod")))

# Create derived columns
df_clean = df_clean.withColumn("TotalAmount", col("Quantity") * col("UnitPrice"))

# Extract date components
df_clean = df_clean.withColumn("OrderYear", year(col("OrderDate"))) \
                   .withColumn("OrderMonth", month(col("OrderDate"))) \
                   .withColumn("OrderWeek", weekofyear(col("OrderDate"))) \
                   .withColumn("OrderDayOfWeek", dayofweek(col("OrderDate")))

# Calculate delivery time (if both dates are available)
df_clean = df_clean.withColumn("DeliveryDays",
    when(col("DeliveryDate").isNotNull(), 
         datediff(col("DeliveryDate"), col("OrderDate")))
    .otherwise(None))

# Create customer value segments based on total amount
df_clean = df_clean.withColumn("OrderValueSegment",
    when(col("TotalAmount") >= 1000, "High Value")
    .when(col("TotalAmount") >= 500, "Medium Value")
    .otherwise("Low Value"))

print("Data transformation completed!")
df_clean.printSchema()

# ================================================================
# 5. AGGREGATIONS AND BUSINESS METRICS
# ================================================================

print("\n" + "="*50)
print("BUSINESS METRICS AND AGGREGATIONS")
print("="*50)

# 1. Sales Performance Analysis
print("\n1. SALES PERFORMANCE ANALYSIS")
print("-" * 30)

# Total sales by month
monthly_sales = df_clean.groupBy("OrderYear", "OrderMonth") \
    .agg(
        sum("TotalAmount").alias("TotalSales"),
        count("OrderID").alias("TotalOrders"),
        countDistinct("CustomerID").alias("UniqueCustomers"),
        avg("TotalAmount").alias("AvgOrderValue")
    ).orderBy("OrderYear", "OrderMonth")

print("Monthly Sales Summary:")
monthly_sales.show()

# Sales by country
country_sales = df_clean.groupBy("Country") \
    .agg(
        sum("TotalAmount").alias("TotalSales"),
        count("OrderID").alias("TotalOrders"),
        countDistinct("CustomerID").alias("UniqueCustomers")
    ).orderBy(desc("TotalSales"))

print("Sales by Country:")
country_sales.show()

# 2. Product Performance Analysis
print("\n2. PRODUCT PERFORMANCE ANALYSIS")
print("-" * 30)

product_performance = df_clean.groupBy("ProductID", "ProductName") \
    .agg(
        sum("Quantity").alias("TotalQuantitySold"),
        sum("TotalAmount").alias("TotalRevenue"),
        count("OrderID").alias("TimesOrdered"),
        avg("UnitPrice").alias("AvgUnitPrice"),
        avg("CustomerRating").alias("AvgRating")
    ).orderBy(desc("TotalRevenue"))

print("Top 10 Products by Revenue:")
product_performance.show(10)

# 3. Customer Segment Analysis
print("\n3. CUSTOMER SEGMENT ANALYSIS")
print("-" * 30)

customer_segment_analysis = df_clean.groupBy("CustomerSegment") \
    .agg(
        count("OrderID").alias("TotalOrders"),
        sum("TotalAmount").alias("TotalRevenue"),
        avg("TotalAmount").alias("AvgOrderValue"),
        avg("CustomerRating").alias("AvgRating"),
        countDistinct("CustomerID").alias("UniqueCustomers")
    ).orderBy(desc("TotalRevenue"))

print("Customer Segment Performance:")
customer_segment_analysis.show()

# 4. Payment Method Analysis
print("\n4. PAYMENT METHOD ANALYSIS")
print("-" * 30)

payment_analysis = df_clean.groupBy("PaymentMethod") \
    .agg(
        count("OrderID").alias("TotalOrders"),
        sum("TotalAmount").alias("TotalRevenue"),
        avg("TotalAmount").alias("AvgOrderValue")
    ).orderBy(desc("TotalOrders"))

print("Payment Method Usage:")
payment_analysis.show()

# ================================================================
# 6. ADVANCED ANALYTICS
# ================================================================

print("\n" + "="*50)
print("ADVANCED ANALYTICS")
print("="*50)

# 1. Customer Lifetime Value (CLV) Analysis
print("\n1. CUSTOMER LIFETIME VALUE ANALYSIS")
print("-" * 30)

customer_clv = df_clean.groupBy("CustomerID") \
    .agg(
        sum("TotalAmount").alias("TotalSpent"),
        count("OrderID").alias("TotalOrders"),
        countDistinct("ProductID").alias("UniqueProducts"),
        avg("CustomerRating").alias("AvgRating"),
        min("OrderDate").alias("FirstOrderDate"),
        max("OrderDate").alias("LastOrderDate")
    )

# Calculate customer tenure
customer_clv = customer_clv.withColumn("CustomerTenureDays",
    datediff(col("LastOrderDate"), col("FirstOrderDate")) + 1)

# Top customers by total spent
print("Top 10 Customers by Total Spent:")
customer_clv.orderBy(desc("TotalSpent")).show(10)

# 2. Shipping Performance Analysis
print("\n2. SHIPPING PERFORMANCE ANALYSIS")
print("-" * 30)

shipping_performance = df_clean.filter(col("DeliveryDays").isNotNull()) \
    .groupBy("ShippingStatus", "Country") \
    .agg(
        avg("DeliveryDays").alias("AvgDeliveryDays"),
        count("OrderID").alias("TotalOrders"),
        min("DeliveryDays").alias("MinDeliveryDays"),
        max("DeliveryDays").alias("MaxDeliveryDays")
    ).orderBy("Country", "ShippingStatus")

print("Shipping Performance by Country and Status:")
shipping_performance.show()

# 3. Promotion Effectiveness Analysis
print("\n3. PROMOTION EFFECTIVENESS ANALYSIS")
print("-" * 30)

promotion_analysis = df_clean.groupBy("PromotionApplied") \
    .agg(
        count("OrderID").alias("TotalOrders"),
        sum("TotalAmount").alias("TotalRevenue"),
        avg("TotalAmount").alias("AvgOrderValue"),
        avg("CustomerRating").alias("AvgRating")
    )

print("Promotion vs Non-Promotion Orders:")
promotion_analysis.show()

# Discount code effectiveness
discount_analysis = df_clean.filter(col("DiscountCode").isNotNull()) \
    .groupBy("DiscountCode") \
    .agg(
        count("OrderID").alias("TimesUsed"),
        sum("TotalAmount").alias("TotalRevenue"),
        avg("TotalAmount").alias("AvgOrderValue"),
        countDistinct("CustomerID").alias("UniqueCustomers")
    ).orderBy(desc("TimesUsed"))

print("Discount Code Usage:")
discount_analysis.show()

# ================================================================
# 7. WINDOW FUNCTIONS AND RANKING
# ================================================================

print("\n" + "="*50)
print("WINDOW FUNCTIONS AND RANKING")
print("="*50)

from pyspark.sql.window import Window

# 1. Customer ranking by total spent
customer_window = Window.orderBy(desc("TotalSpent"))

customer_ranking = customer_clv.withColumn("CustomerRank", 
    rank().over(customer_window))

print("Top 10 Customers with Rankings:")
customer_ranking.select("CustomerID", "TotalSpent", "TotalOrders", "CustomerRank") \
    .show(10)

# 2. Product ranking within each category (assuming ProductID prefix indicates category)
df_clean = df_clean.withColumn("ProductCategory", 
    substring(col("ProductID"), 1, 4))  # Extract first 4 chars as category

product_window = Window.partitionBy("ProductCategory").orderBy(desc("TotalAmount"))

product_ranking = df_clean.groupBy("ProductCategory", "ProductID", "ProductName") \
    .agg(sum("TotalAmount").alias("TotalRevenue")) \
    .withColumn("CategoryRank", rank().over(product_window))

print("Product Rankings within Categories:")
product_ranking.filter(col("CategoryRank") <= 3).show()

# 3. Running total of sales by date
daily_sales = df_clean.groupBy("OrderDate") \
    .agg(sum("TotalAmount").alias("DailySales")) \
    .orderBy("OrderDate")

date_window = Window.orderBy("OrderDate")

daily_running_total = daily_sales.withColumn("RunningTotal",
    sum("DailySales").over(date_window))

print("Daily Sales with Running Total:")
daily_running_total.show()

# ================================================================
# 8. DATA QUALITY MONITORING
# ================================================================

print("\n" + "="*50)
print("DATA QUALITY MONITORING")
print("="*50)

# Create data quality metrics
def calculate_data_quality_metrics(df):
    total_records = df.count()
    
    quality_metrics = []
    
    for column in df.columns:
        null_count = df.filter(col(column).isNull()).count()
        null_percentage = (null_count / total_records) * 100
        
        quality_metrics.append({
            'Column': column,
            'NullCount': null_count,
            'NullPercentage': round(null_percentage, 2),
            'CompletionRate': round(100 - null_percentage, 2)
        })
    
    return quality_metrics

quality_metrics = calculate_data_quality_metrics(df_clean)

print("Data Quality Metrics:")
for metric in quality_metrics:
    print(f"{metric['Column']}: {metric['CompletionRate']}% complete, {metric['NullCount']} nulls")

# ================================================================
# 9. EXPORT AND SAVE RESULTS
# ================================================================

print("\n" + "="*50)
print("SAVING RESULTS")
print("="*50)

# Cache frequently used dataframes for better performance
df_clean.cache()
customer_clv.cache()

# Save cleaned data
print("Saving cleaned data...")
df_clean.write.mode("overwrite").parquet("cleaned_ecommerce_data.parquet")

# Save analysis results
print("Saving analysis results...")
monthly_sales.write.mode("overwrite").csv("monthly_sales_analysis.csv", header=True)
customer_clv.write.mode("overwrite").csv("customer_lifetime_value.csv", header=True)
product_performance.write.mode("overwrite").csv("product_performance.csv", header=True)

print("All results saved successfully!")

# ================================================================
# 10. PRACTICE EXERCISES
# ================================================================

print("\n" + "="*50)
print("PRACTICE EXERCISES FOR YOU TO TRY")
print("="*50)

exercises = [
    "1. Find the top 5 customers who made the most orders in each country",
    "2. Calculate the month-over-month growth rate for total sales",
    "3. Identify products that are frequently bought together (market basket analysis)",
    "4. Find customers who haven't made a purchase in the last 30 days",
    "5. Calculate the return rate by product category",
    "6. Analyze seasonal trends in product sales",
    "7. Find the correlation between customer rating and order value",
    "8. Identify the most profitable shipping method",
    "9. Calculate customer acquisition cost by marketing channel (if available)",
    "10. Create a customer segmentation based on RFM analysis (Recency, Frequency, Monetary)"
]

for exercise in exercises:
    print(exercise)

print("\n" + "="*50)
print("ADDITIONAL PYSPARK CONCEPTS TO PRACTICE")
print("="*50)

concepts = [
    "• UDFs (User Defined Functions)",
    "• Broadcast variables and accumulators",
    "• Partitioning and bucketing",
    "• Joining large datasets efficiently",
    "• Handling skewed data",
    "• Using SQL with DataFrames",
    "• Working with nested data structures",
    "• Stream processing with structured streaming",
    "• Machine learning with MLlib",
    "• Graph processing with GraphFrames"
]

for concept in concepts:
    print(concept)

# Stop Spark session
spark.stop()
print("\nSpark session stopped. Practice completed!")