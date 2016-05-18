numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function
def sum(numbers_list):
    summed = 0
    for i in numbers_list:
        summed += i
    return(summed)
print(sum(numbers))
