from turtle import Turtle
default_scale = 10

def init_drawman():
    global t,xc,yc,_drawman_scale
    t = Turtle()
    t.penup()
    xc = 0
    yc = 0
    t.goto(xc,yc)
    drawman_scale(default_scale)

def drawman_scale(scale):
    global _drawman_scale
    _drawman_scale = scale

def pen_up():
    t.penup()

def pen_down():
    t.pendown()

def to_point(x,y):
    global xc,yc
    xc = x
    yc = y
    t.goto(_drawman_scale*xc,_drawman_scale*yc)

def on_vector(dx,dy):
    to_point(xc+dx,yc+dy)

init_drawman()

