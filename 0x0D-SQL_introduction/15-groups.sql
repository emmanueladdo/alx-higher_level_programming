-- List number of records with same score in 'second_table'
-- of db 'hbtn_0c_0'
-- Result should display the score and
-- number of records for this score with label 'number'
-- List should be sorted by number of records descending
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
