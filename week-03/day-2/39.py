names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list
def shortest(input_list):
    output = input_list[0]
    for i in input_list:
        if len(i) < len(output):
            output = i
    return(output)
print(shortest(names))
