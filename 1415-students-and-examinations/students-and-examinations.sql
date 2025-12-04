# Write your MySQL query statement below
select Students.student_id, STudents.student_name, Subjects.subject_name, count(Examinations.subject_name) as attended_exams
From Students
JOIN Subjects
LEFT JOIN Examinations on Examinations.student_id = Students.student_id AND Subjects.subject_name = Examinations.subject_name
GROUP by 1,2,3
ORDER BY 1,3;
