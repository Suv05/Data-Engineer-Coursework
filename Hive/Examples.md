# HiveQL Examples

This document provides practical examples of common HiveQL (Hive Query Language) commands for database and table operations, data loading, and querying.

---

## 1. Create a database

This command creates a new database. The `IF NOT EXISTS` clause prevents an error if the database already exists.

```sql
CREATE DATABASE IF NOT EXISTS my_database;

```

## 2. Use the database
This command sets `my_database` as the current database, so subsequent table operations will apply to it without needing to specify the database name.

```sql
USE my_database;
```
---

## 3. Create a table
This example creates a table named `employees` with three columns: `id` (integer), `name` (string), and `salary` (double). It also specifies the row and field delimiters for text files and declares that the data will be stored as a plain text file.

```sql
CREATE TABLE IF NOT EXISTS employees (
    id INT,
    name STRING,
    salary DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

```

---

## 4. Load data into the table
This command loads data from a local CSV file (e.g., `employees.csv` on your machine) into the `employees` table. Replace `/path/to/employees.csv` with the actual path to your file.

```sql
LOAD DATA LOCAL INPATH '/path/to/employees.csv' INTO TABLE employees;

```

---

## 5. Select data from the table
This query retrieves all columns (`*`) from the `employees` table where the `salary` is greater than 50000.

```sql
SELECT * FROM employees WHERE salary > 50000;

```

---

## 6. Describe the table
This command displays the schema of the `employees` table, showing the column names, their data types, and any comments.

```sql
DESCRIBE employees;

```

