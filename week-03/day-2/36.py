numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list
def revers(input_list):
    reversed_list = []
    for i in range(len(input_list)-1, -1, -1):
        reversed_list.append(input_list[i])
    return(reversed_list)
print(revers(numbers))
