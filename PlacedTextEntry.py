from tkinter import *

def cmdfunction():
    print(Textbox.get())


root = Tk()

Textbox = Entry(root, width=50, bg="light blue", fg="green", font=("Helvetica", 16), justify=CENTER)
Textbox.place(x=50, y=50)

Printer = Button (root, text="print your text!" , command=cmdfunction)
Printer.grid (row = 0 , column = 3, sticky=W, padx=10, pady=10)

root.mainloop()