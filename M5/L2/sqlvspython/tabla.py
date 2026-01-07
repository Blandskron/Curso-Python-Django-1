"""
Ejemplo SQL: Crear tabla clients
CREATE TABLE clients (
  client_id   INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name        VARCHAR(120) NOT NULL,
  email       VARCHAR(180) NULL,
  country     VARCHAR(80)  NOT NULL,
  created_at  TIMESTAMP    NOT NULL DEFAULT now()
);
"""

class Cliente:
    def __init__(self, client_id, name, email, country, created_at):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.country = country
        self.created_at = created_at
