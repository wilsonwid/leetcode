WITH cte AS (
SELECT customer_number, COUNT(1) AS c
FROM Orders
GROUP BY customer_number
ORDER BY c DESC
)
SELECT customer_number
FROM cte
LIMIT 1
