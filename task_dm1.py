from drawman import*
from time import sleep

def f(x):
    return x*x

to_point(-10,f(-10))
pen_down()
for x in range(-10,11):
    to_point(x,f(x))
pen_up()

sleep(5)