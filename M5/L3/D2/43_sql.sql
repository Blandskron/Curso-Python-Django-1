UPDATE clients
SET email = 'nuevo@acme.cl'
WHERE client_id = 1
RETURNING client_id, name, email;