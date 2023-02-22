/* Write your T-SQL query statement below */
WITH cte AS (
    SELECT year, comp, winner
    FROM (
        SELECT year, Wimbledon, Fr_open, US_open, Au_open
        FROM Championships
    ) p
    UNPIVOT (
        winner FOR comp IN (
            Wimbledon, Fr_open, US_open, Au_open
        )
    ) AS unpvt
)
SELECT cte.winner AS player_id, p.player_name AS player_name, COUNT(*) AS grand_slams_count
FROM cte INNER JOIN Players p ON cte.winner = p.player_id
GROUP BY cte.winner, p.player_name
