# write a recursive function
# that takes one parameter: n
# and return a list with elements to 1 to n

def concat(n):
    if n <= 0:
        return[]
    else:
        return concat(n-1) + [n]

print(concat(10))
