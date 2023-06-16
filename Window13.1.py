from tkinter import *

roto = Tk()
roto.state('zoomed')

def weather():
    app1 = Toplevel()
    app1.geometry('400x400')
    app1.title('Weather')




image2 = PhotoImage(file='C:\\Users\\Hp\\Downloads\\t.png')
Label(roto,image=image2,bd=0).pack()


roto.mainloop()