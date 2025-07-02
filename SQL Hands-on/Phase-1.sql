-- Active: 1751469617468@@127.0.0.1@5432@New_Data
-- 1. Get All Customers
SELECT
    *
FROM
    customers;

-- → List all columns of all customers from USA.
SELECT
    first_name,
    last_name,
    country
FROM
    customers
WHERE
    country = 'USA';

--2. Recently Registered Customers
-- → Show top 5 most recently registered customers.
SELECT
    concat (first_name, ' ', last_name),
    email,
    registration_date,
    city,
    country
FROM customers
ORDER BY registration_date DESC
LIMIT 5;


-- 3. Unique Countries
-- → List all unique countries from the customers table
SELECT DISTINCT country,first_name,last_name
FROM customers;


--4. High Order Amounts
SELECT *
FROM orders;

-- → Fetch all orders where total_amount > 400
SELECT * 
FROM orders
WHERE total_amount > 400


-- 5. Products by Category
-- → List all orders in the “Electronics” product category
SELECT * 
FROM orders
WHERE product_category='Electronics';