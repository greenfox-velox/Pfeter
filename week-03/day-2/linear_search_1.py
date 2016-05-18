# linear_search = ([4,5,6], 6)
# expected output: 2
def linear_search(input_list, target):
    output = 0
    for i in input_list:
        if i == target:
            return(output)
        output += 1
print(linear_search([4,5,6], 6))
