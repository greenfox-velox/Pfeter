# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1, 101):
    printable = ''
    if i % 3 == 0:
        printable += 'Fizz'
    if i % 5 == 0:
        printable += 'Buzz'
    if printable == '':
        printable = i
    print(printable)
