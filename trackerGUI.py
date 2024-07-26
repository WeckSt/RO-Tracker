from tkinter import *
from tkinter import ttk

root = Tk()
root.title("roTracker")
root.resizable(width=True, height=True)
root.geometry("1400x600")

my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label="test",menu=file_menu)

root.mainloop()