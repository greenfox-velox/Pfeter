# Create a function that prints a triangle like this:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has
def draw_triangle(how_many_lines):
    for i in range(0,how_many_lines):
        print((i + 1) * '*')
draw_triangle(6)
