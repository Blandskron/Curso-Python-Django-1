CREATE TABLE usuarios (
  user_id SERIAL PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  password_hash TEXT NOT NULL
);