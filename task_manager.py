"""Capstone template project for FCS Task 19 Compulsory task 1 and 2."""

# =====importing libraries===========
"""This is the section where you will import libraries"""
from datetime import date
import calendar
from collections import Counter


# Function when user selects r - register new user
def reg_user():
    """Add a new user to the user.txt file if admin
    - Request input of a new username, Request input of a new password, Request input of password confirmation, if confirmed -add them to the user.txt file,
    - Don't duplicate users.
    """
    duplicate_flag = False
    if username == "admin":
        new_username = input("Please enter a username: ")
        new_password = input("Please enter a new password: ")
        password_conf = input("Please reenter the password to confirm: ")
        with open("user.txt", "r") as f:
            if new_username in f:
                duplicate_flag = True
                print("Username already exists.")
        if new_password == password_conf and duplicate_flag == False:
            with open("user.txt", "a+") as f:
                f.write("\n" + new_username + ", " + new_password)
                print("New user registered.")
        else:
            print("Passwords don't match. Please try again")
    else:
        print("\n\nOnly admin can register new users.")
    return


# Function when user selects a - add new task
def add_task():
    """Allow a user to add a new task to task.txt file
    - Prompt a user a username, task title, description, due date and add the current date and "No" to task.txt
    """
    username = input(
        "Please enter the username of the person the task is assigned to: "
    )
    title = input("Please enter the task title: ")
    description = input("Please enter the task description: ")
    due_date = input("Please enter the task due date: ")
    assigned_date = date.today()
    assigned_date = (
        str(assigned_date.day)
        + " "
        + str(calendar.month_abbr[assigned_date.month])
        + " "
        + str(assigned_date.year)
    )
    with open("tasks.txt", "a+") as f:
        f.write(
            "\n"
            + username
            + ", "
            + title
            + ", "
            + description
            + ", "
            + due_date
            + ", "
            + assigned_date
            + ", "
            + "No"
        )
    return


# Function when user selects va - view all tasks
def view_all():
    """Read the task from task.txt file and print to the console
    - Read a line from the file, split comma and space, print the results"""

    with open("tasks.txt", "r") as f:
        lines = [line.rstrip() for line in f]
        for i in range(0, len(lines)):
            task = lines[i].strip().split(", ")
            print(
                f"Task: \t {task[1]} \nAssigned to: \t {task[0]} \nDate assigned: \t {task[3]} \nDue date: \t {task[4]} \nTask Complete: \t {task[5]} \nTask Description: \n   {task[2]} \n\n"
            )
    return


# Function when user selects vm - view all tasks assigned to them
def view_mine():
    """Read the task from task.txt file and print to the console in the format of Output 2 presented in the L1T19 pdf
    - Read a line from the file, split comma and space, print if user matches username in file
    """
    with open("tasks.txt", "r") as f:
        lines = [line.rstrip() for line in f]
        entry = []
        for i in range(1, len(lines) + 1):
            task = lines[i - 1].strip().split(", ")
            if username == task[0]:
                entry.append(i)
                print(
                    f"Task {i}: \t {task[1]} \nAssigned to: \t {task[0]} \nDate assigned: \t {task[3]} \nDue date: \t {task[4]} \nTask Complete: \t {task[5]} \nTask Description: \n   {task[2]} \n\n"
                )
    # User select task or return to menu
    while True:
        task_select = int(
            input(
                "Please enter a task number to edit the task, or -1 to return to the main menu: "
            )
        )
        menu_flag = change_task(task_select, entry)
        if menu_flag == True:
            break
    return


# Function to edit task or mark it as complete
def change_task(task_select, entry):
    menu_flag = False
    if task_select in entry:
        for i in entry:
            if task_select == i:
                edit_or_complete = input(
                    'Enter "c" to mark the task as complete or "e" to edit the task: '
                )
                if edit_or_complete.lower() == "c":
                    menu_flag = mark_as_complete(task_select)
                elif edit_or_complete.lower() == "e":
                    edit_task(task_select)
    elif task_select == -1:
        menu_flag = True
    return menu_flag


# Function to mark task as complete
def mark_as_complete(task_select):
    if task_select == -1:
        return True
    else:
        with open("tasks.txt", "r+") as f:  # Calculate number of lines in file
            linelist = f.readlines()
        with open(
            "tasks.txt", "r+"
        ) as f:  # Replace "No" with "Yes" if the line index matches the chosen task
            linecount = 0
            for line in linelist:
                linecount += 1
                if linecount == task_select:
                    line = line.replace("No", "Yes")
                    f.write(line)
                else:
                    f.write(line)
    return


