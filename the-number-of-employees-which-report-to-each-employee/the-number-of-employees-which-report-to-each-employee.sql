SELECT e.employee_id, e.name, COUNT(*) AS reports_count, ROUND(AVG(e1.age), 0) AS average_age
FROM Employees e
LEFT JOIN Employees e1 ON e.employee_id = e1.reports_to
GROUP BY e.employee_id, e.name
HAVING AVG(e1.age) IS NOT NULL
ORDER BY e.employee_id
