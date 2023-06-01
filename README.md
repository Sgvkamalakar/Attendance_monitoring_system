# Attendance Monitoring System

The Attendance Monitoring System is a software application designed to track and manage attendance records for organizations, schools, or any other group that requires attendance tracking. This system provides an efficient and automated way of recording attendance, reducing manual effort and ensuring accuracy.

## Features

- **User Authentication**: Secure user authentication and authorization system to ensure only authorized users can access the system.
- **Attendance Recording**: Easy and convenient attendance recording for individuals or groups, allowing users to mark attendance with just a few clicks.
- **Real-time Tracking**: Real-time monitoring and tracking of attendance status, providing instant updates on attendance records.
- **Reporting and Analytics**: Generate comprehensive attendance reports and analytics, including attendance summaries, trends, and individual attendance records.
- **Notifications**: Automated notifications to remind users of upcoming events, classes, or meetings and send alerts for absentees.
- **Data Management**: Efficient storage and management of attendance data, allowing users to search, filter, and organize attendance records easily.
- **Integration**: Seamless integration with existing systems or tools such as databases, student information systems, or employee management systems.
- **Customization**: Flexible configuration options to adapt the system to specific organizational requirements and workflows.
- **User-Friendly Interface**: Intuitive and easy-to-use interface for both administrators and users, ensuring a smooth user experience.
- **Scalability**: Ability to handle a large number of users and attendance records while maintaining performance and reliability.

## Getting Started

### Prerequisites

- Python: Make sure you have Python installed on your machine. You can download Python from the official website: python.org.

- Flask: Install Flask, a Python web framework, by running the following command in your command prompt or terminal: `pip install flask`
- Web Browser: The application is compatible with modern web browsers such as Chrome, Firefox, Safari, or Edge. Ensure you have the latest version of Google Chrome installed on your machine to view the application.
- MySQL Database: Install and set up MySQL database server on your machine. You can download MySQL Community Edition from the official website: dev.mysql.com/downloads.

- MySQL Connector: Install the MySQL Connector Python library, which allows Python to communicate with the MySQL database. You can install it using the following command: `pip install mysql-connector-python`

#### Database Configuration
- Create a new database in MySQL for your Attendance Monitoring System.
- Load the data from the db.sql file into the database
- Update the following details in the `app.py` code with your credentials
    - Host: The hostname or IP address of the MySQL database server.
    - Port: The port number on which MySQL is running (default is usually 3306).
    - Database: The name of the database you created for the Attendance Monitoring System.
    - Username: The username for accessing the MySQL database.
    - Password: The password for the specified userna


### Installation

1. Clone the repository: `git clone https://github.com/Sgvkamalakar/Attendance_monitoring_system.git`
2. `pip install -r requirements.txt`

### Usage
1. Start the MySQL database server.
2. Run the Flask application: `flask run`
3. Open your web browser and enter the following URL: http://localhost:5000
4. The application should now be running and connected to the MySQL database for data storage.

### Working
To provide an overview of the working of the Attendance Monitoring System based on the mentioned requirements, here's a step-by-step explanation:

#### Admin Registration and Student/Teacher Management:
- The admin has the authority to register teachers and students in the system.
- The admin can update student details as necessary, such as personal information, class/section, etc.

#### Teacher Profile and Class Creation:
-A registered teacher can log in and update their own profile information.
-The teacher can create a class by providing inputs such as class/section, subject name, and date.

#### Student Details Management by Admin:
- The admin has the ability to fetch and update student details, such as personal information or class/section assignment.

#### Marking Attendance by Teachers:
- The teacher can access the attendance portal for a specific class/section and date.
- In the attendance portal, the teacher can mark the attendance by checking the checkboxes corresponding to the students who are present.

#### Attendance Submission and Viewing:
- After marking the attendance, the teacher submits the attendance details.
- Both the teacher and the admin can view the attendance records of students.
- The attendance records provide information about the dates, class/section, and the presence or absence of each student.

#### Attendance Status for Any Class/Section:
- The admin has the capability to view the attendance status for any class/section.
- This feature allows the admin to monitor attendance trends and identify any issues or patterns.

The Attendance Monitoring System enables the admin to manage teachers and students, allows teachers to mark attendance for their classes, and provides a centralized platform for viewing and tracking attendance records. This system streamlines the attendance management process, reduces manual effort, and facilitates efficient monitoring of student attendance.




