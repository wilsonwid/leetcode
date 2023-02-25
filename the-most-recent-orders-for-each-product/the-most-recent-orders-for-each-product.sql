# Write your MySQL query statement below
WITH cte AS (
    SELECT o.product_id, MAX(o.order_date) AS order_date
    FROM Orders o
    GROUP BY o.product_id
)
SELECT p.product_name, cte.product_id, o.order_id, cte.order_date
FROM Products p
JOIN cte ON p.product_id = cte.product_id
JOIN Orders o ON p.product_id = o.product_id AND cte.order_date = o.order_date
ORDER BY p.product_name ASC, cte.product_id ASC, o.order_id ASC
