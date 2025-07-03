-- Active: 1751469617468@@127.0.0.1@5432@New_Data
--6. Customer Order Count
-- → Count how many orders each customer has placed.
SELECT
    customer_id,
    count(*) AS total_order
FROM
    orders
GROUP BY
    customer_id
ORDER BY
    customer_id;

-- 7-Total Revenue per Country
--→ Show total order value (total_amount) for each country
SELECT
    country,
    sum(orders.total_amount) AS total_revenu
FROM
    customers
    JOIN orders ON customers.customer_id = orders.customer_id
GROUP BY
    customers.country
ORDER BY
    total_revenu;

--8. Top 3 Product Categories by Revenue
--→ List the top 3 product_category by sum of total_amount
SELECT
    product_category,
    sum(total_amount) AS revenu
FROM
    orders
GROUP BY
    product_category
ORDER BY
    revenu DESC
LIMIT
    (3);

--9. Avg. Order Value per Customer
-- → For each customer, calculate average order value
SELECT
    concat (first_name, ' ', last_name) AS name,
    avg(orders.total_amount) AS avg_order
FROM
    customers
    JOIN orders ON customers.customer_id = orders.customer_id
GROUP BY
    customers.customer_id
ORDER BY avg_order;


--10. High Revenue Countries Only
--→ Show countries where total revenue > ₹500
SELECT customers.country,sum(orders.total_amount) AS revenue
FROM customers
JOIN orders
ON customers.customer_id=orders.customer_id
GROUP BY customers.country
HAVING sum(orders.total_amount) > 500.00;
