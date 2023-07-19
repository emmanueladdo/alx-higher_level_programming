-- Update score of Bob to 10 from 'second_table' of 'hbtn_0c_0'
-- Not allowed to use Bob's id value, only name field
-- db name will be passed as arg to mysql cmd
UPDATE second_table
WHERE name = "Bob"
SET score = 10;
