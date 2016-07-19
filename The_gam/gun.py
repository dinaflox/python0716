from tkinter import *
from random import choice, randint

screen_width = 500
screen_height = 400
timer_delay = 50
available_colors = ['green', 'blue', 'red','#F0F']

class Ball:
    initial_number = 10
    minimal_radius = 15
    maximal_radius = 40


    def __init__(self, b):
        """
        Cоздаёт шарик в случайном месте игрового холста canvas,
        при этом шарик не выходит за границы холста!
        """
        if b:
            self._R = randint(Ball.minimal_radius, Ball.maximal_radius)
            self._x = randint(0, screen_width-1-2 * self._R)
            self._y = randint(0, screen_height-1-2 * self._R)
            self._color = choice(available_colors)
            self._Vx = randint(-2, +2)
            self._Vy = randint(-2, +2)
            while self._Vx == 0 and self._Vy == 0:
                self._Vx = randint(-2, +2)
                self._Vy = randint(-2, +2)
        else:
            self._x = 0
            self._y = 0
            self._color = 'black'
            self._R = 5
            self._Vx = 2
            self._Vy = -2

        self._avatar1 = canvas.create_oval(self._x, self._y,
                                          self._x + 2 * self._R, self._y + 2 * self._R,
                                          width=1, fill=self._color,
                                          outline=self._color)
        if b: self._avatar2 = canvas.create_arc(self._x + 5, self._y + 5,
                                         self._x + 2 * self._R - 5, self._y + 2 * self._R - 5,
                                         start = 90, extent = 90, style = ARC, outline = 'white')



    def fly(self, b):
        if self._x + self._Vx < 0 or self._x + self._Vx + self._R * 2 > screen_width:
            self._Vx = -self._Vx
        if self._y + self._Vy < 0 or self._y + self._Vy + self._R * 2 > screen_height:
            self._Vy = -self._Vy
        self._x += self._Vx
        self._y += self._Vy
        canvas.coords(self._avatar1, self._x, self._y,
                      self._x + 2*self._R, self._y + 2*self._R)
        if b:canvas.coords(self._avatar2, self._x + 5, self._y + 5,
                                         self._x + 2 * self._R - 5, self._y + 2 * self._R - 5)


class Gun:
    def __init__(self):
        self._x = 0
        self._y = screen_height
        self._lx = +30
        self._ly = -30
        self._avatar = canvas.create_line(self._x, self._y,
                                          self._x+self._lx,
                                          self._y+self._ly, width = 3)

    def shoot(self):
        """
        :return возвращает объект снаряда (класса Ball)
        """
        shell = Ball(False)
        shell._x = self._x + self._lx - shell._R
        shell._y = self._y + self._ly - shell._R
        shell.fly(False)
        return shell


def init_game():
    """
    Создаём необходимое для игры количество объектов-шариков,
    а также объект - пушку.
    """
    global balls, gun, shells_on_fly
    balls = [Ball(True) for i in range(Ball.initial_number)]
    gun = Gun()
    shells_on_fly = []

def init_main_window():
    global root, canvas, scores_text, scores_value
    root = Tk()
    root.title("Пушка")
    scores_value = IntVar()
    canvas = Canvas(root, width=screen_width, height=screen_height,
                    bg="white")
    scores_text = Entry(root, textvariable=scores_value)
    canvas.grid(row=1, column=0, columnspan=3)
    scores_text.grid(row=0, column=2)
    canvas.bind('<Button-1>', click_event_handler)


def timer_event():
    # все периодические рассчёты, которые я хочу, делаю здесь
    for ball in balls:
        ball.fly(True)
    for shell in shells_on_fly:
        shell.fly(False)
    canvas.after(timer_delay, timer_event)


def click_event_handler(event):
    global shells_on_fly
    shell = gun.shoot()
    shells_on_fly.append(shell)


if __name__ == "__main__":
    init_main_window()
    init_game()
    timer_event()
    root.mainloop()