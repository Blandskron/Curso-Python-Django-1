SELECT email, COUNT(*)
FROM students
GROUP BY email
HAVING COUNT(*) > 1;