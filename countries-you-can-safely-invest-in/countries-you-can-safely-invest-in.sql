# Write your MySQL query statement below
WITH cte AS (
    SELECT C.name, AVG(CL.duration) AS avg_duration
    FROM Country C
    JOIN Person P ON C.country_code = SUBSTRING(P.phone_number, 1, 3)
    JOIN Calls CL ON CL.caller_id = P.id OR CL.callee_id = P.id
    GROUP BY C.name
)
SELECT cte.name AS country FROM cte
WHERE cte.avg_duration > (SELECT AVG(CL.duration) FROM Calls CL)
