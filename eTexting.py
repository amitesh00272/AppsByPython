from tkinter import *

HEIGHT = 600
WIDTH = 800

root = Tk()
root.title('eTexting')

def give():
    result = entry.get()
    Label(lower_frame,text=result).pack()
    


canvas = Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

icon_image = PhotoImage(file='C:\\Users\\Hp\\Downloads\\micro.png')
root.iconphoto(False,icon_image)

background_image = PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Pictures\\earth.png')
background_label = Label(root,image=background_image)
background_label.place(relheight=1,relwidth=1)

frame = Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry = Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

button = Button(frame,text='Print Button',font=40,command=give)
button.place(relx=0.7,relwidth=0.3,relheight=1)

lower_frame = Frame(root,bg='#80c1ff',bd=5)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

Label(lower_frame,bg='white').place(relwidth=1,relheight=1)

Button(lower_frame,text='clear',font='cascadia').place(x=900,y=0)


root.mainloop()