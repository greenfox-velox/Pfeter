import sys
import os
import csv

def usage_information():
    print('Python Todo application')
    print('=======================')
    print('')
    print('Command line arguments:')
    print(' -l   Lists all the tasks')
    print(' -a   Adds a new task')
    print(' -r   Removes a task')
    print(' -c   Completes a task')

def read_todos(file_name):
    output = []
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            output.append(line)
    csvfile.close()
    return output

def list_todos(file_name):
    todos = read_todos(file_name)
    if len(todos) > 0:
        for i in range(len(todos)):
            todo = ""
            if todos[i].get('is_checked') == 'True':
                todo += '[X] '
            else:
                todo += '[ ] '
            todo += todos[i].get('task_string')
            print(i + 1,'-', todo)
    else:
        print('No todos for today! :)')

def append_todos(file_name, new_todo):
    with open(file_name, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['task_string', 'is_checked'])
        writer.writerow({'task_string': new_todo, 'is_checked': 'False'})
    csvfile.close()

def add_new_todo_controller(file_name):
    if len(sys.argv) == 3:
        append_todos(file_name, sys.argv[2])
    else:
        print('Unable to add: No task is provided')

def remove_todo(file_name, todo_to_remove):
    output = read_todos(file_name)
    output.pop(int(todo_to_remove) - 1)
    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['task_string', 'is_checked'])
        writer.writerow({'task_string': 'task_string', 'is_checked': 'is_checked'})
        for i in range(len(output)):
            writer.writerow(output[i])
    csvfile.close()

def remove_todo_controller(file_name):
    if len(sys.argv) < 3:
        print('Unable to remove: No index is provided')
    elif not sys.argv[2].isdigit():
        print('Unable to remove: Index is not a number')
    elif (len(read_todos(file_name)) >= int(sys.argv[2])) and (int(sys.argv[2]) > 0):
        remove_todo(file_name, sys.argv[2])
    else:
        print('Unable to remove: Index is out of bound')

def is_file_missing(file_name):
    if not os.path.exists(file_name):
        f = open(file_name, 'w')
        f.close()

def main():
    if len(sys.argv) == 1:
        usage_information()
    else:
        is_file_missing('todos.csv')
        if sys.argv[1] == '-l':
            list_todos('todos.csv')
        elif sys.argv[1] == '-a':
            add_new_todo_controller('todos.csv')
        elif sys.argv[1] == '-r':
            remove_todo_controller('todos.csv')
        else:
            print('Unsupported argument')
            usage_information()

main()
