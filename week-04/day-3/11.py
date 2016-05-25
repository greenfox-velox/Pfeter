# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *
import random

root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

def square_drawing(square_size, square_color):
    square = canvas.create_rectangle(canvas_width / 2 - square_size / 2, canvas_height / 2 - square_size / 2, canvas_width / 2 + square_size / 2, canvas_height / 2 + square_size / 2, fill = square_color)

def random_color():
    hexs = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
    color = '#'
    for i in range(6):
        color += str(random.choice(hexs))
    return(color)

drawing_step = 5

for i in range(canvas_width // drawing_step, 0, -1):
    square_drawing(i * drawing_step, random_color())

root.mainloop()
