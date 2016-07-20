from tkinter import *
from random import choice, randint
from math import cos, sin, atan, pi, sqrt
from time import time

screen_width = 500
screen_height = 400
timer_delay = 50
available_colors = ['green', 'blue', 'red','#F0F']
gun_len = 40
shoot_count = 0
very_count = 0
game = True
shoot_speed = 6

def mess():
    if game:
        label['text'] = 'Выстрелов: ' + str(shoot_count) + '. Попаданий: ' + str(very_count) + '.'
    else:
        label['text'] = 'GAME OVER!  (точность: ' + str(round(very_count * 100 / shoot_count, 2)) + \
                        ' %, время: ' + str(round(time() - t)) + ' c.)'

class Ball:
    initial_number = 10
    minimal_radius = 15
    maximal_radius = 40

    def __init__(self, b):
        """
        Cоздаёт шарик  в случайном месте игрового холста canvas,
        при этом шарик не выходит за границы холста
        ну или снаряд (при b == False)
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
            self._v = shoot_speed
            self._Vx = self._v * cos(pi / 4)
            self._Vy = -self._v * sin(pi / 4)

        self._b = b
        self._avatar1 = canvas.create_oval(self._x, self._y,
                                          self._x + 2 * self._R, self._y + 2 * self._R,
                                          width=1, fill=self._color,
                                          outline=self._color)
        if b: self._avatar2 = canvas.create_arc(self._x + 5, self._y + 5,
                                         self._x + 2 * self._R - 5, self._y + 2 * self._R - 5,
                                         start = 90, extent = 90, style = ARC, outline = 'white')


    def fly(self):
        global very_count, game
        if self._b:
            if self._x + self._Vx < 0 or self._x + self._Vx + self._R * 2 > screen_width:
                self._Vx = -self._Vx
            if self._y + self._Vy < 0 or self._y + self._Vy + self._R * 2 > screen_height:
                self._Vy = -self._Vy
        else:
            if self._x + self._Vx + self._R * 2 > screen_width or self._y + self._Vy < 0 or self._y + self._Vy + self._R * 2 > screen_height:
                canvas.delete(self._avatar1)
                shells_on_fly.remove(self)
                return
            for ball in balls:
                xo = ball._x + ball._R
                yo = ball._y + ball._R
                if sqrt((self._x - xo)**2 + (self._y - yo)**2) <= self._R + ball._R:
                    canvas.delete(ball._avatar2)
                    canvas.delete(ball._avatar1)
                    balls.remove(ball)
                    canvas.delete(self._avatar1)
                    shells_on_fly.remove(self)  # FIXME
                    very_count += 1
                    if len(balls) == 0:
                        game = False
                        canvas.delete("all")
                        shells_on_fly.clear()
                    mess()
                    return
            self._Vy += 0.05
        self._x += self._Vx
        self._y += self._Vy
        canvas.coords(self._avatar1, self._x, self._y,
                      self._x + 2*self._R, self._y + 2*self._R)
        if self._b:canvas.coords(self._avatar2, self._x + 5, self._y + 5,
                                         self._x + 2 * self._R - 5, self._y + 2 * self._R - 5)


class Gun:
    def __init__(self):
        self._x = 0
        self._y = screen_height
        self._l = gun_len
        self._a = pi / 4
        self._lx = self._x + self._l * cos(self._a)
        self._ly = self._y - self._l * sin(self._a)
        self._avatar = canvas.create_line(self._x, self._y,
                                          self._lx, self._ly, width = 3)

    def shoot(self):
        """
        получаем снаряд, запускаем его и возращаем для запоминания в список снарядов
        """
        global shoot_count
        shell = Ball(False)
        shoot_count += 1
        mess()
        shell._x = self._lx - shell._R
        shell._y = self._ly - shell._R
        shell.fly()
        return shell

    def moves(self,dx,dy):
        """
        расчет координат рисования пушки
        """
        if dx == 0:
            self._a = pi / 2
        else:
            self._a = atan(dy / dx)
        self._lx = self._x + self._l * cos(self._a)
        self._ly = self._y - self._l * sin(self._a)
        canvas.coords(self._avatar, self._x, self._y,
                                          self._lx, self._ly)

def gun_move(event):
    """
    Движение пушки за мышкой
    """
    if game: gun.moves(event.x, screen_height - event.y)

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
    """
    инициализация экрана
    """
    global root, canvas, label
    root = Tk()
    root.title("Пушка")
    root.geometry(str(screen_width)+'x'+str(screen_height+20))
    canvas = Canvas(root, width=screen_width, height=screen_height, bg="white")
    canvas.bind('<Button-1>', click_event_handler)
    canvas.bind('<Motion>', gun_move)
    canvas.pack(side=TOP)
    label = Label(root)
    label['text'] = 'Надо лопнуть все шары. Клик - выстрел...'
    label.pack(side=BOTTOM)

def timer_event():
    # таймер: гоняет шары и снаряды
    if game:
        for ball in balls:
            ball.fly()
        for shell in shells_on_fly:
            shell.fly()
        canvas.after(timer_delay, timer_event)

def click_event_handler(event):
    """
    добавляем по клику новый снаряд, рассчитываем, куда он полетит
    """
    global shells_on_fly
    if game:
        shell = gun.shoot()
        shell._Vx = shell._v * cos(gun._a)
        shell._Vy = -shell._v * sin(gun._a)
        shells_on_fly.append(shell)

if __name__ == "__main__":
    init_main_window()
    init_game()
    t = time()
    timer_event()
    root.mainloop()