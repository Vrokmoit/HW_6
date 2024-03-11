SELECT AVG(sm.mark) AS average_mark
FROM student_marks sm
JOIN subjects subj ON sm.subject_id = subj.subject_id
JOIN teachers t ON subj.teacher_id = t.teacher_id
WHERE t.teacher_name = 'Brenda Mccann';