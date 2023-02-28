# create a empty list for the tasks
tasks = []

# function to create a task


def create_task(task):
    tasks.append(task)
    print("Your task has been created: ", task)

# function to delete a task


def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Your task has been deleted: ", task)
    else:
        print("The task you entered cannot be deleted")

# function to complete the task


def complete_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Your task has been completed: ", task)
    else:
        print("No tasks found.")

# function to view the tasks


def view_tasks():
    print("Tasks: ")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")


# main loop to run the tasks


def main_loop():
    while (True):
        print("""
        To-Do List
        1. Add Task
        2. Delete Task
        3. Complete Task
        4. View Tasks
        5. Exit
        """)

        choice = int(input("Enter your choice:"))

        if choice == 1:
            task = input("Enter a task: ")
            create_task(task)
        elif choice == 2:
            task = input("Task to be deleted: ")
            delete_task(task)
        elif choice == 3:
            task = input("Task to complete: ")
            complete_task(task)
        elif choice == 4:
            view_tasks()
        elif choice == 5:
            break
        else:
            print("Please provide valid parameters.")


if __name__ == "__main__":
    main_loop()
