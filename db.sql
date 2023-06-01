-- Create teachers table
CREATE TABLE teachers (
    username VARCHAR(50) PRIMARY KEY,
    teacher_name varchar(20),
    password VARCHAR(50),
    email varchar(20),
    phone varchar(10)
);

-- Insert dummy data into teachers table
INSERT INTO teachers (username, teacher_name,password,email,phone)
VALUES
    ('teacher1','Jenny','password1','jenny@gmail.com','9183885580'),
    ('teacher2','Mary','password2','marys@gmail.com','9801802223');

-- Create admins table
CREATE TABLE admins (
    username VARCHAR(50) PRIMARY KEY,
    admin_name varchar(20),
    password VARCHAR(50),
    email varchar(20),
    phone varchar(10)
);

-- Insert dummy data into admins table
INSERT INTO admins (username, admin_name,password,email,phone)
VALUES
    ('admin1','Will Smith','password1','smithw@gmail.com','9550634682'),
    ('admin2','John Wick', 'password2','wjohn@gmai.com','8192083447');

-- Create classes table
CREATE TABLE classes (
    class_id INT PRIMARY KEY AUTO_INCREMENT,
    class_name VARCHAR(50),
    teacher_username VARCHAR(50),
    class_sec VARCHAR(10),
    FOREIGN KEY (teacher_username) REFERENCES teachers(username)
);


-- Create classes table
CREATE TABLE classes (
    class_id INT PRIMARY KEY AUTO_INCREMENT,
    class_name VARCHAR(50),
    teacher_username VARCHAR(50),
    class_date date,
    class_sec VARCHAR(10),
    FOREIGN KEY (teacher_username) REFERENCES teachers(username)
);

-- Insert dummy data into classes table
INSERT INTO classes (class_id, class_name, teacher_username, class_date,class_sec)
VALUES
    (1,'Machine Learning','teacher1','2023-05-31',,'CSE1'),
    (2,'BCT', 'teacher2','2023-05-31','CSE2'),
    (3,'CPNM','teacher1','2023-05-30','CSE2'),
    (4,'Statistics','teacher1','2023-06-01','CSE2'),
    (5,'Algorithms','teacher2','2023-05-30','CSE1'),
    (6,'DS','teacher2','2023-06-01','CSE1');

-- Create students table
CREATE TABLE students (
    student_id INT PRIMARY KEY ,
    student_name VARCHAR(50),
    email varchar(20),
    class_sec VARCHAR(10),
    phone varchar(10)
);

-- Insert dummy data into students table
INSERT INTO students (student_id,student_name, email,class_sec,phone)
VALUES
    (1,'John Doe','john@gmail.com','CSE1','8866443210' ),
    (2,'Jane Smith','smithj@gmail.com','CSE1','9313302392'),
    (3,'Mark Johnson','johnm@gmail.com','CSE2','9314123452' ),
    (4,'Emily Davis','davis@gmail.com','CSE2','9233351521'),
    (5,'Jacob White','dean58@example.net','CSE1','6059073030'),
    (6,'Shaun Simpson','kochvickie@example.net','CSE1','896-060-15'),
    (7,'Tyler Hodge','christinebarrett@example.net','CSE1','836-921-13'),
    (8,'Steven Reid','dwaynewright@example.com','CSE1','3841459133'),
    (9,'Sheila Jones','keithnixon@example.net','CSE1','240-938-36'),
    (10,'Courtney Richards','pamela49@example.net','CSE1','209-582-42'),
    (11,'Angela Williams','hallvirginia@example.org','CSE1','(931)552-5'),
    (12,'Taylor Jackson','kristin79@example.net','CSE1','(242)991-2'),
    (13,'Joshua Morris','camposbreanna@example.org','CSE2','(313)267-3'),
    (14,'Jasmin Parker','christopher44@example.org','CSE2','(509)934-1'),
    (15,'Marc Chang','amygibbs@example.net','CSE2','(555)978-8'),
    (16,'Kimberly Haynes','meganspencer@example.org','CSE2','139.554.92'),
    (17,'Dr. Robert Jacobson','brownkristin@example.org','CSE2','5538343275'),
    (18,'Anthony Miller','rebekahsalazar@example.org','CSE2','117.760.40'),
    (19,'Laura Stewart','paul54@example.net','CSE2','749-718-11'),
    (20,'Jacqueline York','belldenise@example.com','CSE2','001-348-79');

-- Create attendance table
CREATE TABLE attendance (
    id INT PRIMARY KEY AUTO_INCREMENT,
    class_id INT,
    student_id INT,
    status ENUM('present', 'absent'),
    FOREIGN KEY (class_id) REFERENCES classes(class_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Insert dummy data into attendance table
INSERT INTO attendance (id,class_id, student_id, status)
VALUES
    (1, 1, 1, 'present'),
    (2, 1, 2, 'absent'),
    (3, 2, 3, 'present'),
    (4, 2, 4, 'absent');
