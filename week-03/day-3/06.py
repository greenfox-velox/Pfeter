# create a function that takes a list and returns a new list that is reversed
def revers(input_list):
    reversed_list = []
    for i in range(len(input_list)-1, -1, -1):
        reversed_list.append(input_list[i])
    return(reversed_list)

print(revers([3, 4, 5, 6, 7]))

def revers_pop(input_list):
    reversed_list = []
    for i in range(0, len(input_list)):
        reversed_list.append(input_list.pop())
    return(reversed_list)

print(revers_pop([3, 4, 5, 6, 7]))
