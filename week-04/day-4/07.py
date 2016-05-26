# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def x_change(string):
    if len(string) <= 1:
        return string[0]
    elif string[0] == 'x':
        string = 'y' + string[1:]
    return string[0] + x_change(string[1:])
print(x_change('asdfxasdfxasdfXXX'))
