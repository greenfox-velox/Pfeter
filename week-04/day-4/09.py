# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def x_change(string):
    if len(string) <= 1:
        return string[0]
    return string[0] + '*' + x_change(string[1:])
print(x_change('asdfxasdfxasdfXXX'))
