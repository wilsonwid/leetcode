# Write your MySQL query statement below
WITH cte AS (SELECT e.employee_id, name, salary FROM Employees AS e
LEFT JOIN Salaries s ON e.employee_id = s.employee_id
UNION
SELECT s.employee_id, name, salary FROM Employees AS e
RIGHT JOIN Salaries s ON e.employee_id = s.employee_id
)
SELECT employee_id FROM cte
WHERE name IS NULL OR salary IS NULL
ORDER BY employee_id
