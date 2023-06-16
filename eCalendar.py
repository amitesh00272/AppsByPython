from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import calendar

root = Tk()
root.title("Microsoft")
root.geometry("840x500+0+0")
root.resizable(False,False)

####################Icon image####################################
icon_image = PhotoImage(file='C:\\Users\\Hp\\Downloads\\micro.png')
root.iconphoto(False, icon_image)

def ex():
    root.destroy()

def wrong():
    print('Your answer is incorrect!!')

def submit():
    print('Answer is correct!!')
    Button(root,text='Submit',bd=6,command=main_screen).place(x=700,y=298)

frame = Frame(root,width=840,height=100,bg='black').pack()
Label(frame,text='Python Web From',bg='black',fg='white',font=('algerian',25)).place(x=276,y=22)

###########################################################Questions and options#########################################
frame = Frame(root,width=420,height=20,bg='black').place(x=420,y=105)
Label(root,text='Answer the following questions for entry in this app.',bg='black',fg='white').place(x=420,y=104)
Label(root,text='Who founded Google?',font = ('times',14)).place(x=420,y=134)
optionA = StringVar()
question_optionA = Radiobutton(root,variable=optionA,value='Bill Gates',text='Bill Gates',font = ('times',12),command=wrong).place(x=420,y=159)
optionA.set('Bill Gates')

question_optionB = Radiobutton(root,variable=optionA,value='Mark Zuckerberg',text='Mark Zuckerberg',font = ('times',12),command=wrong).place(x=420,y=189)

question_optionC = Radiobutton(root,variable=optionA,value='Elon Musk',text='Elon Musk',font = ('times',12),command=wrong).place(x=420,y=219)

answer = Radiobutton(root,variable=optionA,value='Larry Page and Sargey Brin',text='Larry Page and Sargey Brin',font = ('times',12)).place(x=420,y=249)

############################################Buttons
Button(root,text='Exit❗',bd=6,command=exit()).place(x=420,y=298)
Frame(frame,width=440,height=2,bg='grey').place(x=400,y=368)

Button(root,text='Exit❗',bd=6,command=main_screen()).place(x=420,y=298)
Frame(frame,width=440,height=2,bg='grey').place(x=400,y=368)
######################################################Content###########################################
Label(root,text='Enter your name:',font=('times',14)).place(x=10,y=120)
Entry(root,bd=4).place(x=10,y=152)

Frame(frame,width=400,height=2,bg='grey').place(x=0,y=190)
Frame(frame,width=2,height=370,bg='grey').place(x=400,y=100)
Frame(frame,width=400,height=2,bg='grey').place(x=0,y=468)

Label(root,text='Enter your email:',font = ('times',14)).place(x=10,y=200)
Entry(root,bd=4).place(x=140,y=200)


Label(root,text='Enter your phone number:',font = ('times',14)).place(x=10,y=260)
Entry(root,bd=4).place(x=210,y=260)

###############################################Radio button#################################################
gender = StringVar()
study = Radiobutton(root,variable=gender,value='Are you a student?',text='Are you a student?',font = ('times',14)).place(x=10,y=350)
gender.set('Are you a student?')

age = Radiobutton(root,variable=gender,value='Are you over 13 years?',text='Are you over 13 years?',font = ('times',14)).place(x=10,y=390)

