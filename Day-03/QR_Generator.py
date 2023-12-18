<<<<<<< HEAD
import pyqrcode
import png
from PIL import ImageTk, Image
from pyqrcode import QRCode
import tkinter as tk 
from tkinter import *
import PIL.Image

window = Tk()  
window.geometry('300x350')
window.title('PythonGeeks')

Label(window,text='Lets Create QR Code',font='arial 15').pack()

s = tk.StringVar()


def create_qrcode():
    s1=s.get()
    qr = pyqrcode.create(s1)
    qr.png('myqr.png', scale = 6)
    Label(window,text='QR Code is created and saved successfully').pack()

Entry(window,textvariable=s,font='arial 15').pack()
Button(window,text='create',bg='pink',command=create_qrcode).pack()
=======
import pyqrcode
import png
from PIL import ImageTk, Image
from pyqrcode import QRCode
import tkinter as tk 
from tkinter import *
import PIL.Image

window = Tk()  
window.geometry('300x350')
window.title('PythonGeeks')

Label(window,text='Lets Create QR Code',font='arial 15').pack()

s = tk.StringVar()


def create_qrcode():
    s1=s.get()
    qr = pyqrcode.create(s1)
    qr.png('myqr.png', scale = 6)
    Label(window,text='QR Code is created and saved successfully').pack()

Entry(window,textvariable=s,font='arial 15').pack()
Button(window,text='create',bg='pink',command=create_qrcode).pack()
>>>>>>> 54acf9adfb3e62c395c5a5041773b767eb40bcd5
window.mainloop()