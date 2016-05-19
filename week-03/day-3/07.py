# create a function that takes a list and returns a new list with all the elements doubled
def double(input_list):
    for list_element in range(0, len(input_list)):
        input_list[list_element] *= 2
    print(input_list)

double([3, 4, 5, 6, 7])
