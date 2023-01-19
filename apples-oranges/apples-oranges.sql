WITH cte1 AS (
    SELECT sale_date, sold_num
    FROM Sales
    WHERE fruit = "apples"
), cte2 AS (
    SELECT sale_date, sold_num
    FROM Sales
    WHERE fruit = "oranges"
)
SELECT cte1.sale_date, (cte1.sold_num - cte2.sold_num) AS diff
FROM cte1
LEFT JOIN cte2 ON cte1.sale_date = cte2.sale_date
GROUP BY cte1.sale_date
