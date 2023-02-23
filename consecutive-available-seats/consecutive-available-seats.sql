/* Write your T-SQL query statement below */
SELECT DISTINCT c.seat_id
FROM Cinema c
WHERE EXISTS (
    SELECT c1.seat_id
    FROM Cinema c1
    WHERE (c.seat_id = c1.seat_id - 1 OR  c1.seat_id = c.seat_id - 1) AND c.free = 1 AND c1.free = 1
)
