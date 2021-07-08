import turtle as t
from itertools import cycle
colors = cycle(["red","darkorange","yellow","green","blue","purple"])
from turtle import*
def draw_circle(size, angle, shift):
  t.pencolor(next(colors))
  t.circle(size)
  t.right(angle)
  t.forward (shift)
  draw_circle(size + 5, angle + 1, shift + 1)
t.bgcolor("aqua")
t.speed(10)
t.pensize(40)
t.pencolor("red")
draw_circle(30, 0, 1)



