WITH cte1 AS (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
    ORDER BY num DESC
    LIMIT 1
)
SELECT CASE 
    WHEN COUNT(cte1.num) = 0 THEN NULL
    ELSE cte1.num
    END AS num
FROM cte1
