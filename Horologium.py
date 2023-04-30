from os import remove
from tkinter import *
from tkinter.ttk import *
from time import strftime
import winsound
import datetime

#Body depan
Root = Tk()
Root.title("Jam Digital")
Root.geometry('630x420')
photo = PhotoImage(file = r"D:\Koding\Background2.png")
tampilan1 = Label(Root, image = photo)
tampilan1.place(x = 0, y = 0)
#Setel waktu
def time():
    string = strftime('%H:%M:%S %p')
    waktu.config(text = string)
    waktu.after(1000,time)
#Setel waktu WITA dan WIT
def exit():
    Root.destroy()
tombol = Button(Root, text='WITA')
tombol.place(x=10, y=100)
tombol2 = Button(Root, text='WIT')
tombol2.place(x=10, y=200)
exit = Button(Root, text='Keluar', command=exit)
exit.place(x=10, y=300)
#font
waktu = Label(Root, font = ('Arial', 32, 'bold'),
    foreground = 'black')

#Eksekyut
waktu.pack(anchor = 'center')
time()
Root.resizable(False, False)
Root.mainloop()