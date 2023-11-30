from tkinter import *

def on_button_click():
    text = entry.get()
    label.config(text=f"You entered: {text}")
    listbox.insert(END, text)
    entry.delete(0, END)

root = Tk()

label = Label(root, text="Enter some text")
label.pack()

entry = Entry(root)
entry.pack()

button = Button(root, text="Submit", command=on_button_click)
button.pack()

listbox = Listbox(root)
listbox.pack()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

checkbutton = Checkbutton(root, text="Check me")
checkbutton.pack()

radiobutton1 = Radiobutton(root, text="Option 1", value=1)
radiobutton1.pack()

radiobutton2 = Radiobutton(root, text="Option 2", value=2)
radiobutton2.pack()

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL)
scale.pack()

spinbox = Spinbox(root, from_=0, to=10)
spinbox.pack()

root.mainloop()
