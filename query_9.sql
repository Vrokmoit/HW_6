SELECT subj.subject_name
FROM subjects subj
JOIN student_marks sm ON subj.subject_id = sm.subject_id
JOIN students s ON sm.student_id = s.student_id
WHERE s.student_name = 'Robert Price';