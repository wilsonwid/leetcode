# Write your MySQL query statement below
WITH cte AS (
    SELECT E.managerId FROM Employee E
    GROUP BY managerId
    HAVING COUNT(*) >= 5
)
SELECT E1.name FROM Employee E1
WHERE E1.id IN (SELECT * FROM cte)
