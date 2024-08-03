import tkinter as tk
from tkinter import ttk
kin = tk.Tk()

#setting up window
kin.geometry('400x300')
kin.title("learning menus")

#setting up menu bar and holder
menu = tk.Menu(kin)
kin.configure(menu = menu)

#creating first submenu
file_menu1 = tk.Menu(menu, tearoff=False)
file_menu1.add_command(label="hmm", command= lambda: print("hmmmmmmmm"))
file_menu1.add_command(label="uhh", command= lambda: print("uhhhhhhhh"))
file_menu1.add_command(label="ehh", command= lambda: print("ehhhhhhhh"))

file_menu2 = tk.Menu(menu, tearoff=False)


menu.add_cascade(label="first option", menu=file_menu1)
menu.add_cascade(label="second option", menu=file_menu2)
file_menu2.add_command(label="wha", command= lambda: print("whaaaaaaa"))
file_menu2.add_command(label="who", command= lambda: print("whooooooo"))
file_menu2.add_command(label="why", command= lambda: print("whyyyyyyy"))

# non-top-bar version of menu
mainmenu = ttk.Menubutton(kin, text="Main menu")
mainmenu.grid()

firstsubmenu = tk.Menu(mainmenu, tearoff=False)
firstsubmenu.add_command(label="op1", command= lambda: print("cheese"))
firstsubmenu.add_checkbutton(label="op2", command= lambda: print("cheese"))

mainmenu.configure(menu = firstsubmenu)

# Realistic usecase in my program of this menu
filemenu = ttk.Menubutton(kin, text="file menu")
filemenu.grid(row=0, column=2)

filemainmenu = tk.Menu(filemenu, tearoff=False)
checkval = tk.StringVar()
checkval1 = tk.StringVar()
checkval2 = tk.StringVar()
filemainmenu.add_checkbutton(label="op3", onvalue="on", offvalue= "off",
                              variable=checkval, command= lambda: print("quack"))
filemainmenu.add_checkbutton(label="op4", onvalue="on", offvalue= "off",
                              variable=checkval1, command= lambda: print("quook"))
filesubmenu = tk.Menu(filemenu, tearoff=False)
filemainmenu.add_cascade(label="First actual submenu", menu= filesubmenu, command= lambda: print("QUAHH?!"))
filesubmenu.add_checkbutton(label="quo:)", onvalue="on", offvalue= "off",
                              variable=checkval2, command= lambda: print("QUOAH"))

filemenu.configure(menu = filemainmenu)

# part of window setup
kin.mainloop()