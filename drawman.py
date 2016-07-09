from turtle import Turtle

def init_drawmen():
    global t,xc,yc
    t = Turtle()
    t.penup()
    xc = 0
    yc = 0
    t.goto(xc,yc)

def pen_up():
    t.penup()

def pen_down():
    t.pendown()

def to_point(x,y):
    global xc,yc
    xc = x
    yc = y
    t.goto(xc,yc)

def on_vector(dx,dy):
    global xc,yc
    xc += dx
    yc += dy
    t.goto(xc,yc)

init_drawmen()

