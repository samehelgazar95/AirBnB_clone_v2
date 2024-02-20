-- MySQL setup development
-- Write a script that prepares a MySQL server for the project:


-- Creating database called hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creating user called hbnb_dev (in localhost) with passwd hbnb_dev_pwd 
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Make hbnb_dev as a root
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;

-- Grant user with SELECT for specific db 
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
