# Write your MySQL query statement below
SELECT D.dept_name, COUNT(S.student_id) AS student_number
FROM Department D
LEFT JOIN Student S ON D.dept_id = S.dept_id
GROUP BY D.dept_name
ORDER BY student_number DESC, dept_name ASC
