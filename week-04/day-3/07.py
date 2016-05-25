# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

greenBox = canvas.create_rectangle(0, 0, canvas_width / 2, canvas_height / 2, fill="green")
redBox = canvas.create_rectangle(canvas_width / 2, 0, canvas_width, canvas_height / 2, fill="red")
blueBox = canvas.create_rectangle(0, canvas_height / 2, canvas_width / 2, canvas_height, fill="blue")
purpleBox = canvas.create_rectangle(canvas_width / 2, canvas_height / 2, canvas_width, canvas_height, fill="purple")

root.mainloop()
