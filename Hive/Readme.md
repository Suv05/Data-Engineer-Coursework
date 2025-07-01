# Hive Command Cheat Sheet

This README provides a comprehensive guide to essential Hive commands, categorized into Data Definition Language (DDL), Data Manipulation Language (DML), and other useful commands. Each command is accompanied by a brief explanation.

## Table of Contents

1.  [Data Definition Language (DDL) Commands](#data-definition-language-ddl-commands)
2.  [Data Manipulation Language (DML) Commands](#data-manipulation-language-dml-commands)
3.  [Other Useful Commands](#other-useful-commands)

---

## 1. Data Definition Language (DDL) Commands

DDL commands are used to define, modify, and manage the structure of databases and tables in Hive.

* **`CREATE DATABASE database_name;`**
    * *Explanation:* Creates a new database with the specified name in Hive.
    * *Example:*
        ```sql
        CREATE DATABASE my_new_db;
        ```

* **`DROP DATABASE database_name;`**
    * *Explanation:* Deletes an existing database. By default, it will only delete an empty database. Use `DROP DATABASE database_name CASCADE;` to delete a database and all its tables, even if it's not empty.
    * *Example:*
        ```sql
        DROP DATABASE my_old_db;
        ```

* **`SHOW DATABASES;`**
    * *Explanation:* Lists all databases available in Hive.
    * *Example:*
        ```sql
        SHOW DATABASES;
        ```

* **`USE database_name;`**
    * *Explanation:* Selects a database to be the current database for subsequent operations. You don't need to specify the database name for tables within this selected database.
    * *Example:*
        ```sql
        USE my_new_db;
        ```

* **`CREATE TABLE table_name (column_name data_type, ...);`**
    * *Explanation:* Creates a new table with the specified name and defines its columns along with their data types.
    * *Example:*
        ```sql
        CREATE TABLE employees (
            id INT,
            name STRING,
            age INT,
            salary DOUBLE
        );
        ```

* **`DROP TABLE table_name;`**
    * *Explanation:* Deletes an existing table from the current database.
    * *Example:*
        ```sql
        DROP TABLE employees;
        ```

* **`ALTER TABLE table_name ...;`**
    * *Explanation:* Used to modify the structure of an existing table. This can include adding, dropping, or renaming columns, changing table properties, etc.
    * *Examples:*
        ```sql
        ALTER TABLE employees ADD COLUMNS (department STRING);
        ALTER TABLE employees RENAME TO staff;
        ```

* **`DESCRIBE table_name;`**
    * *Explanation:* Displays the schema (structure) of a table, including column names, data types, and comments.
    * *Example:*
        ```sql
        DESCRIBE employees;
        ```

* **`SHOW TABLES;`**
    * *Explanation:* Lists all tables present in the currently selected database.
    * *Example:*
        ```sql
        SHOW TABLES;
        ```

* **`SHOW CREATE TABLE table_name;`**
    * *Explanation:* Displays the exact `CREATE TABLE` statement that was used to create the specified table, including all its properties and definitions.
    * *Example:*
        ```sql
        SHOW CREATE TABLE employees;
        ```

---

## 2. Data Manipulation Language (DML) Commands

DML commands are used for managing data within schema objects.

* **`LOAD DATA [LOCAL] INPATH 'filepath' INTO TABLE table_name;`**
    * *Explanation:* Loads data from a file into a Hive table. `LOCAL` specifies that the file is on the local filesystem of the machine running the Hive client; otherwise, it assumes the file is in HDFS.
    * *Example:*
        ```sql
        LOAD DATA LOCAL INPATH '/home/user/data.csv' INTO TABLE employees;
        LOAD DATA INPATH '/user/hive/warehouse/data.txt' INTO TABLE employees;
        ```

* **`INSERT INTO TABLE table_name SELECT ...;`**
    * *Explanation:* Inserts data into a table by selecting data from another table or a query result.
    * *Example:*
        ```sql
        INSERT INTO TABLE new_employees SELECT id, name FROM employees WHERE age > 30;
        ```

* **`SELECT column_names FROM table_name WHERE conditions;`**
    * *Explanation:* Retrieves data from one or more tables based on specified conditions. This is the most frequently used DML command for querying data.
    * *Examples:*
        ```sql
        SELECT * FROM employees;
        SELECT name, salary FROM employees WHERE department = 'Sales';
        ```

* **`UPDATE table_name SET column1 = value1 WHERE condition;`**
    * *Explanation:* Modifies existing records in a table that meet a specified condition. **Note:** This command requires Hive 0.14 or later and specific configurations (e.g., ACID properties enabled for the table).
    * *Example:*
        ```sql
        UPDATE employees SET salary = 60000 WHERE id = 101;
        ```

* **`DELETE FROM table_name WHERE condition;`**
    * *Explanation:* Deletes records from a table that meet a specified condition. **Note:** This command also requires Hive 0.14 or later and specific configurations (e.g., ACID properties enabled for the table).
    * *Example:*
        ```sql
        DELETE FROM employees WHERE age < 25;
        ```

* **`TRUNCATE TABLE table_name;`**
    * *Explanation:* Removes all rows from a table, effectively emptying it. This operation is generally faster than `DELETE` without a `WHERE` clause as it doesn't process rows individually.
    * *Example:*
        ```sql
        TRUNCATE TABLE staging_data;
        ```

---

## 3. Other Useful Commands

These commands provide additional functionalities for query optimization, user-defined functions, and interacting with the underlying filesystem.

* **`EXPLAIN query;`**
    * *Explanation:* Displays the execution plan for a given HiveQL query. This is invaluable for understanding how Hive will process a query and for performance tuning.
    * *Example:*
        ```sql
        EXPLAIN SELECT name, salary FROM employees WHERE department = 'IT';
        ```

* **`ANALYZE TABLE table_name COMPUTE STATISTICS;`**
    * *Explanation:* Computes statistics (e.g., number of rows, column min/max values) for a table. These statistics are used by Hive's query optimizer to create more efficient execution plans, thus improving query performance.
    * *Example:*
        ```sql
        ANALYZE TABLE employees COMPUTE STATISTICS FOR COLUMNS name, age;
        ```

* **`CREATE VIEW view_name AS SELECT ...;`**
    * *Explanation:* Creates a virtual table (view) based on the result set of a `SELECT` query. Views do not store data themselves but provide a simplified way to query complex underlying tables.
    * *Example:*
        ```sql
        CREATE VIEW high_earners AS
        SELECT name, salary
        FROM employees
        WHERE salary > 70000;
        ```

* **`CREATE FUNCTION function_name AS class_name USING archive_name;`**
    * *Explanation:* Creates a user-defined function (UDF) in Hive. UDFs allow users to extend Hive's functionality by writing custom code (e.g., in Java) to process data.
    * *Example:*
        ```sql
        CREATE FUNCTION my_udf AS 'com.example.MyUDF' USING JAR 'hdfs:///user/hive/udf/myudf.jar';
        ```

* **`!command;`**
    * *Explanation:* Executes a shell command directly from the Hive shell. The `!` prefix tells Hive to pass the command to the underlying operating system.
    * *Example:*
        ```sql
        !ls -l /tmp;
        ```

* **`dfs command;`**
    * *Explanation:* Executes a Hadoop Distributed File System (HDFS) command directly from the Hive shell. This is a shorthand for `hadoop fs` or `hdfs dfs` commands.
    * *Example:*
        ```sql
        dfs -ls /user/hive/warehouse;
        ```
