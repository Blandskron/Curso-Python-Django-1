CREATE TABLE student_primary_address (
  student_id BIGINT PRIMARY KEY REFERENCES students(student_id) ON DELETE CASCADE,
  street VARCHAR(160) NOT NULL,
  city VARCHAR(80) NOT NULL,
  country CHAR(2) NOT NULL REFERENCES countries(country_code)
);