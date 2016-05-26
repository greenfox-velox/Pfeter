# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

def x_change(string):
    if len(string) <= 1:
        return string[0]
    elif string[0] == 'x':
        string = string[1:]
    return string[0] + x_change(string[1:])
print(x_change('asdfxasdfxasdfXXX'))
