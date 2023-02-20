# Write your MySQL query statement below
SELECT E.left_operand AS left_operand, E.operator AS operator,
    E.right_operand AS right_operand,
    CASE
        WHEN E.operator = '>' THEN IF(V1.value > V2.value, 'true', 'false')
        WHEN E.operator = '=' THEN IF(V1.value = V2.value, 'true', 'false')
        ELSE IF(V1.value < V2.value, 'true', 'false')
    END AS value
FROM Expressions E
LEFT JOIN Variables V1 ON E.left_operand = V1.name
LEFT JOIN Variables V2 ON E.right_operand = V2.name
