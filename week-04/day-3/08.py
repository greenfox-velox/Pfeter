# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

def square_drawing(start_x, start_y):
    square = canvas.create_rectangle(start_x, start_y, start_x + 50, start_y + 50)

square_drawing(10, 10)
square_drawing(10, 100)
square_drawing(100, 10)

root.mainloop()
