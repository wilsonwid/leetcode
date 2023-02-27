# Write your MySQL query statement below
WITH cte AS (
    SELECT u.users_id
    FROM Users u
    WHERE u.banned = 'No'
), cte2 AS (
    SELECT t.id, t.request_at
    FROM Trips t
    WHERE t.client_id IN (SELECT * FROM cte WHERE t.client_id = cte.users_id)
        AND t.driver_id IN (SELECT * FROM cte WHERE t.driver_id = cte.users_id)
        AND (t.status = 'cancelled_by_driver' OR t.status = 'cancelled_by_client')
        AND '2013-10-01' <= t.request_at AND t.request_at <= '2013-10-03'
), cte3 AS (
    SELECT DISTINCT t.request_at
    FROM Trips t
)
SELECT cte3.request_at AS Day, ROUND(COUNT(cte2.id)/COUNT(t.id), 2) AS 'Cancellation Rate'
FROM cte3
LEFT JOIN Trips t ON cte3.request_at = t.request_at
LEFT JOIN cte2 ON t.id = cte2.id
WHERE t.client_id IN (SELECT * FROM cte)
    AND t.driver_id IN (SELECT * FROM cte)
    AND '2013-10-01' <= cte3.request_at AND cte3.request_at <= '2013-10-03'

GROUP BY cte3.request_at
