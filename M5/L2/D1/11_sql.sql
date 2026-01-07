SELECT client_id, name
FROM clients
WHERE name ILIKE '%spa%'; 
-- contenido 'spa' en cualquier parte del nombre

SELECT client_id, name
FROM clients
WHERE name ILIKE 'Amc%'; 
-- contenido 'Amc' al inicio del nombre

SELECT client_id, name
FROM clients
WHERE name ILIKE '%e Spa'; 
-- contenido 'e Spa' al final del nombre