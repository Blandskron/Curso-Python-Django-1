CREATE TABLE org.audit_log (
  audit_id BIGSERIAL PRIMARY KEY,
  table_name TEXT NOT NULL,
  action TEXT NOT NULL,
  record_id BIGINT,
  changed_at TIMESTAMP NOT NULL DEFAULT now()
);