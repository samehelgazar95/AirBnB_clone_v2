-- MySQL setup script for test environment


-- Create database (if not already exists)
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- Create user (if not already exists)
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Make user hbnb_test as a root
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost'; 

-- Grant specific privilege for `performance_schema` database
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;
