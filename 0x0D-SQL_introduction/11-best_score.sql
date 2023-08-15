-- This script lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
--- Records should be ordered by score (top first)
SELECT score, name
FROM TABLE second_table
WHERE SCORE IS >= 10 ORDER BY DEC;
