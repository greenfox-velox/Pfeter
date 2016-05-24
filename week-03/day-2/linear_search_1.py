# linear_search = ([4,5,6], 6)
# expected output: 2
def linear_search(input_list, target):
    for i in range(0, len(input_list)):
        if input_list[i] == target:
            return(i)
print(linear_search([4,5,6], 6))
