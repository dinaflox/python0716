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


if __name__ == "__main__":
    root = Tk()
    root.geometry(str(canvas_width+100)+'x'+str(canvas_height))
    canvas = Canvas(root, width = canvas_width, height = canvas_height)
    canvas.pack(side=LEFT)
    field = Field()
    field.paint()
    root.mainloop()
