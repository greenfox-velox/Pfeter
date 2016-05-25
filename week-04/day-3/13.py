# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

def line_drawing(start_x, start_y):
    blackLine = canvas.create_line(start_x, start_y, canvas_width / 2, canvas_height / 2)

step = 20

for i in range(canvas_width // step):
    line_drawing(i * step, 0)

for i in range(canvas_height // step):
    line_drawing(canvas_width, i * step)

for i in range(canvas_width // step, 0, -1):
    line_drawing(i * step, canvas_height)

for i in range(canvas_height // step, 0, -1):
    line_drawing(0, i * step)

root.mainloop()
