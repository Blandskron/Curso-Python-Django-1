SELECT
  c.relname AS table_name,
  a.attname AS column_name,
  d.description
FROM pg_class c
JOIN pg_attribute a ON a.attrelid = c.oid
LEFT JOIN pg_description d ON d.objoid = c.oid AND d.objsubid = a.attnum
WHERE c.relkind = 'r' AND a.attnum > 0
ORDER BY table_name, a.attnum;