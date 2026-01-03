ALTER TABLE enrollments
ADD CONSTRAINT chk_grade
CHECK (final_grade IS NULL OR final_grade BETWEEN 1 AND 7);