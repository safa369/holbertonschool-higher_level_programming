-- best score >= 10.
SELECT score, name FROM second_table
HAVING score >= 10
ORDER BY score DESC;