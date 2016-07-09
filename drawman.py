from turtle import Turtle
default_scale = 10
default_color = 'black'
default_width = 1

def init_drawman():
    global t,xc,yc
    t = Turtle()
    t.penup()
    xc = 0
    yc = 0
    t.goto(xc,yc)
    t.speed(100)
    t.hideturtle()
    drawman_color(default_color)
    drawman_scale(default_scale)
    drawman_width(default_width)

def drawman_width(width):
    global _drawman_width
    _drawman_width = width
    t.width(width)

def drawman_color(color):
    global _drawman_color
    _drawman_color = color
    t.color(color)

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

def draw_grid():
    xy = 500 // _drawman_scale
    dw = _drawman_width
    dc = _drawman_color
    drawman_width(1)
    for x in range(-xy,xy+1):
        if x != 0:
            drawman_color('grey')
        else:
            drawman_color('black')
        pen_up()
        to_point(x,-xy)
        pen_down()
        on_vector(0,2*xy)
    for y in range(-xy,xy+1):
        if y != 0:
            drawman_color('grey')
        else:
            drawman_color('black')
        pen_up()
        to_point(-xy,y)
        pen_down()
        on_vector(2*xy,0)
    pen_up()
    drawman_width(dw)
    drawman_color(dc)


