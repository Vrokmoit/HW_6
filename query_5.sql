SELECT subj.subject_name
FROM subjects subj
JOIN teachers t ON subj.teacher_id = t.teacher_id
WHERE t.teacher_name = 'Samuel Gray';
