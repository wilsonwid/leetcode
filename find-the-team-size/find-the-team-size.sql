# Write your MySQL query statement below
WITH cte AS (
    SELECT E.team_id, COUNT(*) AS team_size FROM Employee E
    GROUP BY E.team_id
)
SELECT E1.employee_id, cte.team_size
FROM Employee E1, cte
WHERE E1.team_id = cte.team_id
