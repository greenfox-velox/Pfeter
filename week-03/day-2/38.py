numbers = [7, 5, 8, -1, 2]
# Write a function that returns the minimal element
# in a list (your own min function)
def minimal(input_list):
    output = input_list[0]
    for i in input_list:
        if i < output:
            output = i
    return(output)
print(minimal(numbers))
