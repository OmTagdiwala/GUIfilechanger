import tkinter as tk
from tkinter import messagebox
kin = tk.Tk()
print("File Changer")
filename = ".txt"


# # Following code is during file input

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

print(filename)
# # Following code is after file input

if filename == ".txt":
    print("nooo")
    messagebox.showerror("Error", "Invalid Filename\nTry Rerunning the program")
    quit()

file = open(filename, "r")
# This is the preview of the file
prepreview = file.readlines()
preview = f"{prepreview[0]}{prepreview[1]}"