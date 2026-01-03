CREATE TABLE modules (
  module_id BIGSERIAL PRIMARY KEY,
  course_id BIGINT NOT NULL REFERENCES courses(course_id) ON DELETE CASCADE,
  title     VARCHAR(160) NOT NULL,
  position  INT NOT NULL CHECK (position > 0),
  UNIQUE (course_id, position)
);