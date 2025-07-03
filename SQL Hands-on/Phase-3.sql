-- Active: 1751469617468@@127.0.0.1@5432@New_Data
SELECT * FROM customers;

SELECT * FROM orders;

SELECT * FROM order_items;

--11. Customer Order Details
-- → List each order with customer’s name, email, and city.
SELECT
    product_name AS order_item_name,
    customers.city,
    customers.email,
    concat (first_name, ' ', last_name) AS customer_name
FROM
    order_items
    JOIN orders ON order_items.order_id = orders.order_id
    JOIN customers ON customers.customer_id = orders.customer_id;

--