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

def print_list_todos(todos):
    for i in range(len(todos)):
        todo = ''
        if todos[i].get('is_checked') == 'True':
            todo += '[X] '
        else:
            todo += '[ ] '
        todo += todos[i].get('task_string')
        print(i + 1,'-', todo)

def append_todos(file_name, new_todo):
    output = read_todos(file_name)
    output.append({'task_string': new_todo, 'is_checked': 'False'})
    write_todos(file_name, output)

def remove_todo(file_name, todo_to_remove):
    output = read_todos(file_name)
    output.pop(todo_to_remove - 1)
    write_todos(file_name, output)

def check_task(file_name, todo_to_check):
    output = read_todos(file_name)
    output[todo_to_check - 1]['is_checked'] = 'True'
    write_todos(file_name, output)

def write_todos(file_name, input_todo_list):
    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['task_string', 'is_checked'])
        writer.writerow({'task_string': 'task_string', 'is_checked': 'is_checked'})
        for i in range(len(input_todo_list)):
            writer.writerow(input_todo_list[i])
    csvfile.close()

def is_file_missing(file_name):
    if not os.path.exists(file_name):
        write_todos(file_name, [])

def main_controller(what_do, what_provide):
    file_name = 'todos.csv'
    is_file_missing(file_name)
    if what_do == 'list':
        todos = read_todos(file_name)
        if len(todos) > 0:
            print_list_todos(todos)
        else:
            print('No todos for today! :)')
    elif len(sys.argv) < 3:
        print('Unable to ' + what_do + ': No '+ what_provide + ' is provided')
    elif what_do == 'add':
        append_todos(file_name, sys.argv[2])
    elif not sys.argv[2].isdigit():
        print('Unable to ' + what_do + ': Index is not a number')
    elif (len(read_todos(file_name)) >= int(sys.argv[2])) and (int(sys.argv[2]) > 0):
        if what_do == 'remove':
            remove_todo(file_name, int(sys.argv[2]))
        elif what_do == 'check':
            check_task(file_name, int(sys.argv[2]))
    else:
        print('Unable to ' + what_do + ': Index is out of bound')

def main():
    if len(sys.argv) == 1:
        usage_information()
    else:
        if sys.argv[1] == '-l':
            main_controller('list','')
        elif sys.argv[1] == '-a':
            main_controller('add', 'task')
        elif sys.argv[1] == '-r':
            main_controller('remove', 'index')
        elif sys.argv[1] == '-c':
            main_controller('check', 'index')
        else:
            print('Unsupported argument')
            usage_information()

main()
