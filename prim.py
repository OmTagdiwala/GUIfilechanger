import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time
import os

kin = tk.Tk()
palist = __file__.split("\\")
print(palist)
selectionlab = palist[:1]
machpath = ("\\".join(palist[:1])) + "\\"
print(machpath)

q = 6

def addtopath(t):
    global machpath
    global selectionlab
    global selectionlab
    premachpath = str(machpath)
    machpath = os.path.join(machpath, t)
    selectionlab = t
    pathin.delete(0, tk.END)
    pathin.insert(10, machpath)
    print(machpath)
    dirmenu()


def file_menus(directories):
    global q
    global selectionlab
    pathin = tk.Label(kin, text="Current File Location: ").grid(row=5)

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
    elif dirs == []:
        messagebox.showinfo("No Directory", "No Directories here :(\nThis will still become the new path though")

    
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

    dirmenu()

    print(machpath)

    def get_file():
        global filename
        filename = filein.get()
        kin.quit()

    def get_path():
        global machpath
        global pathin
        if (pathin.get() != machpath) and os.path.exists(pathin.get()):        
            machpath = pathin.get()
            print(machpath)
            dirmenu()
        else:
            print("nahhh >:(")
            messagebox.showerror("Error", "Invalid Manual Path\nDouble check the path\n(Also won't work if this is the currently used path already)")


    pathin = tk.Entry(kin, cursor="target", width=50)
    pathin.insert(10, machpath)
    pathin.grid(row=5, column=1)
    
    kin.title("File Changer :)")
    kin.geometry("500x500")

    tk.Label(kin, text="Enter a Filename: ").grid(row=0)
    # for file input textbox
    filein = tk.Entry(kin, cursor="target", width=50)
    filein.grid(row=0, column=1)
    filein.insert(10, ".txt")
    # for file input confirmation button
    tk.Button(kin, text="Search for File", cursor="dot", command=get_file, width=15, relief="ridge", justify="center").grid(row=2, column=1)
    # for path input
    tk.Button(kin, text="Use Manual Path (type in entry)", cursor="dot", command=get_path, width=15, relief="ridge", justify="center").grid(row=2, column=2)


        

    kin.mainloop()

    if filename == ".txt" or filename.strip() == "":
        print("nooo")
        messagebox.showerror("Error", "Invalid Filename\nTry another filename")
        filename = "Untitled"

    print(filename)

# # Following code is after file input

try:    
    file = open(filename, "r")
    prepreview = file.readlines()
    preview = f"{prepreview[0]}{prepreview[1]}"
except:
    file = open(filename, "w")