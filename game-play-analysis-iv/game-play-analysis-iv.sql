WITH cte1 AS (
    SELECT a.player_id, MIN(a.event_date) AS event_date
    FROM Activity a
    GROUP BY a.player_id
), cte2 AS (
    SELECT COUNT(DISTINCT a1.player_id) AS counts
    FROM Activity a1
    WHERE EXISTS (
        SELECT 1
        FROM Activity a2
        WHERE DATEDIFF(a1.event_date, a2.event_date) = 1
            AND a1.player_id = a2.player_id
            AND a2.event_date IN (
                SELECT cte1.event_date 
                FROM cte1 WHERE cte1.player_id = a1.player_id
            )
    )
)
SELECT ROUND(cte2.counts/COUNT(DISTINCT a.player_id), 2) AS fraction
FROM cte2, Activity a
