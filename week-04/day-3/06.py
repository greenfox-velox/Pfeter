# create a 300x300 canvas.
# draw a green 10x10 square to its center.

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

greenBoxSize = 10

greenBox = canvas.create_rectangle(canvas_width / 2 - greenBoxSize / 2, canvas_height / 2 - greenBoxSize / 2, canvas_width / 2 + greenBoxSize / 2, canvas_height / 2 + greenBoxSize / 2, fill="green")

root.mainloop()
