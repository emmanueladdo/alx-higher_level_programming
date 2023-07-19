-- Convert 'hbtn_0c_0' to utf8mb4, collate utf8mb4_unicode_ci
-- Convert db 'hbtn_0c_0'
-- Convert hbtn_0c_0 database to UTF8 (utf8mb4)
ALTER DATABASE hbtn_0c_0 CHARACTER 
SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert first_table table to UTF8 (utf8mb4)
ALTER TABLE hbtn_0c_0.first_table 
CONVERT TO CHARACTER 
SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert name field in first_table to UTF8 (utf8mb4)
ALTER TABLE hbtn_0c_0.first_table 
MODIFY COLUMN name VARCHAR(255) CHARACTER 
SET utf8mb4 COLLATE utf8mb4_unicode_ci;
