# reproduce this: [image link]
# divide the canvas into 4 parts and repeat the pattern.

from tkinter import *
import random

root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

def line_drawing(start_x, start_y, end_x, end_y, color):
    blackLine = canvas.create_line(start_x, start_y, end_x, end_y, fill=color)

def figure_drawing(canvas_start_x, canvas_start_y, canvas_end_x, canvas_end_y):
    step = 10
    for i in range((canvas_end_x - canvas_start_x) // step):
        line_drawing(canvas_start_x, canvas_start_y + i * step, canvas_start_x + step + i * step, canvas_end_y, 'green')
    for i in range((canvas_end_y - canvas_start_y) // step):
        line_drawing(canvas_start_x + i * step, canvas_start_y, canvas_end_x, canvas_start_y + step + i * step, 'purple')

figure_drawing(0, 0, canvas_width // 2, canvas_height // 2)
figure_drawing(canvas_width // 2, 0, canvas_width, canvas_height // 2)
figure_drawing(canvas_width // 2, canvas_height // 2, canvas_width, canvas_height)
figure_drawing(0, canvas_height // 2, canvas_width // 2, canvas_height)

root.mainloop()
