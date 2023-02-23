# Write your MySQL query statement below
WITH cte AS (
    SELECT s.id - 1 AS id, s.student
    FROM Seat s
    WHERE s.id > 1
), cte2 AS (
    SELECT s.id + 1 AS id, s.student
    FROM Seat s
)
SELECT s.id, 
    CASE
        WHEN s.id % 2 = 1 AND cte.student IS NOT NULL THEN cte.student
        WHEN s.id % 2 = 0 AND cte2.student IS NOT NULL THEN cte2.student
        ELSE s.student
    END AS student
FROM Seat s LEFT JOIN cte ON s.id = cte.id 
LEFT JOIN cte2 ON s.id = cte2.id
ORDER BY s.id ASC
