from drawman import*
from time import sleep
from math import sin

def f1(x):
    return sin(x)*x

def f2(x):
    return x*x-4*x+2

def f3(x):
    return abs(5*sin(x) / x)


ff = [f1,f2,f3]

def drawing(number_function):
    x = -10
    to_point(x, ff[number_function](x))
    pen_down()
    while x <= 10:
        to_point(x, ff[number_function](x))
        x += 0.1
    pen_up()

drawman_scale(50)
draw_grid()
drawman_width(3)
drawman_color('blue')
drawing(0)
sleep(5)