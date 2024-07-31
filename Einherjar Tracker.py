import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from trackerFunctions import *


# initialize json data
jsonData = getJsonData('./trackerConfig.json')
bossData = getBossData(jsonData)


#init UI
root = Tk()
root.title("roTracker")
root.resizable(width=False, height=False)
root.geometry("1400x600")

my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label="test",menu=file_menu)


#Add different Tabs
tabcontrol = ttk.Notebook(root)
tab1 = ttk.Frame(tabcontrol)
tab2 = ttk.Frame(tabcontrol)
tab3 = ttk.Frame(tabcontrol)

tabcontrol.add(tab1, text= "MVPs")
tabcontrol.add(tab2, text= "Quests")
tabcontrol.add(tab3, text= "Instances")

tabcontrol.pack(expand=1, fill="both")


#Fill MVP Site
## Create fix labels
ttk.Label(tab1, text="Select MVP").grid(column=0,row=0,pady=10)
ttk.Label(tab1, text="Name:   ").grid(column=0,row=1,pady=10)
ttk.Label(tab1, text="Level:  ").grid(column=0,row=2,pady=10)
ttk.Label(tab1, text="HP:     ").grid(column=0,row=3,pady=10)
ttk.Label(tab1, text="str:    ").grid(column=0,row=4,pady=10)
ttk.Label(tab1, text="agi:    ").grid(column=0,row=5,pady=10)
ttk.Label(tab1, text="dex:    ").grid(column=0,row=6,pady=10)
ttk.Label(tab1, text="vit:    ").grid(column=0,row=7,pady=10)
ttk.Label(tab1, text="int:    ").grid(column=0,row=8,pady=10)
ttk.Label(tab1, text="luk:    ").grid(column=0,row=9,pady=10)

##Create variable labels
bossnames_combobox_string = tk.StringVar()
bossname_string = tk.StringVar()
hp_string = tk.StringVar()
cooldown_string = tk.StringVar()
str_string = tk.StringVar()
agi_string = tk.StringVar()
dex_string = tk.StringVar()
int_string = tk.StringVar()
vit_string = tk.StringVar()
luk_string = tk.StringVar()
level_string = tk.StringVar()
race_string = tk.StringVar()
property_string = tk.StringVar()
size_string = tk.StringVar()
hit100_string = tk.StringVar()
flee95_string = tk.StringVar()
atk_string = tk.StringVar()


# Define internal function
def set_bossname(*arg):
   bossname_string.set(bossData[select_boss_combobox.current()]["name"])
   hp_string.set(bossData[select_boss_combobox.current()]["hp"])
   cooldown_string.set(bossData[select_boss_combobox.current()]["hp"])
str_string.set(bossData[select_boss_combobox.current()]["hp"])
agi_string.set(bossData[select_boss_combobox.current()]["hp"])
dex_string.set(bossData[select_boss_combobox.current()]["hp"])
int_string.set(bossData[select_boss_combobox.current()]["hp"])
vit_string = tk.StringVar()
luk_string = tk.StringVar()
level_string = tk.StringVar()
race_string = tk.StringVar()
property_string = tk.StringVar()
size_string = tk.StringVar()
hit100_string = tk.StringVar()
flee95_string = tk.StringVar()
atk_string = tk.StringVar()
   

##Fill combobox with boss names
select_boss_combobox = ttk.Combobox(tab1, textvariable=(bossnames_combobox_string),state="readonly")

boss_name_Label = ttk.Label(tab1, textvariable=(bossname_string)).grid(column=1,row=1,pady=10)
boss_hp_label = ttk.Label(tab1, textvariable=(hp_string)).grid(column=1,row=3,pady=10)
bossnames_combobox_string.trace("w", set_bossname)
bossnames = list()
for item in bossData:
    bossnames.append(item["name"])

select_boss_combobox['values'] = bossnames
select_boss_combobox.grid(column=1,row=0, padx = 0,columnspan=2)

root.mainloop()



