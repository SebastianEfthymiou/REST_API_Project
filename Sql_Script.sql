CREATE DATABASE IF NOT EXISTS productdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE productdb;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price FLOAT NOT NULL,
    stock INT DEFAULT 0
);
