ALTER TABLE modules
DROP CONSTRAINT modules_course_id_fkey;

ALTER TABLE modules
ADD CONSTRAINT modules_course_id_fkey
FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE;