<<<<<<< HEAD
import tkinter as tk
from tkinter import *

window=Tk()
window.title("PythonGeeks")
window.geometry("500x500")
Label(window,text="Play FLAMES With PythonGeeks",font=("Arial", 15 ),bg="grey").pack()

n1=tk.StringVar()
n2=tk.StringVar()

def Flames():
    name1=n1.get()
    name2=n2.get()
    namestr = name1 + name2
    for c in namestr:
        if namestr.count(c) != 1:
            namestr = namestr.replace(c,"")

    number = len(namestr) % 6

    global rel 
    rel= ""
    if number == 1:
        rel += "Friends"
    elif number == 2:
        rel += "Love"
    elif number == 3:
        rel += "Affection"
    elif number == 4:
        rel += "Marriage"
    elif number == 5:
        rel += "Enemy"
    elif number == 0:
        rel += "Siblings"
    else:
        pass
    
    Label(window,text="According to the Game of Flames the Relation is:").pack()
    Label(window,text=rel).pack()

Label(window,text="Enter Your Name").pack()
Entry(window,textvariable=n1).pack()
Label(window,text="Enter Your Crush's Name").pack()
Entry(window,textvariable=n2).pack()

Button(window,text="SHOW RESULT",bg="light blue",command=Flames).pack()
=======
import tkinter as tk
from tkinter import *

window=Tk()
window.title("PythonGeeks")
window.geometry("500x500")
Label(window,text="Play FLAMES With PythonGeeks",font=("Arial", 15 ),bg="grey").pack()

n1=tk.StringVar()
n2=tk.StringVar()

def Flames():
    name1=n1.get()
    name2=n2.get()
    namestr = name1 + name2
    for c in namestr:
        if namestr.count(c) != 1:
            namestr = namestr.replace(c,"")

    number = len(namestr) % 6

    global rel 
    rel= ""
    if number == 1:
        rel += "Friends"
    elif number == 2:
        rel += "Love"
    elif number == 3:
        rel += "Affection"
    elif number == 4:
        rel += "Marriage"
    elif number == 5:
        rel += "Enemy"
    elif number == 0:
        rel += "Siblings"
    else:
        pass
    
    Label(window,text="According to the Game of Flames the Relation is:").pack()
    Label(window,text=rel).pack()

Label(window,text="Enter Your Name").pack()
Entry(window,textvariable=n1).pack()
Label(window,text="Enter Your Crush's Name").pack()
Entry(window,textvariable=n2).pack()

Button(window,text="SHOW RESULT",bg="light blue",command=Flames).pack()
>>>>>>> 54acf9adfb3e62c395c5a5041773b767eb40bcd5
window.mainloop()