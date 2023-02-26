# Write your MySQL query statement below
SELECT DISTINCT o.order_id
FROM OrdersDetails o
GROUP BY o.order_id
HAVING MAX(o.quantity) > ALL(
    SELECT AVG(o1.quantity)
    FROM OrdersDetails o1
    GROUP BY o1.order_id
)
