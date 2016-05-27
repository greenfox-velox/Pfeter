from tkinter import *
import random

root = Tk()

h = (3**0.5)/2
size = 300

canvas_width = 2*size
canvas_height = 2*h*size

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

def random_color():
    hexs = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
    color = '#'
    for i in range(6):
        color += str(random.choice(hexs))
    return(color)

def hexagon(x, y, size):
    canvas.create_polygon(x, y, x+size, y, x+1.5*size, y+h*size, x+size, y+2*h*size, x, y+2*h*size, x-0.5*size, y+h*size, fill = random_color(), outline = 'black')

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
