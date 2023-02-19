WITH cte1 AS (
    SELECT C.customer_id FROM Customers C, Orders O
    WHERE C.customer_id = O.customer_id AND O.product_name = 'A'
), cte2 AS (
    SELECT C.customer_id FROM Customers C, Orders O
    WHERE C.customer_id = O.customer_id AND O.product_name = 'B'
), cte3 AS (
    SELECT C.customer_id FROM Customers C, Orders O
    WHERE C.customer_id = O.customer_id AND O.product_name = 'C'
)

SELECT C.customer_id AS customer_id, C.customer_name AS customer_name
FROM Customers C
WHERE C.customer_id IN (SELECT * FROM cte1) AND C.customer_id IN (SELECT * FROM cte2) AND C.customer_id NOT IN (SELECT * FROM cte3)
