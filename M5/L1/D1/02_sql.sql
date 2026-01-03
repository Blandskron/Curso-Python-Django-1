CREATE TABLE org.clients (
  client_id BIGSERIAL PRIMARY KEY,
  name      VARCHAR(120) NOT NULL,
  email     VARCHAR(150) UNIQUE,
  created_at TIMESTAMP NOT NULL DEFAULT now()
);