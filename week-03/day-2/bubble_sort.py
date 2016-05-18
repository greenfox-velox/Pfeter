# bubble_sort([3,9,4,5,2,1])
# expected output: [1,2,3,4,5,9]
def bubble_sort(input_list):
    container = ''
    for i in range(0, len(input_list)):
        for u in range(0, len(input_list) - 1):
            if input_list[u] > input_list[u + 1]:
                container = input_list[u + 1]
                input_list[u + 1] = input_list[u]
                input_list[u] = container
    return(input_list)
print(bubble_sort([3,9,4,5,2,1]))
