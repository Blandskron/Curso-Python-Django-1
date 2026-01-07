"""
Ejemplo Python: Clase Cliente
class Cliente:
    def __init__(self, client_id, name, email, country, created_at):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.country = country
        self.created_at = created_at

Ejemplo SQL: Crear tabla clients
CREATE TABLE clients (
  client_id   INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name        VARCHAR(120) NOT NULL,
  email       VARCHAR(180) NULL,
  country     VARCHAR(80)  NOT NULL,
  created_at  TIMESTAMP    NOT NULL DEFAULT now()
);
"""

from django.db import models


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=180, null=True,blank=True)
    country = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "clients"
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return f"{self.name} ({self.country})"
