from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

def square_drawing(start_x, start_y, size):
    square = canvas.create_rectangle(start_x, start_y, start_x + size, start_y + size, fill = "purple")

square_size = 10
sum = 10
for i in range(6):
    square_drawing(sum , sum , square_size + square_size * i)
    sum += square_size + i * square_size

root.mainloop()
