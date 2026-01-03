CREATE TABLE raw_enrollments_bad (
  student_email VARCHAR(150),
  student_name  VARCHAR(120),
  course_code   VARCHAR(30),
  course_title  VARCHAR(160),
  module_titles TEXT, -- "Intro|SQL Básico|JOINs"
  status        VARCHAR(20),
  final_grade   NUMERIC(5,2)
);