# Function to edit username or due date of task
def edit_task(task_select):
    selection = int(
        input(
            "Please select 1 to change the task assignee, or 2 to edit the due date: "
        )
    )
    if selection == 1:  # Change username of person to do the task
        new_username = input("Please enter the new user to assign the task to: ")
        with open("tasks.txt", "r+") as f:  # Calculate number of lines in file
            linelist = f.readlines()
        with open("tasks.txt", "r+") as f:  # Write new username into file
            linecount = 0
            for line in linelist:
                linecount += 1
                task = line.strip().split(", ")
                if linecount == task_select:
                    f.write(
                        f"{new_username}, {task[1]}, {task[2]}, {task[3]}, {task[4]}, {task[5]}\n"
                    )
                else:
                    f.write(
                        f"{task[0]}, {task[1]}, {task[2]}, {task[3]}, {task[4]}, {task[5]}\n"
                    )
    elif selection == 2:
        new_due_date = input("Please enter the new due date: ")
        with open("tasks.txt", "r+") as f:  # Calculate number of lines in file
            linelist = f.readlines()
        with open("tasks.txt", "r+") as f:  # Write new username into file
            linecount = 0
            for line in linelist:
                linecount += 1
                task = line.strip().split(", ")
                if linecount == task_select:
                    f.write(
                        f"{task[0]}, {task[1]}, {task[2]}, {task[3]}, {new_due_date}, {task[5]}\n"
                    )
                else:
                    f.write(
                        f"{task[0]}, {task[1]}, {task[2]}, {task[3]}, {task[4]}, {task[5]}\n"
                    )
    return


# Function to generate task overview file
def gen_task_overview():
    with open("tasks.txt", "r") as f:
        lines = f.readlines()
    task_count = len(lines)  # total number of tasks tracked
    for i in range(task_count):  # total number of completed tasks
        completed_tasks = 0
        if "Yes" in lines[i]:
            completed_tasks += 1
    incomplete_tasks = task_count - completed_tasks  # total number of incomplete tasks

    with open("tasks.txt", "r") as f:  # total number of overdue tasks
        linelist = f.readlines()
        overdue_tasks = 0

    with open("tasks.txt", "r") as f:
        for line in linelist:
            task = line.strip().split(", ")
            if (
                task[5] == "No" and task[3] > task[4]
            ):  # if current date after due date, mark as overdue
                overdue_tasks += 1
    percentage_incomplete = (
        incomplete_tasks / task_count
    ) * 100  # percentage of incomplete tasks
    percentage_overdue = (
        overdue_tasks / task_count
    ) * 100  # percentage of overdue tasks

    with open("task_overview.txt", "w") as f:  # Write data to task_overview file
        f.write(f"Total Tasks Tracked:\t {task_count}\n")
        f.write(f"Total Tasks Completed:\t {completed_tasks}\n")
        f.write(f"Total Tasks Incomplete:\t {incomplete_tasks}\n")
        f.write(f"Total Tasks Overdue:\t {overdue_tasks}\n")
        f.write(f"% Tasks Incomplete:\t {percentage_incomplete}%\n")
        f.write(f"% Tasks Overdue:\t {percentage_overdue}%\n")

    # Print data on screen
    print(f"Total Tasks Tracked:\t {task_count}\n")
    print(f"Total Tasks Completed:\t {completed_tasks}\n")
    print(f"Total Tasks Incomplete:\t {incomplete_tasks}\n")
    print(f"Total Tasks Overdue:\t {overdue_tasks}\n")
    print(f"% Tasks Incomplete:\t {percentage_incomplete}%\n")
    print(f"% Tasks Overdue:\t {percentage_overdue}%\n")

    return


