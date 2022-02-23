from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry('300x300')

l1 = Label(text='tk Test', fg='black', bg='white')
l1.grid(row=0, column=0, columnspan=5)


style = ttk.Style()
style.configure('BW.TLabel', foreground='black', background='white')
l2 = ttk.Label(text='ttk Test', style='BW.TLabel')
l2.grid(row=1, column=0)

window.mainloop()