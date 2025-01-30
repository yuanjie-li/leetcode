SELECT 
    student_id 
    ,student_name 
    ,subject_name 
    ,IFNULL(attended_exams, 0) AS attended_exams 
FROM Students s 

CROSS JOIN Subjects 

LEFT JOIN 
(
    SELECT DISTINCT  
        subject_name AS exam_subject_name 
        ,student_id as exam_student_id
        ,COUNT(subject_name)OVER(PARTITION BY student_id, subject_name) AS attended_exams
    FROM Examinations 
) exam 
ON 
exam_student_id = student_id 
AND 
exam_subject_name = subject_name

ORDER BY student_id, subject_name 
