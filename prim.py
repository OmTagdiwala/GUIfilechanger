import tkinter as tk
from tkinter import messagebox
import time
kin = tk.Tk()

print("File Changer")
time.sleep(1)
filename = "Untitled"
path = __file__

# # Following code is during file input
while filename == "Untitled":
    # file locator

    def selectfile(foldername):
        path = foldername
        print(path)

    machpath = __file__
    spmachpath = dict(enumerate(machpath.split("\\")))
    filemenu = tk.Menu(kin)
    kin.config(menu=filemenu)

    filemenu.add_command(label="File", command=selectfile("yoo"))

    # file inputting

    def get_file():
        global filename
        filename = filein.get()
        kin.quit()

    kin.title("File Changer :)")
    kin.geometry("300x50")

    tk.Label(kin, text="Enter a Filename: ").grid(row=0)
    # for file input textbox
    filein = tk.Entry(kin, cursor="target")
    filein.grid(row=0, column=1)
    filein.insert(10, ".txt")
    # for file input confirmation button
    tk.Button(kin, text="Search for File", cursor="dot", command=get_file, width=15, relief="ridge", justify="center").grid(row=2, column=1)
        
    kin.mainloop()

    if filename == ".txt":
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