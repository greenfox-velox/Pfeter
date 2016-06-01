# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.
def number_of_lines(file_name):
    try:
        lines = 0
        f = open(file_name)
        lines = sum(1 for line in f)
        f.close()
        return lines
    except:
        return 0
