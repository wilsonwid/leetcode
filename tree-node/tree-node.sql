# Write your MySQL query statement below
WITH cte AS (
    SELECT Tree.id AS p_id, t1.id FROM Tree AS t1
    RIGHT JOIN Tree ON t1.p_id = Tree.id
),
cte2 AS (SELECT cte.p_id, GROUP_CONCAT(cte.id) AS children, Tree.p_id AS parent FROM cte
LEFT JOIN Tree ON cte.p_id = Tree.id
GROUP BY cte.p_id)
SELECT cte2.p_id AS id, CASE WHEN 
    cte2.children IS NOT NULL AND cte2.parent IS NOT NULL THEN 'Inner'
    WHEN cte2.parent IS NULL THEN 'Root'
    ELSE 'Leaf'
END AS type
FROM cte2
