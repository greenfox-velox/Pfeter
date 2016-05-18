# create a function that returns it's input factorial
def factorial(number):
    summed = 1
    for i in range(number):
        summed *= i + 1
    return(summed)
print(factorial(8))
