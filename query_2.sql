SELECT s.student_id, s.student_name, AVG(sm.mark) AS average_mark
FROM students s
JOIN student_marks sm ON s.student_id = sm.student_id
JOIN subjects sub ON sm.subject_id = sub.subject_id
WHERE sub.subject_name = 'message'
GROUP BY s.student_id, s.student_name
ORDER BY average_mark DESC
LIMIT 1;
