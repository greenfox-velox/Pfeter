# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

def square_drawing(square_size):
    square = canvas.create_rectangle(canvas_width / 2 - square_size / 2, canvas_height / 2 - square_size / 2, canvas_width / 2 + square_size / 2, canvas_height / 2 + square_size / 2)

square_drawing(10)
square_drawing(20)
square_drawing(30)

root.mainloop()
