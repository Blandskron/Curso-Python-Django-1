ALTER TABLE enrollments
ADD CONSTRAINT chk_enroll_status
CHECK (status IN ('ACTIVE','COMPLETED','DROPPED'));