from tkinter import *

root = Tk()

canvas_width = 600
canvas_height = 600

canvas = Canvas(root, width = canvas_width, height = canvas_height, bg = 'yellow')
canvas.pack()

def hashmark(draw_x, draw_y, size):
    canvas.create_line(draw_x, draw_y+size/3, draw_x+size, draw_y+size/3)
    canvas.create_line(draw_x, draw_y+size/3*2, draw_x+size, draw_y+size/3*2)
    canvas.create_line(draw_x+size/3, draw_y, draw_x+size/3, draw_y+size)
    canvas.create_line(draw_x+size/3*2, draw_y, draw_x+size/3*2, draw_y+size)
    if size < 5:
        pass
    else:
        hashmark(draw_x+size/3, draw_y, size/3)
        hashmark(draw_x, draw_y+size/3, size/3)
        hashmark(draw_x+size/3, draw_y+size/3*2, size/3)
        hashmark(draw_x+size/3*2, draw_y+size/3, size/3)

hashmark(0,0,600)

root.mainloop()
