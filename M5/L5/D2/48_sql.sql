SELECT code, COUNT(*)
FROM courses
GROUP BY code
HAVING COUNT(*) > 1;