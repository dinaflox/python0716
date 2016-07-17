import tkinter


def print_b1():
    button1['text'] = 'djn'


def print_hello(event):
    print(dir(event))
    me = event.widget
    if me == button1:
        print('Hello!')
    elif me == button2:
        print('You pressed button2')
    else:
        raise ValueError()


def init_main_window():
    global root, button1,button2,label,text,scale
    root = tkinter.Tk()

    button1 = tkinter.Button(root, text="Button 1", command=print_b1, width=10)
    button1.bind("<Button>", print_hello)
    button1.pack()
    button2 = tkinter.Button(root, text="Button 2")
    button2.bind("<Button>", print_hello)
    button2.pack()

    variable = tkinter.IntVar(0)
    label = tkinter.Label(root, textvariable=variable)
    label.pack()
    scale = tkinter.Scale(root, orient=tkinter.HORIZONTAL)
    scale.pack()
    text = tkinter.Entry(root, textvariable=variable)
    text.pack()

if __name__ == "__main__":
    init_main_window()
    root.mainloop()
