SELECT student_name
FROM students s
JOIN groupsst gs ON s.stgroup_id = gs.group_id
WHERE gs.group_name = 'Group 1';
