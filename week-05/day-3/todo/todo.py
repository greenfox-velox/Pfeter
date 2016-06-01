import sys

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
    for i in range(len(todos)):
        print(i + 1,'-', todos[i])

def main():
    if len(sys.argv) == 1:
        usage_information()
    elif sys.argv[1] == '-l':
        list_todos('todos.txt')

main()
