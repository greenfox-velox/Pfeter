from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

def square_drawing(start_x, start_y):
    square = canvas.create_rectangle(start_x, start_y, start_x + 10, start_y + 10, fill = "purple")

for i in range(19):
    square_drawing(10 + 10 * i, 10 + 10 * i)

root.mainloop()
