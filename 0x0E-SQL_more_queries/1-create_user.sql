-- creates a user and grants all privileges
-- sql query syntax to create a user
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES TO user_0d_1@localhost ON *.*;
