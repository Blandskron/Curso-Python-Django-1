INSERT INTO clients (email, name, country)
VALUES ('contacto@acme.cl', 'Acme SpA', 'CL')
ON CONFLICT (email)
DO UPDATE SET name = EXCLUDED.name,
              country = EXCLUDED.country;