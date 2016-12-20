#Cesar Neri
#December 19, 2016

#Excercise 16-1 from Murach's Python Programming Book

#Implements a basic interface for the task manager porogram



#!/usr/bin/env python3

from business import Task, TaskList, TaskManager 

#Displays basic commands to the user
def display_commands():
    print("COMMAND MENU")
    print("list     - List all tasks",
          "add      - Add a new task",
          "complete - Complete task",
          "delete   - delet a task",
          "exit     - Close program", sep="\n")
    print()

#Displays the avilable lists to chose from
def print_lists(manager):
    print ("TASK LISTS")

    i = 0
    for tList in manager:
        i += 1
        print (str(i) + ". " + tList.name)

    print()

#Returns a list to work on, chosen by user input
def get_list(manager):
    while True:
        listNumber = input("Enter the number to select task list:\t")
        if not listNumber.isdigit():
            print("Enter a valid integer")
            continue
        else:
            listNumber = int(listNumber)

            if listNumber < 1 or listNumber > manager.count:
                print("Enter a valid list number.")
                continue
            
            return manager.getList(listNumber-1)

#Addds a user entered task to the specified list
def add_task(tList):
    desc = input("Description:\t")
    task = Task(desc)
    tList.addTask(task)

#deletes user specified task from specified list
def del_task(tList):
    while True:
        taskNumber = input("Number:\t")
        if not taskNumber.isdigit():
            print("Enter a valid integer")
            continue
        else:
            taskNumber = int(taskNumber)

            if taskNumber <= 0 or taskNumber > tList.qty:
                print("Enter a valid list number.")
                continue
            
            tList.delTask(taskNumber-1)
            break

#Marks a task chosen by user as completed, from specified list
def comp_task(tList):
    while True:
        taskNumber = input("Number:\t")
        if not taskNumber.isdigit():
            print("Enter a valid integer")
            continue
        else:
            taskNumber = int(taskNumber)

            if taskNumber <= 0 or taskNumber > tList.qty:
                print("Enter a valid list number.")
                continue
            
            tList.toggleTask(taskNumber-1)
            break


def main():

    #initialize 2 Task Lists
    l1 = TaskList("Personal")
    l2 = TaskList("Business")

    #create task manager and add to lists
    tManager = TaskManager()
    tManager.addList(l1)
    tManager.addList(l2)
    
    #print commands
    display_commands()

    #print name of lists
    print_lists(tManager)

    #get the list to work on
    task_list = get_list(tManager)

    while True:

        command = input("Command:\t")
        print()

        if command == "list":
            print(task_list)
        elif command == "add":
            add_task(task_list)
        elif command == "delete":
            del_task(task_list)
        elif command == "complete":
            comp_task(task_list)
        elif command == "exit":
            break
        else:
            print("Please enter a valid command.")

    print("Goodbye!")

#Only call main if it is the main module
if __name__ == "__main__":
    main()
        
    
        
        
        
    
    
    
