-- Creates the table 'unique_id'
-- id INT default 1 unique, name VARCHAR(256)
-- If table already exists, script should not fail
-- The database name will be passed as an arg of the mysql cmd
CREATE TABLE IF NOT EXISTS unique_id
(
		id INT DEFAULT 1 UNIQUE,
			name VARCHAR(256)
		);
