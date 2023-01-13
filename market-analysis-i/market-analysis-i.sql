WITH cte AS (
    SELECT buyer_id, order_date
    FROM Orders
    WHERE YEAR(order_date) = 2019
)
SELECT u.user_id AS buyer_id, 
    u.join_date AS join_date, COUNT(order_date) AS orders_in_2019
FROM Users u
LEFT JOIN cte ON u.user_id = cte.buyer_id
GROUP BY u.user_id
