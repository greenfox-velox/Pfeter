# create a 300x300 black canvas.
# draw a red horizontal line to its middle.
# draw a green vertical line to its middle.
from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

redLine = canvas.create_line(0, canvas_height / 2, canvas_width, canvas_height / 2, fill="red")
greenLine = canvas.create_line(canvas_width / 2, 0, canvas_width / 2, canvas_height, fill="green")

root.mainloop()
