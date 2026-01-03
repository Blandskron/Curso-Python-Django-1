ALTER TABLE student_addresses
ADD CONSTRAINT fk_addr_country
FOREIGN KEY (country) REFERENCES countries(country_code);