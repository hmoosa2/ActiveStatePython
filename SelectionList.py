from tkinter import *

root = Tk()

listbox = Listbox(root)
listbox.pack()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL)
scale.pack()

checkbutton = Checkbutton(root, text="Check me")
checkbutton.pack()

spinbox = Spinbox(root, from_=0, to=10)
spinbox.pack()

root.mainloop()