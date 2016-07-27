from tkinter import *

canvas_width = 800
canvas_height = 600
default_cell_size = 10
default_color_life = 'green'
default_color_not_life = 'white'
grid_color = 'lightgray'
begin = False
time_sleep = 50
count_changes = 0

class Field:
    def __init__(self):
        self.cell_size = default_cell_size
        self.color_life = default_color_life
        self.color_not_life = default_color_not_life

    def calc_cell_count(self):
        self.cells_x_count = canvas_width // self.cell_size
        self.cells_y_count = canvas_height // self.cell_size
        self.matrix = [[0] * self.cells_x_count for i in range(self.cells_y_count)]
        self.avatars = [[0] * self.cells_x_count for i in range(self.cells_y_count)]

    def cell_color(self,key):
        colors = {0:self.color_not_life, 1:self.color_life}
        return colors[key]

    def paint(self):
        canvas.delete("all")
        self.calc_cell_count()
        for y in range(self.cells_y_count):
            for x in range(self.cells_x_count):
                self.avatars[y][x] = canvas.create_rectangle(x*self.cell_size, y*self.cell_size,
                                        (x+1)*self.cell_size, (y+1)*self.cell_size,
                                        fill = self.cell_color(self.matrix[y][x]), outline = grid_color)

    def change_cell(self,y,x):
        if self.matrix[y][x] == 0:
            self.matrix[y][x] = 1
        else:
            self.matrix[y][x] = 0
        canvas.delete(self.avatars[y][x])
        self.avatars[y][x] = canvas.create_rectangle(x*self.cell_size, y*self.cell_size,
                                        (x+1)*self.cell_size, (y+1)*self.cell_size,
                                        fill = self.cell_color(self.matrix[y][x]), outline = grid_color)

    def next_population(self):
        global count_changes
        count_changes = 0
        new_matrix = [[0] * self.cells_x_count for i in range(self.cells_y_count)]
        for y in range(1,self.cells_y_count-1):
            for x in range(1,self.cells_x_count-1):
                count_of_neighbours = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        count_of_neighbours += self.matrix[y+i][x+j]
                count_of_neighbours -= self.matrix[y][x]
                if self.matrix[y][x] == 1 and count_of_neighbours == 2 or count_of_neighbours == 3:
                    new_matrix[y][x] = 1
                else:
                    new_matrix[y][x] = 0
        for y in range(1,self.cells_y_count-1):
            for x in range(1,self.cells_x_count-1):
                if new_matrix[y][x] != self.matrix[y][x]:
                    self.change_cell(y,x)
                    count_changes += 1



def new_field():
    label['text']='Ждите...'
    if begin:
        start_or_stop()
    label.update()
    field.cell_size = scale.get()
    field.paint()
    label['text']=''
    label.update()


def mouse_click(event):
    global field
    field.change_cell(event.y // field.cell_size,event.x // field.cell_size)


def start_or_stop():
    global begin
    if begin:
        button_start_or_stop['text']='Старт'
    else:
        button_start_or_stop['text']='Стоп'
    begin = not begin


def init_window():
    global root, label, scale, field, canvas, button_start_or_stop
    root = Tk()
    root.title("Игра \"Жизнь\"")
    ew = root.winfo_screenwidth()
    eh = root.winfo_screenheight()
    w = canvas_width+100
    h = canvas_height
    x = (ew - w) // 2
    y = (eh - h) // 2 - 50
    s = str(w)+'x'+str(h)+'+'+str(x)+'+'+str(y)
    root.geometry(s)
    root.resizable(False,False)
    canvas = Canvas(root, width = canvas_width, height = canvas_height)
    canvas.pack(side=LEFT)
    canvas.bind('<Button-1>', mouse_click)
    scale = Scale(root, from_=5, to=20, orient=HORIZONTAL, length=80)
    scale.place(x = canvas_width+10,y = 10)
    scale.set(default_cell_size)
    button_new_field = Button(root, text='Новые поле', command=new_field)
    button_new_field.place(x = canvas_width+10,y = 50)
    label = Label(root, text='')
    label.place(x = canvas_width+10,y = 80)
    button_start_or_stop = Button(root, text='Старт', width=10, command=start_or_stop)
    button_start_or_stop.place(x = canvas_width+10,y = 120)
    field = Field()
    field.paint()

def time_event():
    if begin:
        field.next_population()
        if count_changes == 0:
            start_or_stop()
    canvas.after(time_sleep,time_event)

if __name__ == "__main__":
    init_window()
    time_event()
    root.mainloop()
