CREATE DATABASE IF NOT EXISTS query_system;
USE query_system;

CREATE TABLE users (
    username VARCHAR(50) PRIMARY KEY,
    hashed_password VARCHAR(255) NOT NULL,
    role ENUM('Client', 'Support') NOT NULL
);

CREATE TABLE queries (
    query_id INT AUTO_INCREMENT PRIMARY KEY,
    mail_id VARCHAR(100) NOT NULL,
    mobile_number VARCHAR(20),
    query_heading VARCHAR(255) NOT NULL,
    query_description TEXT NOT NULL,
    status ENUM('Open', 'Closed') DEFAULT 'Open',
    query_created_time DATETIME NOT NULL,
    query_closed_time DATETIME DEFAULT NULL
);

select * from users;
select * from queries;