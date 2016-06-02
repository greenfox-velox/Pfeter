import sys
import os

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
    f = open(file_name)
    for line in f:
        output.append(line.rstrip())
    f.close()
    return output

def list_todos(file_name):
    todos = read_todos(file_name)
    if len(todos) > 0:
        for i in range(len(todos)):
            print(i + 1,'-', todos[i])
    else:
        print('No todos for today! :)')

def append_todos(file_name, new_todo):
    f = open(file_name, 'a')
    f.write(new_todo + '\n')
    f.close()

def add_new_controller(file_name):
    if len(sys.argv) == 3:
        append_todos(file_name, sys.argv[2])
    else:
        print('Unable to add: No task is provided')

def remove_todo(file_name, todo_to_remove):
    output = read_todos(file_name)
    output.pop(int(todo_to_remove) - 1)
    f = open(file_name, 'w')
    for i in range(len(output)):
        f.write(output[i] + '\n')
    f.close()

def remove_controller(file_name):
    if len(sys.argv) < 3:
        print('Unable to remove: No index is provided')
    elif not sys.argv[2].isdigit():
        print('Unable to remove: Index is not a number')
    elif len(read_todos(file_name)) >= int(sys.argv[2]):
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
        is_file_missing('todos.txt')
        if sys.argv[1] == '-l':
            list_todos('todos.txt')
        elif sys.argv[1] == '-a':
            add_new_controller('todos.txt')
        elif sys.argv[1] == '-r':
            remove_controller('todos.txt')
        else:
            print('Unsupported argument')
            usage_information()

main()
