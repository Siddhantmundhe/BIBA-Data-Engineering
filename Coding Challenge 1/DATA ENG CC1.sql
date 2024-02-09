#DATA ENGINEERING BATCH 1
#CODING CHALLENGE 1

CREATE DATABASE IF NOT EXISTS coding_challenge;

use coding_challenge;

CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    registration_date DATE
);

INSERT INTO users (user_id, username, email, registration_date) VALUES
    (1, 'Siddhant_Mundhe', 'sid@gmail..com', '2022-01-01'),
    (2, 'Aniket_Biyani', 'aniket@gmail.com', '2022-02-15'),
    (3, 'Abhishek_kanauja', 'abhi@gmail.com', '2022-03-20');
    
CREATE TABLE IF NOT EXISTS challenges (
    challenge_id INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    difficulty VARCHAR(20),
    creation_date DATE
);

INSERT INTO challenges (challenge_id, title, description, difficulty, creation_date) VALUES
    (101, 'String Reversal', 'Reverse a given string', 'Easy', '2022-01-10'),
    (102, 'Palindrome Check', 'Check if a given string is a palindrome', 'Medium', '2022-02-25'),
    (103, 'Prime Number Finder', 'Find prime numbers within a given range', 'Hard', '2022-03-30');
    
CREATE TABLE IF NOT EXISTS submissions (
    submission_id INT PRIMARY KEY,
    user_id INT,
    challenge_id INT,
    submission_date DATE,
    result VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (challenge_id) REFERENCES challenges(challenge_id)
);

INSERT INTO submissions (submission_id, user_id, challenge_id, submission_date, result) VALUES
    (201, 1, 101, '2022-01-15', 'Accepted'),
    (202, 2, 102, '2022-03-05', 'Failed'),
    (203, 3, 103, '2022-04-10', 'Accepted');
    
# Over By and partition Clause
#Assign a unique row number(A/C to difficulty level)

SELECT
    s.user_id,
    s.challenge_id,
    s.result,
    ROW_NUMBER() OVER (PARTITION BY c.difficulty ORDER BY s.challenge_id) AS row_num
FROM
    submissions s
JOIN
    challenges c ON s.challenge_id = c.challenge_id;
    
# Calculate the cumulative sum of submissions for each user

SELECT
    user_id,
    challenge_id,
    result,
    SUM(1) OVER (PARTITION BY user_id ORDER BY submission_date) AS cumulative_submissions
FROM
    submissions;
    
# Subtotals
# Count the number of submissions for each difficulty level

SELECT
    c.difficulty,
    COUNT(*) AS total_submissions
FROM
    submissions s
JOIN
    challenges c ON s.challenge_id = c.challenge_id
GROUP BY
    c.difficulty;
    
#Total aggregation
#Using Count function
#Get the total number of records in the submissions table.

SELECT
    COUNT(*) AS total_submissions
FROM
    submissions;

#JOINS

#Inner Join
/* The inner join is used to select all matching rows or columns in both tables.*/
/* Retrieve information about submissions along with the corresponding user and challenge details.*/

SELECT
    s.user_id,u.username,c.title
    AS challenge_title,s.result
FROM
    submissions s
JOIN
    users u ON s.user_id = u.user_id
JOIN
    challenges c ON s.challenge_id = c.challenge_id;
    
#Left Join/Left Outer Join
/* The LEFT JOIN is used to retrieve all records from the left table and the matched rows or columns from the right table.
 If both tables do not contain any matched rows or columns, it returns the NULL.*/
/*Finds all users along with their submissions, even if they haven't submitted any challenges.*/

SELECT
    u.user_id,u.username,s.challenge_id,s.result
FROM
    users u
LEFT JOIN
    submissions s ON u.user_id = s.user_id;

#RIGHT JOIN/RIGHT Outer JOIN:
/*The RIGHT JOIN is used to retrieve all records from the right table and the matched 
rows or columns from the left table. If both tables do not contain any matched rows or columns, it returns the NULL.*/
/*Finds all challenges along with the submissions, even if there are no submissions for some challenges.*/

SELECT
    c.challenge_id,c.title,s.user_id,s.result
FROM
    challenges c
RIGHT JOIN
    submissions s ON c.challenge_id = s.challenge_id;

#FULL JOIN/FULL Outer JOIN:
/*It is a combination result set of both LEFT JOIN and RIGHT JOIN. The joined tables return all 
records from both the tables and if no matches are found in the table, it places NULL. It is also called a FULL OUTER JOIN.*/
/* Retrieve all users and challenges along with their submissions.*/

SELECT
    u.user_id,u.username,s.challenge_id,s.result
FROM
    users u
LEFT JOIN
    submissions s ON u.user_id = s.user_id
UNION
SELECT
    u.user_id,u.username,s.challenge_id,s.result
FROM
    submissions s
RIGHT JOIN
    users u ON s.user_id = u.user_id;

# CROSS JOIN
/*It is also known as CARTESIAN JOIN, which returns the Cartesian product of two or more joined tables. The CROSS JOIN produces a table 
that merges each row from the first table with each second table row.*/


SELECT
    u.user_id,
    u.username,
    c.challenge_id,
    c.title AS challenge_title
FROM
    users u
CROSS JOIN
    challenges c;









