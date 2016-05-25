# reproduce this: [image link]
# can you make the colors change? make every line a different color.

from tkinter import *
import random

root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

def line_drawing(start_x, start_y, end_x, end_y, color):
    blackLine = canvas.create_line(start_x, start_y, end_x, end_y, fill=color)

def random_color():
    hexs = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
    color = '#'
    for i in range(6):
        color += str(random.choice(hexs))
    return(color)

step = 10

for i in range(150 // step):
    line_drawing(150, i * step, 150 - i * step, 150, random_color())
for i in range(150 // step):
    line_drawing(150, i * step, 150 + i * step, 150, random_color())
for i in range(150 // step):
    line_drawing(150 + i * step, 150, 150, 300 - i * step, random_color())
for i in range(150 // step):
    line_drawing(150 - i * step, 150, 150, 300 - i * step, random_color())

root.mainloop()
