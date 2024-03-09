# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        '''Add a new user to the user.txt file'''
        while True:
            # Request new username
            new_username = input("New Username: ")
        
            # Check if username already exists
            if new_username in username_password:
                print("That username already exists, please try a different one")
            else:
                break

        # - Request input of a new password
        new_password = input("New Password: ")

        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
            
            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))

        # - Otherwise you present a relevant message.
        else:
            print("Passwords do no match")

    elif menu == 'a':
        '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")


        # Then get the current date.
        curr_date = date.today()
        ''' Add the data to the file task.txt and
            Include 'No' to indicate if the task is complete.'''
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        task_list.append(new_task)
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        print("Task successfully added.")


    elif menu == 'va':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''

        for t in task_list:
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            


    elif menu == 'vm':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''

        '''View all tasks assigned to the current user'''
        task_index = 1
        task_indices = {}  # Dictionary to map task numbers to task indices in task_list

        print("Tasks Assigned to You:")
        for i, t in enumerate(task_list):
            if t['username'] == curr_user:
                print(f"Task {task_index}: {t['title']}")
                task_indices[task_index] = i  # Mapping task number to task index
                task_index += 1

        # If no tasks are assigned to the user
        if task_index == 1:
            print("No tasks assigned to you.")
        else:
            # Ask user to select a task or return to main menu
            while True:
                choice = input(f"Enter task number (1-{task_index - 1}) to select a task, or enter -1 to return to the main menu: ")
                if choice == '-1':
                    break
                elif choice.isdigit():
                    task_num = int(choice)
                    if 1 <= task_num <= task_index - 1:
                        task_idx = task_indices[task_num]
                        selected_task = task_list[task_idx]
                        print("Task Details:")
                        print(f"Title: {selected_task['title']}")
                        print(f"Assigned to: {selected_task['username']}")
                        print(f"Date Assigned: {selected_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
                        print(f"Due Date: {selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
                        print(f"Task Description:\n{selected_task['description']}")

                        # Allow user to mark task as complete or edit task if it's not completed
                        if not selected_task['completed']:
                            task_action = input("Enter 'complete' to mark the task as complete or 'edit' to edit the task: ").lower()
                            if task_action == 'complete':
                                task_list[task_idx]['completed'] = True
                                print("Task marked as complete.")
                            elif task_action == 'edit':
                                new_username = input("Enter new username (press Enter to skip): ")
                                new_due_date_str = input("Enter new due date (YYYY-MM-DD) (press Enter to skip): ")
                                if new_username:
                                    task_list[task_idx]['username'] = new_username
                                if new_due_date_str:
                                    new_due_date = datetime.strptime(new_due_date_str, DATETIME_STRING_FORMAT)
                                    task_list[task_idx]['due_date'] = new_due_date
                                print("Task edited.")
                            else:
                                print("Invalid choice.")
                        else:
                            print("Task is already completed.")

                    else:
                        print("Invalid task number.")
                else:
                    print("Invalid input. Please enter a number or -1.")

        
        # for t in task_list:
        #     if t['username'] == curr_user:
        #         disp_str = f"Task: \t\t {t['title']}\n"
        #         disp_str += f"Assigned to: \t {t['username']}\n"
        #         disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        #         disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        #         disp_str += f"Task Description: \n {t['description']}\n"
        #         print(disp_str)
                
    elif menu == 'gr':
        '''Generate reports'''
        total_tasks = len(task_list)
        completed_tasks = sum(1 for t in task_list if t['completed'])
        uncompleted_tasks = total_tasks - completed_tasks
        overdue_tasks = sum(1 for t in task_list if not t['completed'] and t['due_date'] < datetime.now())
        incomplete_percentage = (uncompleted_tasks / total_tasks) * 100
        overdue_percentage = (overdue_tasks / total_tasks) * 100

        # Write task overview to task_overview.txt
        with open("task_overview.txt", "w") as task_overview_file:
            task_overview_file.write("Task Overview\n")
            task_overview_file.write(f"Total number of tasks: {total_tasks}\n")
            task_overview_file.write(f"Total number of completed tasks: {completed_tasks}\n")
            task_overview_file.write(f"Total number of uncompleted tasks: {uncompleted_tasks}\n")
            task_overview_file.write(f"Total number of overdue tasks: {overdue_tasks}\n")
            task_overview_file.write(f"Percentage of tasks that are incomplete: {incomplete_percentage:.2f}%\n")
            task_overview_file.write(f"Percentage of tasks that are overdue: {overdue_percentage:.2f}%\n")

        # Calculate user overview data
        total_users = len(username_password)
        user_task_count = {user: 0 for user in username_password.keys()}
        user_completed_count = {user: 0 for user in username_password.keys()}
        for task in task_list:
            user_task_count[task['username']] += 1
            if task['completed']:
                user_completed_count[task['username']] += 1

        # Write user overview to user_overview.txt
        with open("user_overview.txt", "w") as user_overview_file:
            user_overview_file.write("User Overview\n")
            user_overview_file.write(f"Total number of users: {total_users}\n")
            user_overview_file.write(f"Total number of tasks: {total_tasks}\n")
            for user in username_password.keys():
                total_user_tasks = user_task_count[user]
                completed_user_tasks = user_completed_count[user]
                incomplete_user_tasks = total_user_tasks - completed_user_tasks
                overdue_user_tasks = sum(1 for t in task_list if t['username'] == user and not t['completed'] and t['due_date'] < datetime.now())
                user_percentage = (total_user_tasks / total_tasks) * 100
                user_completed_percentage = (completed_user_tasks / total_user_tasks) * 100 if total_user_tasks != 0 else 0
                user_incomplete_percentage = (incomplete_user_tasks / total_user_tasks) * 100 if total_user_tasks != 0 else 0
                user_overdue_percentage = (overdue_user_tasks / total_user_tasks) * 100 if total_user_tasks != 0 else 0

                user_overview_file.write(f"\nUser: {user}\n")
                user_overview_file.write(f"Total number of tasks assigned: {total_user_tasks}\n")
                user_overview_file.write(f"Percentage of total tasks assigned: {user_percentage:.2f}%\n")
                user_overview_file.write(f"Percentage of tasks completed: {user_completed_percentage:.2f}%\n")
                user_overview_file.write(f"Percentage of tasks to be completed: {user_incomplete_percentage:.2f}%\n")
                user_overview_file.write(f"Percentage of overdue tasks: {user_overdue_percentage:.2f}%\n")

        print("Reports generated successfully.")


    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        
        # Check if task_overview.txt and user_overview.txt exist. If not, generate the reports.
        if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
            print("Reports have not been generated yet. Generating reports...")
            # Call the code to generate reports
            # (the code provided in the previous response)

        # Read task overview from task_overview.txt and print on screen
        with open("task_overview.txt", "r") as task_overview_file:
            print("Task Overview:")
            print(task_overview_file.read())

        # Read user overview from user_overview.txt and print on screen
        with open("user_overview.txt", "r") as user_overview_file:
            print("\nUser Overview:")
            print(user_overview_file.read())
        
        # num_users = len(username_password.keys())
        # num_tasks = len(task_list)

        # print("-----------------------------------")
        # print(f"Number of users: \t\t {num_users}")
        # print(f"Number of tasks: \t\t {num_tasks}")
        # print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")