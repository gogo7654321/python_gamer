import turtle as t
from itertools import cycle
colors = cycle(["red","orange","yellow","green","blue","purple"])
from turtle import*
def draw_circle(size, angle, shift):
  t.pencolor(next(colors))
  t.circle(size)
  t.right(angle)
  t.forward (shift)
  draw_circle(size + 5, angle + 1, shift + 1)
t.bgcolor("aqua")
t.speed(70)
t.pensize(30)
t.pencolor("orange")
draw_circle(30, 0, 1)



