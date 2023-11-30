from tkinter import *

def cmdfunction ():
  print ("Hello")
  print(var.get())

root = Tk()

var = IntVar()
var.set(0)

radiobutton1 = Radiobutton(root, text="Option 1", value=1, variable=var, command=cmdfunction)
radiobutton1.pack(side=LEFT, fill=BOTH, expand=True)

radiobutton2 = Radiobutton(root, text="Option 2", value=2, variable=var, command=cmdfunction)
radiobutton2.pack(side=LEFT, fill=BOTH, expand=True)

root.mainloop()