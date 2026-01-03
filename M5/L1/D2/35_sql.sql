SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_schema = 'org'
ORDER BY table_name;