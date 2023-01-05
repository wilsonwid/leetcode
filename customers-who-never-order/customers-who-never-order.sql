# Write your MySQL query statement below
SELECT c.name AS Customers
FROM Customers AS c
LEFT JOIN Orders AS o ON c.id = o.customerId
WHERE customerId IS NULL
