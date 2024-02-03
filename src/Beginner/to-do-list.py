### To-Do List ###
# This program allows users to store and manage a list of tasks
# Users can add, remove, and view tasks

import os

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    else:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks, task):
    tasks.append(task)
    return tasks

def remove_task(tasks, task):
    tasks.remove(task)
    return tasks

def view_tasks(tasks):
    print("Tasks:")
    for task in tasks:
        print(task)

def main():
    todo_list = load_tasks()
    while True:
        print("To-Do List Actions: \n")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Exit")

        action = input("\nEnter the number of the action: \n")
        
        if action == "1":
            task = input("\nEnter the name of the task you want to add: \n")
            todo_list = add_task(todo_list, task)
            save_tasks(todo_list)

        elif action == "2":
            task = input("\nEnter the name of the task you want to remove: \n")
            try: 
                todo_list = remove_task(todo_list, task.lower())
                save_tasks(todo_list)
            except: 
                print("\n[ERROR] Task not found, please enter a valid task! \n")

        elif action == "3":
            view_tasks(todo_list)
            exit = input("\nPress any key and enter to go back to the main menu. \n")
            if exit:
                continue

        elif action == "4":
            break

        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main() 