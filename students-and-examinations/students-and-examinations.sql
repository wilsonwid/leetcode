# Write your MySQL query statement below
WITH cte AS (
    SELECT S.student_id, S.student_name, S2.subject_name
    FROM Students S, Subjects S2
)
SELECT cte.student_id, cte.student_name, cte.subject_name, COUNT(E.subject_name) AS attended_exams
FROM cte
LEFT JOIN Examinations E ON cte.student_id = E.student_id AND cte.subject_name = E.subject_name
GROUP BY cte.student_id, cte.student_name, cte.subject_name
ORDER BY student_id, subject_name
