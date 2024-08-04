import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time
import os
q = 5

kin = tk.Tk()

palist = __file__.split("\\")
print(palist)
machpath = ("\\".join(palist[:2])) + "\\"

def file_menus():
    global q
    q+=1
    mainmenu = ttk.Menubutton(kin, text="Select File Location")

    mainmenu.grid(row= q, column= 1)

    firstsubmenu = tk.Menu(mainmenu, tearoff=False)
    firstsubmenu.add_command(label="op1", command= file_menus)
    firstsubmenu.add_command(label="op2", command= lambda: print("cheese"))

    mainmenu.configure(menu = firstsubmenu)
    print("cheese", q)

def scaledirparsing(level=None):
    global machpath
    if level != None:
        directoryy = level.split(",")
        print(directoryy)
        dirpath = ("\\".join(directoryy)) + "\\"
        machpath = os.path.join(machpath, dirpath)
        print(machpath)
    for i in os.scandir(machpath):
        if not os.path.isdir(i):
            continue
        print(i)
    print(machpath)


print("File Changer")
time.sleep(1)
filename = "Untitled"
path = __file__

# # Following code is during file input
while filename == "Untitled":
    # file locator
    q = 5
    def selectfile(foldername):
        path = foldername
        print(path)

    file_menus()
    # file inputting

    def get_file():
        global filename
        filename = filein.get()
        kin.quit()

    kin.title("File Changer :)")
    kin.geometry("500x150")

    tk.Label(kin, text="Enter a Filename: ").grid(row=0)
    # for file input textbox
    filein = tk.Entry(kin, cursor="target")
    filein.grid(row=0, column=1)
    filein.insert(10, ".txt")
    # for file input confirmation button
    tk.Button(kin, text="Search for File", cursor="dot", command=get_file, width=15, relief="ridge", justify="center").grid(row=2, column=1)
        
    kin.mainloop()

    if filename == ".txt" or filename.strip() == "":
        print("nooo")
        messagebox.showerror("Error", "Invalid Filename\nTry Rerunning the program")
        filename = "Untitled"

    print(filename)

# # Following code is after file input

try:    
    file = open(filename, "r")
    prepreview = file.readlines()
    preview = f"{prepreview[0]}{prepreview[1]}"
except:
    file = open(filename, "w")