def main_screen():
    root.destroy()
    calendar2 = Tk()
    calendar2.geometry('1000x580')
    calendar2.title('eCalendar')
    calendar2.resizable(False,False)


    #########################################Icon image
    icon = PhotoImage(file='C:\\Users\\Hp\\Downloads\\icon.png')
    calendar2.iconphoto(False,icon)
    ###################################Images
    background = PhotoImage(file='C:\\Users\\Hp\\Downloads\\back.png')
    back = Label(calendar2,image=background)
    back.pack()
    image = PhotoImage(file='C:\\Users\\Hp\\Downloads\\welcome.png')
    image_label = Label(calendar2,image=image,bg='white')
    image_label.place(x=280,y=88)




    #########################################################Up and Down lines
    Label(calendar2,text='Calendar By Python',font=('Microsoft YaHei UI Light',18,'bold')).place(x=500,y=3)
    Frame(calendar2,width=1000,height=5,bg='grey').place(x=0,y=40)
    Frame(calendar2,width=1000,height=6,bg='red').place(x=0,y=0)
    Frame(calendar2,width=1000,height=6,bg='red').place(x=0,y=554)

    #########################################################Right and left line
    Frame(calendar2,width=7,height=580,bg="red").place(x=240,y=0)
    Frame(calendar2,width=7,height=580,bg="red").place(x=993,y=0)

    #########################################################Main frame
    Frame(calendar2,width=240,height=580,bg="grey").place(x=0,y=0)

    Button(calendar2,text="📆 Calendar",bg='grey',fg='black',font=('Microsoft YaHei UI Light',18,'bold')).place(x=0,y=20)

    ##########################################################Main app code##################################
    def calendar_menu2():
        messagebox.showwarning('Warning','If you want to use calendar no 2 then calendar no 1 will destroy permanently.')
        calendar2.destroy()

        #####################################Code of calendar no 2
        amitesh = Tk()
        amitesh.geometry('1000x580')
        amitesh.title('eCalendar2')
      
        #########################################Icon image
        icon = PhotoImage(file='C:\\Users\\Hp\\Downloads\\icon.png')
        amitesh.iconphoto(False,icon)
        ###################################Images
        background = PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Pictures\\c.png')
        back = Label(amitesh,image=background)
        back.pack()
        

        Label(amitesh,text='Calendar2 By Python',font=('Microsoft YaHei UI Light',18,'bold')).place(x=380,y=3)
        Frame(amitesh,width=1000,height=5,bg='red').place(x=0,y=40)

        def show2():
            year = int(myCombo.get())
            calen = calendar.calendar(year)
            textBox2.delete(0.0,END)
            textBox2.insert(INSERT,calen)

        textBox2 = Text(amitesh,width=74,height=29,bd=23)
        textBox2.place(x=260,y=60)
   

        ##################################Combo Box
        myCombo = ttk.Combobox(amitesh,value=('2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010'),font=('Microsoft YaHei UI Light',8,'bold'),width=18,justify='center')
        myCombo.set('Select Years')
        myCombo.place(x=50,y=63)

        button2 = Button(amitesh,text='Show',bd=4,command=show2)
        button2.place(x=100,y=92)




        amitesh.mainloop()

    def show():
        m = int(label1_spinbox.get())
        y = int(label2_spinbox.get())
        calen = calendar.month(y,m)
        textBox.delete(0.0,END)
        textBox.insert(INSERT,calen)

    ##################Right - Left
    frame1 = Frame(calendar2,width=2,height=80,bg='black')
    frame1.place(x=480,y=100)
    frame2 = Frame(calendar2,width=2,height=80,bg='black')
    frame2.place(x=770,y=100)

    #####################Up - Down
    frame3 = Frame(calendar2,width=290,height=2,bg='black')
    frame3.place(x=480,y=100)
    frame4 = Frame(calendar2,width=292,height=2,bg='black')
    frame4.place(x=480,y=180)


    #############################Month and Year
    lbe1 = Label(calendar2,text='Month',font=('aerial',13,'bold'))
    lbe1.place(x=500,y=128)
    label1_spinbox = Spinbox(calendar2,values=(1,2,3,4,5,6,7,8,9,10,11,12),width=3,bd=5)
    label1_spinbox.place(x=570,y=130)
    lbe2 = Label(calendar2,text='Year',font=('aerial',13,'bold'))
    lbe2.place(x=660,y=128)
    label2_spinbox = Spinbox(calendar2,from_=1999,to=2100,width=4,bd=5)
    label2_spinbox.place(x=710,y=130)


    #################################Button
    button = Button(calendar2,text='Show',bd=7,command=show)
    button.place(x=600,y=210)
    textBox = Text(calendar2,width=30,height=9,bd=19)
    textBox.place(x=500,y=270)

    ###############################################################Menu bar#########################################

    Mymenu = Menu(calendar2)

    edit = Menu(Mymenu,tearoff=False)
    filemenu = Menu(Mymenu, tearoff=False)
    Help = Menu(Mymenu, tearoff=False)
    ##################File Menu
    Mymenu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='📆 Calendar2',accelerator='    Ctrl+shift+s',command=calendar_menu2)
    filemenu.add_command(label='📕 New window',accelerator='    Ctrl+N')
    filemenu.add_command(label='📂 Open File',accelerator='    Ctrl+O')
    filemenu.add_command(label='📁 New File',accelerator='    Ctrl+Alt+N')
    filemenu.add_command(label='✖ Exit',accelerator='    Ctrl+E')

    ###############################Edit Menu
    Mymenu.add_cascade(label='Edit', menu=edit)
    edit.add_command(label='💬 Undo',accelerator='    Ctrl+Z')
    edit.add_command(label='📖 Redo',accelerator='    Ctrl+Y')
    edit.add_command(label='✂ Cut',accelerator='    Ctrl+X')
    edit.add_command(label='📚 Paste',accelerator='    Ctrl+V')
    edit.add_command(label='🧮 Copy',accelerator='    Ctrl+C')

    ##############################Help Menu
    Mymenu.add_cascade(label='Help', menu=Help)
    Help.add_command(label='❗ About',accelerator='    Ctrl+A')
    Help.add_command(label='🧐 Control',accelerator='    Ctrl+Shift+C')
    Help.add_command(label='👍 Uses',accelerator='    Ctrl+Alt+U')
    Help.add_command(label='👨‍💻 About Developer',accelerator='    Shift+D')


    calendar2.config(menu=Mymenu)

    calendar2.mainloop()

root.mainloop()