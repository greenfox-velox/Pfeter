# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n

def count_up(n):
    if n <= 0:
        return n
    else:
        return count_up(n-1) + n

print(count_up(5))