# Function to generate user overview file
def gen_user_overview():
    with open("user.txt", "r") as f:
        lines = f.readlines()
    user_count = len(lines)  # total number of users registered

    with open("tasks.txt", "r") as f:
        lines = f.readlines()
    task_count = len(lines)  # total number of tasks tracked

    with open(
        "tasks.txt", "r"
    ) as f:  # create dictionary of users and number of assigned tasks
        lines = f.readlines()
        user_list = [*set([i.split(", ")[0] for i in lines])]  # list of users

    with open(
        "user_overview.txt", "w"
    ) as f:  # create dataset of users and number of assigned tasks
        for i in range(0, len(user_list)):  # for total number of users
            task_num = 0
            task_complete = 0
            task_incomplete = 0
            task_overdue = 0
            task_iterate = 0
            for j in lines:  # for total number of tasks
                task_list = j.strip().split(", ")
                if user_list[i] in task_list[task_iterate]:
                    task_num += 1
                    if "Yes" in task_list[task_iterate]:
                        task_complete += 1
                    elif "No" in task_list[task_iterate]:
                        task_incomplete += 1
                    if "No" in task_list[task_iterate] and task_list[3] > task_list[4]:
                        task_overdue += 1
                task_iterate += 1

            percentage_tasks_assigned = (task_num / task_count) * 100
            percentage_tasks_completed = (
                task_complete / task_count
            ) * 100  # % tasks completed
            percentage_tasks_incomplete = (
                task_incomplete / task_count
            ) * 100  # % tasks incomplete
            percentage_tasks_overdue = (
                task_overdue / task_count
            ) * 100  # % tasks incomplete

        # Write data to user_overview file
        with open("user_overview.txt", "w+") as f:
            f.write(f"Total number of users:\t {user_count}\n")
            f.write(f"Total number of tasks:\t {task_count}\n\n")
            f.write(f"Total number of tasks assigned to user:\t {task_num}\n")
            f.write(
                f"% of total tasks assigned to user:\t\t\t {percentage_tasks_assigned}\n"
            )
            f.write(f"% of tasks completed:\t\t\t\t\t  {percentage_tasks_completed}\n")
            f.write(
                f"% of tasks incomplete:\t\t\t\t\t  {percentage_tasks_incomplete}\n"
            )
            f.write(f"% of tasks overdue:\t\t\t\t\t\t  {percentage_tasks_overdue}\n")

            # Print data
            print(f"Total number of users:\t {user_count}\n")
            print(f"Total number of tasks:\t {task_count}\n\n")
            print(f"Total number of tasks assigned to user:\t {task_num}\n")
            print(
                f"% of total tasks assigned to user:\t\t\t {percentage_tasks_assigned}\n"
            )
            print(f"% of tasks completed:\t\t\t\t\t  {percentage_tasks_completed}\n")
            print(f"% of tasks incomplete:\t\t\t\t\t  {percentage_tasks_incomplete}\n")
            print(f"% of tasks overdue:\t\t\t\t\t\t  {percentage_tasks_overdue}\n")

    return


# ====Login Section====
"""Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
"""
# Fill dictionary with username and password pairs from user.txt
with open("user.txt", "r") as f:
    lines = f.readlines()
    login_data = {}
    for line in lines:
        key, value = line.strip().split(", ")
        login_data[key] = value

# Request username and password and compare against dictionary until true
while True:
    username = input("Please enter a username:")
    password = input("Please enter a password: ")
    if login_data.get(username) == password:
        break
    else:
        print(
            "Username or password failed. Please enter a valid username and password. "
        )

while True:
    if username == "admin":
        # presenting the menu to the user and
        # making sure that the user input is coneverted to lower case.
        menu = input(
            """Select one of the following Options below:
        r - register a user
        a - add a task
        va - view all tasks
        vm - view my tasks
        gr - generate reports
        ds - display statistics
        e - exit
        : """
        ).lower()
    else:
        # presenting the menu to the user and
        # making sure that the user input is coneverted to lower case.
        menu = input(
            """Select one of the following Options below:
        r - register a user
        a - add a task
        va - view all tasks
        vm - view my tasks
        e - exit
        : """
        ).lower()

    if menu == "r":  # register user
        reg_user()
    elif menu == "a":  # add task
        add_task()
    elif menu == "va":  # view all tasks
        view_all()
    elif menu == "vm":  # view user tasks
        view_mine()

    elif username == "admin" and menu == "ds":  # statistics
        with open("user.txt", "r") as f:
            num_users = f.readlines()
        with open("tasks.txt", "r") as f:
            num_tasks = f.readlines()
        print(
            f"\n\nNumber of Users: \t {len(num_users)} \nNumber of Tasks: \t {len(num_tasks)}"
        )

    elif username == "admin" and menu == "gr":  # generate reports
        gen_task_overview()
        gen_user_overview()

    elif menu == "e":  # exit
        print("Goodbye!!!")
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
