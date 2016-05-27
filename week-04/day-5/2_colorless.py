from tkinter import *
import random

root = Tk()

h = (3 ** 0.5) / 2
size = 300

canvas_width = 2 * size + 20
canvas_height = 2 * h * size + 20

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

def hexagon(x, y, size):
    canvas.create_polygon(x, y, x+size, y, x+1.5*size, y+h*size, x+size, y+2*h*size, x, y+2*h*size, x-0.5*size, y+h*size, fill = 'white', outline = 'black')

def fractal(x,y, size):
    hexagon(x,y,size)
    if size <= 10:
        pass
    else:
        fractal(x, y, size/3)
        fractal(x+size*2/3, y, size/3)
        fractal(x+size, y+h*size*2/3, size/3)
        fractal(x+size*2/3, y+h*size*4/3, size/3)
        fractal(x, y+h*size*4/3, size/3)
        fractal(x-size*1/3, y+h*size*2/3, size/3)

fractal(0.5*size, 0, size)

root.mainloop()
