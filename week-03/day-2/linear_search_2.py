# linear_search([4,5,7], 6)
# expected output: -1
def linear_search(input_list, target):
    for i in range(0, len(input_list)):
        if input_list[i] == target:
            return(i)
        elif i == len(input_list) -1:
            return("-1")
print(linear_search([4,5,7], 6))
