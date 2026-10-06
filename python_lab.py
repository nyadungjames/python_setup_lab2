-- Create the school database
CREATE DATABASE school;
USE school;

-- Create the students table with proper data constraints
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    enrolled_on DATE NOT NULL
);

-- Insert two sample records
INSERT INTO students (name, email, enrolled_on) VALUES
('Alice Wanjiku', 'alice.wanjiku@email.com', '2026-10-06'),
('John Omwamba', 'john.omwamba@email.com', '2026-10-06');

-- Query to retrieve all records
SELECT * FROM students;
