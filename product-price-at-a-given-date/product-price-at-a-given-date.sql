/* Write your T-SQL query statement below */
WITH cte AS (
    SELECT product_id, MAX(change_date) AS change_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
), cte2 AS (
    SELECT p.product_id, 
        CASE
            WHEN p.new_price IS NULL THEN 10
            ELSE p.new_price
        END AS price
    FROM Products p
    RIGHT JOIN cte ON p.product_id = cte.product_id AND p.change_date = cte.change_date
)
SELECT * FROM cte2
UNION
SELECT product_id, 10 FROM Products WHERE product_id NOT IN (SELECT product_id FROM cte2)
