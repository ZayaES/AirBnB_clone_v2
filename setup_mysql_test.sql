-- Create the database hbnb_test_db if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user - hbnb_test with hbnb_test_pwd as password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the hbnb_test_db to the hbnb_test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the performance_schema to the hbnb_test user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
