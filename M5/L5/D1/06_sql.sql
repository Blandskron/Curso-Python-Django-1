CREATE TABLE course_profiles (
  course_id BIGINT PRIMARY KEY REFERENCES courses(course_id) ON DELETE CASCADE,
  description TEXT,
  language VARCHAR(10) NOT NULL DEFAULT 'es'
);