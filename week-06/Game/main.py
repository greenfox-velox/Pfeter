from tkinter import *
from gameboard import GameBoard

root = Tk()

canvas_width = 720
canvas_height = 850

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

gameboard = GameBoard()
gameboard.screen_draw(canvas)

def key(event):
    gameboard.keyboard_event_controller(event.keycode, canvas)

root.bind_all('<Key>', key)

root.mainloop()
