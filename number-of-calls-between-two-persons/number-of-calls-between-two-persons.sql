WITH cte1 AS (
    SELECT from_id, to_id, duration
    FROM Calls
    WHERE from_id < to_id
), cte2 AS (
    SELECT to_id, from_id, duration
    FROM Calls
    WHERE to_id < from_id
), cte3 AS (
    SELECT from_id AS person1, to_id AS person2, duration
    FROM cte1
    UNION ALL
    SELECT to_id AS person1, from_id AS person2, duration
    FROM cte2
)
SELECT person1, person2, COUNT(1) AS call_count, SUM(duration) AS total_duration
FROM cte3
GROUP By person1, person2
