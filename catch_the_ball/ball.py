import tkinter

def print_hello():
    print(dir(event))
    me = event.widget
    if me == button1:
        print('Hello!')
    elif me == button2:
        print('You pressed button2')
    else:
        raise ValueError()




root = tkinter.Tk()

button1 = tkinter.Button(root, text="Button 1", command=print_hello())
button1.bind("<Button>", print_hello)
button1.pack()
button2 = tkinter.Button(root, text="Button 2")
button2.bind("<Button>", print_hello)
button2.pack()

root.mainloop()
