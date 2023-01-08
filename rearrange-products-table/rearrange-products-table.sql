# Write your MySQL query statement below
WITH cte AS (
SELECT product_id, 'store1' AS store, store1 AS price
FROM Products
UNION
SELECT product_id, 'store2' AS store, store2 AS price
FROM Products
UNION
SELECT product_id, 'store3' AS store, store3 AS price
FROM Products)
SELECT product_id, store, price
FROM cte
WHERE price IS NOT NULL
