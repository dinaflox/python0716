import tkinter
from random import choice, randint
ball_inition_number = 10
ball_min_radius = 15
ball_max_radius = 40
ball_avaiable_color = ['green','blue','red','yellow','#FF00FF']

def click_ball(event):
    obj = canvas.find_closest(event.x, event.y)
    x1, y1, x2, y2 = canvas.coords(obj)
    if x1 <= event.x <= x2 and y1 <=event.y <= y2:
        canvas.delete(obj)

def move_all_balls(event):
    for obj in canvas.find_all():
        dx = [randint(-1, 1)]
        dy = [randint(-1, 1)]
        canvas.move(obj, dx, dy)

def create_random_ball():
    R = randint(ball_min_radius, ball_max_radius)
    x = randint(1,int(canvas['width'])-2*R-1)
    y = randint(1,int(canvas['height'])-2*R-1)
    canvas.create_oval(x,y, x+2*R, y+2*R, fill=random_color())

def random_color():
    return choice(ball_avaiable_color)

def init_ball_catch_game():
    for i in range(ball_inition_number):
        create_random_ball()


def init_main_window():
    global root, canvas
    root = tkinter.Tk()
    root.title('Balls')
    root.geometry('600x400')
    canvas = tkinter.Canvas(root, background="white", width=400, height=400)
    canvas.bind('<Button>', click_ball)
    root.bind('<Motion>', move_all_balls)
    canvas.pack(side=tkinter.LEFT)


if __name__ == "__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()
