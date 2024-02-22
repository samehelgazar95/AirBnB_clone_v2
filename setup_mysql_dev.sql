-- MySQL setup script for development environment


-- Create database (if not already exists)
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

-- Create user (if not already exists)
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- Grant specific privileges for `performance_schema` database
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;
