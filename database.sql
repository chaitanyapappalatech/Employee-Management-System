CREATE DATABASE employee_db;

USE employee_db;

CREATE TABLE employees(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    email VARCHAR(100)
);
