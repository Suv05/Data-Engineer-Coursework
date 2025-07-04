-- Active: 1751469617468@@127.0.0.1@5432@New_Data
-- Data Manipulation (INSERT, UPDATE, DELETE)

--21. Insert New Customer & Order
--→ Add a new customer and place an order for them
INSERT INTO customers (first_name, last_name, email, registration_date, city, country)
VALUES (
    'Ankita',
    'Smith',
    'ankita.smith@example.com',
    '2024-11-15',
    'Mumbai',
    'India'
);
INSERT INTO orders (customer_id, order_date, total_amount, status, product_category)
VALUES (
    250,
    '2024-11-15 10:00:00',
    450.75,
    'Completed',
    'Electronics'
);

--22. Update Order Status
-- → Mark all orders older than 6 months from latest order date as 'Archived'
UPDATE orders
SET status='Archived'
WHERE order_date < ( --'<' for "older than"
    -- to get the lateast date of order
    WITH t1 AS(
    SELECT order_date
    FROM orders
    ORDER BY order_date DESC
    LIMIT(1))
    -- then -6 months from latest date of order
    SELECT order_date::date - INTERVAL '6 months' as subtract_days 
    FROM t1
);

--23. Delete Orphan Orders
-- → Delete orders that have no matching customer
DELETE FROM orders
WHERE orders.order_id IN(
SELECT o.order_id
FROM orders o
LEFT JOIN customers c
ON c.customer_id=o.customer_id
WHERE c.first_name IS NULL);