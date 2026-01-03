CREATE TABLE enrollments (
  student_id BIGINT NOT NULL REFERENCES students(student_id) ON DELETE CASCADE,
  course_id  BIGINT NOT NULL REFERENCES courses(course_id) ON DELETE RESTRICT,
  enrolled_at TIMESTAMP NOT NULL DEFAULT now(),
  status     VARCHAR(20) NOT NULL CHECK (status IN ('ACTIVE','COMPLETED','DROPPED')),
  final_grade NUMERIC(5,2) CHECK (final_grade BETWEEN 1 AND 7),
  PRIMARY KEY (student_id, course_id)
);