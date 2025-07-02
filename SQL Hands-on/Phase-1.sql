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
