-- Active: 1751469617468@@127.0.0.1@5432@New_Data
SELECT
    *
FROM
    customers;

SELECT
    *
FROM
    orders;

SELECT
    *
FROM
    order_items;

--16. Most Recent Order per Customer
-- → Show each customer’s most recent order (using CTE or window).
WITH c1 AS(
SELECT
    c.customer_id,
        concat (c.first_name, ' ', c.last_name) AS customer_name,
        o.order_id,   
        o.order_date,
        ROW_NUMBER() OVER(PARTITION BY c.customer_id ORDER BY o.order_id desc) as rn
FROM
    customers c
    JOIN orders o ON c.customer_id = o.customer_id
    )
SELECT customer_name, order_id,order_date
from c1
WHERE rn=1;

--17. Average Quantity Ordered per Product
-- → Use subquery to calculate avg. quantity of each product
SELECT oi.product_name,avg(oi.quantity) AS avg_quantity
FROM order_items oi
GROUP BY oi.product_name
ORDER BY avg_quantity;

--18. Top Product per Category
--→ Use ROW_NUMBER() or RANK() to get highest-selling product per category
WITH t1 AS(
SELECT 
o.product_category,
oi.product_name,
sum(oi.quantity) AS total_quantity_sold,
ROW_NUMBER() 
OVER(PARTITION BY o.product_category ORDER BY sum(oi.quantity) DESC) as rn
FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY oi.product_name,o.product_category)
SELECT product_category, product_name,total_quantity_sold
FROM t1
WHERE rn=1;


--19. Running Total of Orders by Date
-- → Compute cumulative revenue (running sum) by order date


