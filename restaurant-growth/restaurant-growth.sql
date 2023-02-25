# Write your MySQL query statement below
WITH cte AS (
    SELECT DISTINCT c.visited_on FROM Customer c
    WHERE DATE_SUB(c.visited_on, INTERVAL 6 DAY) IN (
        SELECT c1.visited_on FROM Customer c1
    )
)
SELECT cte.visited_on, SUM(c.amount) AS amount, ROUND(SUM(c.amount)/7, 2) AS average_amount
FROM cte
LEFT JOIN Customer c ON 
    DATEDIFF(cte.visited_on, c.visited_on) >= 0 AND 
    DATEDIFF(cte.visited_on, c.visited_on) <= 6
GROUP BY cte.visited_on
ORDER BY cte.visited_on ASC
