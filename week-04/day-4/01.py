# 1. write a recursive function
# that takes one parameter: n
# and counts down from n

def count_down(n):
    print(n)
    if n <= 0:
        return 0
    else:
        return count_down(n-1)

count_down(6)
