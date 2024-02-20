-- MySQL setup test
-- Write a script that prepares a MySQL server for the project:


-- Creating the DATABASE called hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creating a user 'hbnb_test'@'localhost' with passwd hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Make user hbnb_test as a root
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost' WITH GRANT OPTION; 

-- Grant user to SELECT ON specific db
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
