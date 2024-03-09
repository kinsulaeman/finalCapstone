**Capstone Project **

This project is a command-line task management application that allows users to register, add tasks, view tasks, and generate reports. 
The application uses two text files, user.txt and tasks.txt, to store user and task data, respectively.

Table of Contents
- Installation
- Usage
- Features
- Credits

Installation
- Clone the repository or download the project files.
- Make sure you have Python installed on your system.
- Navigate to the project directory in your terminal or command prompt.
- Run the task_manager.py file using the following command:
  python task_manager.py

Usage
Upon running the task_manager.py file, you will be presented with a menu of options. Follow the on-screen instructions to navigate through the application.
Here are the available options:
r: Register a new user
a: Add a new task
va: View all tasks
vm: View tasks assigned to the current user
ds: Display statistics and generate reports
e: Exit the application

When selecting vm (View tasks assigned to the current user), you can:
View all tasks assigned to you with corresponding numbers
Select a specific task by entering its number
Mark a selected task as complete
Edit the username or due date of an incomplete selected task

When selecting ds (Display statistics and generate reports), the application will generate two text files:
task_overview.txt: Contains statistics about the total tasks, completed tasks, uncompleted tasks, overdue tasks, and percentages.
user_overview.txt: Contains statistics about the total users, total tasks, and individual user task statistics.
If these text files do not exist, the application will generate them before displaying the reports on the screen.

Features
- User registration with duplicate username prevention
- Task addition
- View all tasks
- View tasks assigned to the current user
- Mark tasks as complete
- Edit task details (username and due date for incomplete tasks)
- Generate task and user overview reports
- Display reports on the screen

Credits
This project was developed by Kinkin Sulaeman as part of the Capstone Project Task 1 for Software Engineering (Fundamentals) course.
