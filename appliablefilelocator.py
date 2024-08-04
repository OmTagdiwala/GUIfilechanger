import os
import tkinter as tk
from tkinter import ttk
kin = tk.Tk()
palist = __file__.split("\\")
print(palist)
machpath = ("\\".join(palist[:2])) + "\\"

q = 5

def addtopath(t):
    global machpath
    machpath = os.path.join(machpath, t)

def file_menus(directories):
    global q
    q+=1
    mainmenu = ttk.Menubutton(kin, text="Select File Location")

    mainmenu.grid(row= q, column= 1)

    firstsubmenu = tk.Menu(mainmenu, tearoff=False)
    for i in directories:    
        firstsubmenu.add_command(label=i, command= lambda: addtopath(i))

    mainmenu.configure(menu = firstsubmenu)
    print("cheese", q)

def dirmenu():
    dirs = []
    for i in os.scandir(machpath):
        if not os.path.isdir(i):
            continue
        dirs.append(i)
    file_menus(dirs)
    

kin.title("File Changer --- File Locator :|")
kin.geometry("500x150")
dirmenu()


kin.mainloop()