-- Active: 1751469617468@@127.0.0.1@5432@New_Data

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

--12. Order with Items
--→ Show each order_id with corresponding product_name and quantity
SELECT
    order_id,
    product_name,
    quantity
FROM
    order_items;

--13. Customer with No Orders
-- → List customers who haven't placed any orders
SELECT
    customer_id,
    concat (first_name, ' ', last_name) AS customer_name
FROM
    customers
WHERE
    customer_id NOT IN (
        SELECT
            customer_id
        FROM
            orders
    );

--14. Orders with No Items
-- → List orders that don't have any items linked.
SELECT
    os.order_id
FROM
    orders os
    LEFT JOIN order_items oi ON os.order_id = oi.order_id
WHERE
    oi.item_id IS NULL;

--15. Top Spend by Customer
-- → Show top 5 customers based on total spend (unit_price * quantity)
SELECT
    concat (first_name, ' ', last_name) AS customer_name,
    SUM(quantity * unit_price) AS total_spend
FROM
    customers c
    JOIN orders os ON c.customer_id = os.customer_id
    JOIN order_items oi ON os.order_id = oi.order_id
GROUP BY
    c.customer_id
ORDER BY
    total_spend DESC
LIMIT(5);