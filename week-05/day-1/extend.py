
# Adds a and b, returns as result
def add(a, b):
    return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    else:
        return c

# Returns the median value of a list given as param
def median(pool):
    sorted_pool = sorted(pool)
    if len(pool) % 2 == 0:
        return (sorted_pool[int(len(pool)/2 - 1)] + sorted_pool[int(len(pool)/2)]) / 2
    return pool[int((len(pool) - 1) / 2)]

# Returns true if the param is a vovel
def is_vovel(char):
    return char.lower() in 'aáäeéiíoóöőuúüű'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = str(hungarian)
    teve_out = ''
    for char in range(len(teve)):
        if is_vovel(teve[char]):
            teve_out += (teve[char]+'v'+teve[char])
        else:
            teve_out += teve[char]
    return teve_out
print(translate('alma'))
