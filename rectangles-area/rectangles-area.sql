# Write your MySQL query statement below
WITH cte AS (
SELECT p1.id AS P1, p2.id AS P2, 
    ABS(p1.x_value - p2.x_value) * ABS(p1.y_value - p2.y_value) AS AREA
FROM Points p1, Points p2
WHERE p1.x_value <> p2.x_value AND p1.y_value <> p2.y_value AND 
    ABS(p1.x_value - p2.x_value) * ABS(p1.y_value - p2.y_value) > 0
    AND p1.id < p2.id
ORDER BY area DESC, p1 ASC, p2 ASC
)
SELECT * FROM cte

