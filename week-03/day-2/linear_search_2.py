# linear_search([4,5,7], 6)
# expected output: -1
def linear_search(input_list, target):
    output = 0
    for i in input_list:
        if i == target:
            return(output)
        elif output == len(input_list) -1:
            return("-1")
        else:
            output += 1
print(linear_search([4,5,7], 6))
