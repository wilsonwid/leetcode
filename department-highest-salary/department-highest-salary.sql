# Write your MySQL query statement below
SELECT D.name AS Department, E.name AS Employee, E.salary AS Salary
FROM Department D
JOIN Employee E ON D.id = E.departmentId
WHERE E.salary = (
    SELECT MAX(E1.salary)
    FROM Employee E1
    WHERE E.departmentId = E1.departmentId
)
