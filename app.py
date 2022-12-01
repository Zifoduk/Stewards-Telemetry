from tkinter import *

root = Tk()
root.title("Tests screens")

e = Entry(root, width=600)

btn_text = StringVar()
is_live = True

def toggle_live(arg):
    global is_live
    is_live = not arg
    btn_text.set(is_live)

live = Button(root,textvariable=btn_text, padx=30, pady=20, command=lambda: toggle_live(is_live))
live.pack()

root.mainloop()