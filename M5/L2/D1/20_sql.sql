SELECT client_id, name, COALESCE(email, 'SIN EMAIL') AS email
FROM clients;