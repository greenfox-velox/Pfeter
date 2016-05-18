numbers = [3, 4, 5, 6, 7]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens
def evenser(input_list):
    output_list = []
    for i in input_list:
        if i % 2 != 0:
            output_list.append(i)
    return(output_list)
print(evenser(numbers))
