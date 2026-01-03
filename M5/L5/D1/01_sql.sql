CREATE TABLE students (
  student_id BIGSERIAL PRIMARY KEY,
  full_name  VARCHAR(120) NOT NULL,
  email      VARCHAR(150) UNIQUE NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT now()
);