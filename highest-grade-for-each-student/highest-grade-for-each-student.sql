SELECT E1.student_id AS student_id, MIN(E1.course_id) AS course_id, E1.grade AS grade
FROM Enrollments E1
WHERE (E1.student_id, E1.grade) IN (
    SELECT E2.student_id, MAX(E2.grade)
    FROM Enrollments E2
    GROUP BY E2.student_id
)
GROUP BY E1.student_id
ORDER BY student_id ASC
