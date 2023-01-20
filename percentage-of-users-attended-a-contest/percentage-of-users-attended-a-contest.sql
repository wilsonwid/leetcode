WITH ct AS (
    SELECT COUNT(1) num FROM Users
)
SELECT contest_id, ROUND(COUNT(DISTINCT user_id) * 100 / (SELECT num FROM ct), 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC
