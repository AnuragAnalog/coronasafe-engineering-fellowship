#!/usr/bin/python3

import os
import sys

from time import strftime

class Todo():
    def __init__(self):
        self.todo_tasks = list()
        self.done_tasks = list()

        if os.path.isfile('todo.txt'):
            self.todo_file = open('todo.txt', 'r+')

            for task in self.todo_file:
                self.todo_tasks.append(task)

        if os.path.isfile('done.txt'):
            self.done_file = open('done.txt', 'r+')

            for task in self.done_file:
                self.done_tasks.append(task)

    def add_task(self, task_name, error=False):
        if error:
            print("Error: Missing todo string. Nothing added!")
            return

        if not os.path.isfile('todo.txt'):
            self.todo_file = open('todo.txt', 'x')

        # tn = task_name[0]
        # self.todo_file.write(tn+'\n')
        # self.todo_tasks.append(tn)

        return

    def list_tasks(self):
        pass

    def delete_task(self, task_num, error=False):
        if error:
            print("Error: Missing NUMBER for deleting todo.")
            return

        tn = task_num[0]
        if len(self.todo_tasks) == 0:
            print("Error: todo #{} does not exist. Nothing deleted.".format(tn))
            return

    def done_task(self, task_num, error=False):
        if error:
            print("Error: Missing NUMBER for marking todo as done.")
            return

        tn = task_num[0]
        if len(self.todo_tasks) == 0:
            print("Error: todo #{} does not exist.".format(tn))
            return

    def help(self):
        print("Usage :-")
        print("$ ./todo add \"todo item\"  # Add a new todo")
        print("$ ./todo ls               # Show remaining todos")
        print("$ ./todo del NUMBER       # Delete a todo")
        print("$ ./todo done NUMBER      # Complete a todo")
        print("$ ./todo help             # Show usage")
        print("$ ./todo report           # Statistics")

        return

    def report(self):
        now_date = strftime("%Y-%m-%d")

        print("{} Pending : {} Completed : {}".format(now_date, len(self.todo_tasks), len(self.done_tasks)))

        return

if __name__ == "__main__":
    todo = Todo()

    n = len(sys.argv)
    add_del_done_error = False

    if n == 1:
        todo.help()
    elif n > 1:
        arg = sys.argv[2:]
        if n == 2:
            add_del_done_error = True
        
        if sys.argv[1] == "help":
            todo.help()
        elif sys.argv[1] == "ls":
            todo.list_tasks()
        elif sys.argv[1] == "report":
            todo.report()
        elif sys.argv[1] == "add":
            todo.add_task(arg, error=add_del_done_error)
        elif sys.argv[1] == "del":
            todo.delete_task(arg, error=add_del_done_error)
        elif sys.argv[1] == "done":
            todo.done_task(arg, error=add_del_done_error)
        else:
            pass