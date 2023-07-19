-- List all records in 'second_table' of 'hbtn_0c_0'
-- Results should display both score and name
-- Records should be ordered by score (top first)
-- where score greater of equal to ten
-- db name will be passed as arg to mysql cmd
SELECT score, name FROM second_table
WHERE score >= 10 ORDER BY score DESC;
