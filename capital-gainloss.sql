WITH cte1 AS (
    SELECT stock_name, SUM(price) AS sum_price
    FROM Stocks
    WHERE operation = 'Buy'
    GROUP BY stock_name
), cte2 AS (
    SELECT stock_name, SUM(price) AS sum_price
    FROM Stocks
    WHERE operation = 'Sell'
    GROUP BY stock_name
)
SELECT cte1.stock_name, (cte2.sum_price - cte1.sum_price) AS capital_gain_loss
FROM cte1
LEFT JOIN cte2 ON cte1.stock_name = cte2.stock_name
