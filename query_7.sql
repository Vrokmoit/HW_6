SELECT sm.mark, s.student_name
FROM student_marks sm
JOIN students s ON sm.student_id = s.student_id
JOIN groupsst gs ON s.stgroup_id = gs.group_id
JOIN subjects subj ON sm.subject_id = subj.subject_id
WHERE gs.group_name = 'Group 1' AND subj.subject_name = 'message';
