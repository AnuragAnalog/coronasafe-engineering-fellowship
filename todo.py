#!/usr/bin/python3

import os
import sys

from time import strftime

class Todo():
    def __init__(self):
        self.todo_tasks = list()
        self.done_tasks = list()

        if os.path.isfile('todo.txt'):
            with open('todo.txt', 'r') as self.todo_file:
                for task in self.todo_file:
                    self.todo_tasks.append(task.strip('\n'))

        if os.path.isfile('done.txt'):
            with open('done.txt', 'r') as self.done_file:
                for task in self.done_file:
                    self.done_tasks.append(task.strip('\n'))

    def add_task(self, task_name, error=False):
        if error:
            print("Error: Missing todo string. Nothing added!")
            return

        if not os.path.isfile('todo.txt'):
            self.todo_file = open('todo.txt', 'x')
        else:
            self.todo_file = open('todo.txt', 'a')

        tn = task_name[0]

        self.todo_file.write(tn+'\n')
        self.todo_file.close()

        print("Added todo: \"{}\"".format(tn))
        self.todo_tasks.append(tn)

        return

    def list_tasks(self):
        if len(self.todo_tasks) == 0:
            print("There are no pending todos!")

        for i, task in enumerate(self.todo_tasks[::-1], start=-len(self.todo_tasks)):
            print("[{}] {}".format(abs(i), task))

        return

    def delete_task(self, task_num, error=False):
        if error:
            print("Error: Missing NUMBER for deleting todo.")
            return

        tn = task_num[0]
        if tn not in range(len(self.todo_tasks)):
            print("Error: todo #{} does not exist. Nothing deleted.".format(tn))
            return

        _ = self.todo_tasks.pop(tn-1)

    def done_task(self, task_num, error=False):
        if error:
            print("Error: Missing NUMBER for marking todo as done.")
            return

        tn = task_num[0]
        if tn not in range(len(self.todo_tasks)):
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