CREATE TABLE enrollments_surrogate (
  enrollment_id BIGSERIAL PRIMARY KEY,
  student_id BIGINT NOT NULL REFERENCES students(student_id),
  course_id  BIGINT NOT NULL REFERENCES courses(course_id),
  status VARCHAR(20) NOT NULL,
  UNIQUE (student_id, course_id)
);