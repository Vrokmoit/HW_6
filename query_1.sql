SELECT s.student_id, s.student_name, AVG(sm.mark) AS average_mark
FROM students s
JOIN student_marks sm ON s.student_id = sm.student_id
GROUP BY s.student_id, s.student_name
ORDER BY average_mark DESC
LIMIT 5;