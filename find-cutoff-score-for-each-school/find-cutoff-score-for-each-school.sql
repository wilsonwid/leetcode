# Write your MySQL query statement below
SELECT s.school_id, COALESCE(MIN(e.score), -1) AS score
FROM Schools s
LEFT JOIN Exam e ON s.capacity >= e.student_count
GROUP BY s.school_id
