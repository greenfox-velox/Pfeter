# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

def line_drawing(start_x, start_y):
    blackLine = canvas.create_line(start_x, start_y, canvas_width / 2, canvas_height / 2)

line_drawing(10, 10)
line_drawing(10, 100)
line_drawing(100, 10)

root.mainloop()
