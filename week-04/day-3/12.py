# create a 300x300 canvas.
# fill it with a checkerboard pattern.

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

square_size = 10

for i in range(canvas_width // square_size):
    for j in range(1, canvas_height // square_size):
        if (i + j) % 2:
            square_color = 'black'
        else:
            square_color = 'white'
        canvas.create_rectangle(i * square_size, j * square_size, i * square_size + square_size, j * square_size + square_size, fill = square_color)

root.mainloop()
