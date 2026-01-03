CREATE TABLE student_addresses (
  student_id BIGINT NOT NULL REFERENCES students(student_id) ON DELETE CASCADE,
  address_no SMALLINT NOT NULL CHECK (address_no > 0),
  street     VARCHAR(160) NOT NULL,
  city       VARCHAR(80) NOT NULL,
  country    CHAR(2) NOT NULL,
  PRIMARY KEY (student_id, address_no)
);