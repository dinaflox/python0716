from drawman import*
from time import sleep
from math import sin

def f(x):
    return sin(x)*x

drawman_scale(50)
drawman_width(3)
drawman_color('blue')
draw_grid()
#drawman_color('blue')


x = -10
to_point(x, f(x))
pen_down()
while x <= 10:
    to_point(x, f(x))
    x += 0.1
pen_up()

sleep(5)