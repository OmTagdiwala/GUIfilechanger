import tkinter as tk
kin = tk.Tk()
print("File Changer")
filename = ".txt"

def get_file():
    global filename
    filename = filein.get()

kin.title("File Changer :)")
kin.geometry("900x500")

tk.Label(kin, text="Enter a Filename: ").grid(row=0)
filein = tk.Entry(kin)
filein.grid(row=0, column=1)
filein.insert(10, ".txt")

tk.Button(kin, text="Search for File", command=get_file).grid(row=2, column=1)

kin.mainloop()

