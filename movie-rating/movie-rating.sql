# Write your MySQL query statement below
WITH cte AS (
SELECT u.name AS results FROM MovieRating m JOIN Users u ON m.user_id = u.user_id
GROUP BY m.user_id
ORDER BY COUNT(*) DESC, u.name ASC
LIMIT 1
), cte2 AS (
SELECT mo.title AS results
FROM MovieRating m JOIN Movies mo ON m.movie_id = mo.movie_id
WHERE '2020-02-01' <= m.created_at AND m.created_at < '2020-03-01'
GROUP BY m.movie_id
ORDER BY AVG(rating) DESC, mo.title
LIMIT 1
)
SELECT * FROM cte
UNION
SELECT * FROM cte2
