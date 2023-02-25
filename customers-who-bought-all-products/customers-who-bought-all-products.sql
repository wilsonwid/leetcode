# Write your MySQL query statement below
WITH cte AS (
    SELECT COUNT(DISTINCT product_key)
    FROM Product
)
SELECT DISTINCT c.customer_id
FROM Customer c
GROUP BY c.customer_id
HAVING COUNT(DISTINCT c.product_key) = (SELECT * FROM cte)
