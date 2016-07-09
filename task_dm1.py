from drawman import*
from time import sleep
from math import sin

def f(x):
    return sin(x)

drawman_scale(50)
draw_grid()
drawman_color('red')
drawman_width(3)
x = -5
to_point(x, f(x))
pen_down()
while x <= 5:
    to_point(x, f(x))
    x += 0.1
pen_up()

sleep(5)