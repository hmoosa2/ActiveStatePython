from tkinter import *

def cmdfunction ():
  print ("Hello")

root = Tk ()
helloButton = Button (root, text="Press me!" , command = cmdfunction)
helloButton.grid (row = 0 , column = 0, sticky=N, padx=10, pady=10)

helloButton2 = Button (root, text="Press me 2!" , command = cmdfunction)
helloButton2.grid (row = 0 , column = 1, sticky=E, padx=10, pady=10)

helloButton3 = Button (root, text="Press me 3!" , command = cmdfunction)
helloButton3.grid (row = 0 , column = 2, sticky=S, padx=10, pady=10)

helloButton4 = Button (root, text="Press me 4!" , command = cmdfunction)
helloButton4.grid (row = 0 , column = 3, sticky=W, padx=10, pady=10)

root.grid_rowconfigure(0, minsize=100)

root.grid_rowconfigure(1, minsize=100)

root.grid_rowconfigure(2, minsize=100)

root.grid_rowconfigure(3, minsize=100)


root.grid_columnconfigure(0, minsize=100)

root.grid_columnconfigure(1, minsize=100)

root.grid_columnconfigure(2, minsize=100)

root.grid_columnconfigure(3, minsize=100)


root.mainloop ()