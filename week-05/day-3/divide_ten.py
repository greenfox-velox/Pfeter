# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0

def divide_ten(number):
    try:
        return 10 / number
    except ZeroDivisionError:
        return 'fail'

print(divide_ten(2))
