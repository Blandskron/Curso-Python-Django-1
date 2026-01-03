CREATE OR REPLACE VIEW v_student_course_status AS
SELECT s.student_id, s.full_name, s.email,
       c.course_id, c.code, c.title,
       e.status, e.enrolled_at, e.final_grade
FROM students s
JOIN enrollments e ON e.student_id = s.student_id
JOIN courses c ON c.course_id = e.course_id;