import os
import tkinter as tk
from tkinter import ttk
kin = tk.Tk()
palist = __file__.split("\\")
print(palist)
selectionlab = palist[:1]
machpath = ("\\".join(palist[:1])) + "\\"
print(machpath)

q = 5

def addtopath(t):
    global machpath
    global selectionlab
    premachpath = str(machpath)
    
    machpath = os.path.join(machpath, t)
    selectionlab = t
    print(machpath)
    dirmenu()


def file_menus(directories):
    global q
    q+=1
    mainmenu = ttk.Menubutton(kin, text=selectionlab)

    mainmenu.grid(row= q, column= 1)

    firstsubmenu = tk.Menu(mainmenu, tearoff=False)
    for i in directories:    
        firstsubmenu.add_command(label=i, command= lambda i=i: addtopath(i))

    mainmenu.configure(menu = firstsubmenu)
    print("cheese", q)

def dirmenu():
    global machpath
    dirs = []
    for i in os.scandir(machpath):
        if not os.path.isdir(i):
            continue
        dirs.append(i)
    if dirs != []:
        file_menus(dirs)
    

kin.title("File Changer --- File Locator :|")
kin.geometry("500x150")


dirmenu()

print(machpath)

kin.mainloop()

print(machpath)