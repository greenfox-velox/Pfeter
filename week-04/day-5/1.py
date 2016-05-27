from tkinter import *
import random

root = Tk()

canvas_width = 600
canvas_height = 600

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

def random_color():
    hexs = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
    color = '#'
    for i in range(6):
        color += str(random.choice(hexs))
    return(color)

def triangle(draw_x, draw_y, size):
    canvas.create_polygon(draw_x, draw_y, draw_x+size, draw_y, draw_x+size/2, draw_y+h*size, fill = random_color(), outline = 'black')

def fractal(x,y, size):
    triangle(x,y,size)
    if size <= 10:
        pass
    else:
        fractal(x, y, size/2)
        fractal(x+size/2, y, size/2)
        fractal(x+size/4, y+h*size/2, size/2)

h = (3**0.5)/2
fractal(0, 0, 600)

root.mainloop()
