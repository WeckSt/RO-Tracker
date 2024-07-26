import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from trackerFunctions import *

# initialize json data
jsonData = getJsonData('./trackerConfig.json')
bossData = getBossData(jsonData)


root = Tk()
root.title("roTracker")
root.resizable(width=True, height=True)
root.geometry("1400x600")

my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label="test",menu=file_menu)

tabcontrol = ttk.Notebook(root)
tab1 = ttk.Frame(tabcontrol)
tab2 = ttk.Frame(tabcontrol)
tab3 = ttk.Frame(tabcontrol)

tabcontrol.add(tab1, text= "MVPs")
tabcontrol.add(tab2, text= "Quests")
tabcontrol.add(tab3, text= "Instances")

tabcontrol.pack(expand=1, fill="both")

ttk.Label(tab1, text="Select MVP").grid(column=0,row=0,pady=10)

#Fill combobox with names

bosstest = tk.StringVar()
test = ttk.Combobox(tab1, textvariable=(bosstest),state="readonly")

bossnames = list()
for item in bossData:
    bossnames.append(item["name"])

test['values'] = bossnames

test.grid(column=1,row=0, padx = 0)

test.bind('<<ComboboxSelected>>', writeInfo(returnvalue=bosstest))

#ttk.Label(tab1, text="").grid(column=0,row=0,pady=10)

root.mainloop()



