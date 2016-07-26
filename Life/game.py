from tkinter import *

canvas_width = 800
canvas_height = 600
default_cell_size = 10
default_color_life = 'green'
default_color_not_life = 'white'
grid_color = 'lightgray'

class Field:
    def __init__(self):
        self.cell_size = default_cell_size
        self.color_life = default_color_life
        self.color_not_life = default_color_not_life

    def calc_cell_count(self):
        self.cells_x_count = canvas_width // self.cell_size
        self.cells_y_count = canvas_height // self.cell_size
        self.matrix = [[0] * self.cells_x_count for i in range(self.cells_y_count)]

    def cell_color(self,key):
        colors = {0:self.color_not_life, 1:self.color_life}
        return colors[key]

    def paint(self):
        for y in range(self.cells_y_count):
            for x in range(self.cells_x_count):
                canvas.create_rectangle(x*self.cell_size, y*self.cell_size,
                                        (x+1)*self.cell_size, (y+1)*self.cell_size,
                                        fill = self.cell_color(self.matrix[y][x]), outline = grid_color)

def new_field():
    canvas.delete("all")
    field.cell_size = scale.get()
    field.calc_cell_count()
    field.paint()

    scale.set(field.cell_size)


if __name__ == "__main__":
    root = Tk()
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
    scale = Scale(root, from_=2, to=20, orient=HORIZONTAL, length=80)
    scale.place(x = canvas_width+10,y = 10)
    scale.set(default_cell_size)
    button = Button(root, text='Новые поле', command=new_field)
    button.place(x = canvas_width+10,y = 50)
    field = Field()
    field.calc_cell_count()
    field.paint()
    root.mainloop()
