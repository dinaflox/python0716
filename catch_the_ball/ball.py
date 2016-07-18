import tkinter
from random import choice, randint
from time import time

ball_inition_number = 10
ball_click_count = 0
click_count = 0
ball_min_radius = 15
ball_max_radius = 40
ball_avaiable_color = ['green','blue','red','yellow','#F0F','black','gray','#0FF']
DX = []
DY = []
Game = True
wg = 500
hg = 500

def click_ball(event):
    """функция обработки события клика мышкой"""
    global label, Game, ball_click_count, click_count
    if Game:
        obj = canvas.find_closest(event.x, event.y)
        x1, y1, x2, y2 = canvas.coords(obj)
        click_count += 1
        if x1 <= event.x <= x2 and y1 <=event.y <= y2:
            canvas.delete(obj)
            ball_click_count += 1
            if ball_click_count == ball_inition_number:
                label['text']='GAME OVER! (точность ' +str((ball_click_count * 10000 // click_count) / 100) + \
                              '%, время: ' + str(round(time() - t)) + 'c.)'
                Game = False
        if Game: label['text']='Всего выстрелов:' + str(click_count) + '. Попаданий: ' + str(ball_click_count)
    else: exit()

def move_all_balls(event):
    """функция движения объектов канвы"""
    for obj in canvas.find_all():
        canvas.move(obj, DX[obj-1], DY[obj-1])
        x1, y1, x2, y2 = canvas.coords(obj)
        if x1 + DX[obj-1] <=0 or x2 + DX[obj-1] >=canvas.winfo_width():
            DX[obj-1] =- DX[obj-1]
        if y1 + DY[obj-1] <=0 or y2 + DY[obj-1] >=canvas.winfo_height():
            DY[obj-1] =- DY[obj-1]

def create_random_ball():
    """функция создания объектов (шариков)
    вместе со списками смещений каждого объекта"""
    R = randint(ball_min_radius, ball_max_radius)
    x = randint(10,int(canvas['width'])-2*R-10)
    y = randint(10,int(canvas['height'])-2*R-10)
    canvas.create_oval(x,y, x+2*R, y+2*R, fill=random_color())
    dx = randint(-2, 2)
    dy = randint(-2, 2)
    while (dx == 0 and dy == 0):
        dx = randint(-2, 2)
        dy = randint(-2, 2)
    DX.append(dx)
    DY.append(dy)

def random_color():
    return choice(ball_avaiable_color)

def init_ball_catch_game():
    for i in range(ball_inition_number):
        create_random_ball()

def init_main_window():
    """функция инициализации игрового поля"""
    global root, canvas, label
    root = tkinter.Tk()
    root.title('Balls')
    root.geometry(str(wg)+'x'+str(hg+20))
    canvas = tkinter.Canvas(root, background="white", width=wg, height=hg)
    canvas.bind('<Button>', click_ball)
    root.bind('<Motion>', move_all_balls)
    canvas.pack(side=tkinter.TOP)
    label = tkinter.Label(root)
    label.pack(side=tkinter.BOTTOM)

if __name__ == "__main__":
    init_main_window()
    init_ball_catch_game()
    t = time()
    root.mainloop()
