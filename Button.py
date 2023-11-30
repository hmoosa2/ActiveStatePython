from tkinter import *

def cmdfunction ():
  print ("Hello")

root = Tk ( )
b = Button (root, text="Press me!" , command = cmdfunction)
b.grid (row = 0 , column = 0)
root.mainloop ( )