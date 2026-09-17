from turtle import *
import tkinter as tk

tim = Turtle()


for steps in range(100):
    for c in ('blue', 'red', 'green'):
        tim.color(c)
        tim.forward(steps)
        tim.right(30)

tim.screen.mainloop()

print(tk.Tkversion)