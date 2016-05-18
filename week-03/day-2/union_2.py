# union([4,5,7], [4,1,7])
# expected output: [1,4,5,7]
def union(input_list, input_list_2):
    sum_list = input_list + input_list_2
    output = []
    for n in range(0, len(sum_list)):
        minelement = sum_list[0]
        for i in sum_list:
            if i < minelement:
                minelement = i
        if len(output) == 0 or output[len(output) - 1] != minelement:
            output.append(minelement)
        sum_list.remove(minelement)
    return(output)
print(union([4,5,7], [4,1,7]))
