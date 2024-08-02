from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")

canvas_widget = Canvas(root, width=canvas_width, height=canvas_height)
root.mainloop() 