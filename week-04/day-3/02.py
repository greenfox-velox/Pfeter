# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.
from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

box_x1pos = 20
box_y1pos = 20
box_x2pos = 150
box_y2pos = 150

redLine = canvas.create_line(box_x1pos, box_y1pos, box_x2pos, box_y1pos, fill="red")
greenLine = canvas.create_line(box_x2pos, box_y1pos, box_x2pos, box_y2pos, fill="green")
blueLine = canvas.create_line(box_x2pos, box_y2pos, box_x1pos, box_y2pos, fill="blue")
purpleLine = canvas.create_line(box_x1pos, box_y2pos, box_x1pos, box_y1pos, fill="purple")

root.mainloop()
