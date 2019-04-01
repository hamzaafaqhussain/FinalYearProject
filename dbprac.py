import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import ImageTk
from PIL import Image


conn= sqlite3.connect('employee.db')
c=conn.cursor()
##c.execute('''CREATE TABLE xyz(                   ### qurey for database
 ##      first name,
   ##    last name
## )''')
print("succefull")
#  ===>                                             try block
try:

 main=Tk()
 main.geometry("1280x800")
 main.resizable(0,0)
 print (main.winfo_width())
 if main.winfo_width() > 200:
   print('frame1 wider than 200 pixels')
   main.pack_propagate(0)
   main.config( width=200 )



 class Window(Frame):
    def __init__(self, master=None):
       Frame.__init__(self, master)

       self.master = master

       self.Home()

# ==> menubar (the small 'menu' is user given)
       menu = Menu(self.master)
       self.master.config(menu=menu)
# <== menubar

# ==> file button on menubar
       file = Menu(menu)
       file.add_command(label='Home', command=self.Home)
       file.add_command(label='About', command=self.about)
       file.add_command(label="Login",command=self.login)
       file.add_command(label='Exit', command=self.exit_window)
       menu.add_cascade(label='File', menu=file)
# <== file button

# ==> help button on menubar
       edit = Menu(menu)
       edit.add_command(label='Contact us', command=self.Help)
       menu.add_cascade(label='Help', menu=edit)
# <== help button

# ==> enter main_page button
      # main_pageBtn = Button(master, text='ABOUT', command=self.about, fg='silver', bg='black',width=8,
       #                  font=('Engravers MT', '12', 'italic', 'bold'))
       #main_pageBtn.place(x=1140, y=4)

# <== enter main_page


# ==> enter title_page button
      # homeBtn = Button(main, text='HOME', command=self.Home, fg='silver', bg='black',width=8,
       #                 font=('Engravers MT', '12', 'italic', 'bold'))
       #homeBtn.place(x=860, y=4)
     #  login = Button(main, text='LOGIN', command=self.login, fg='silver', bg='black',width=8,
      #                  font=('Engravers MT', '12', 'italic', 'bold'))
       #login.place(x=1000, y=4)
 #login



# <== enter title_page


# ==> quit button
      # quitBtn = Button(main, text='QUIT', command=self.exit_window, fg='silver', bg='black',
                       # font=('timesNewRoman', '12', 'italic', 'bold'))
       #quitBtn.place(x=1110, y=650)

# <== quit


# ==> title_page window
    def Home(main):
           main.master.title("Home")
           main.config(bg='white')
           main.showImg_home()
           main.pack(fill=BOTH, expand=1)

           login = Button(main, text='LOGIN', command=main.login, fg='silver', bg='black',width=6,
                        font=('Engravers MT', '12', 'italic', 'bold'))
           login.place(x=1060, y=4)

           about = Button(main, text='ABOUT', command=main.about, fg='silver', bg='black',width=6,
                         font=('Engravers MT', '12', 'italic', 'bold'))
           about.place(x=1166, y=4)





           main._Header = PhotoImage(file='Header.gif')

           main._HeaderLabel = Label(main, image=main._Header, text='Teacher', width=890, height=165).place(
            x=160, y=3)


           main._rights = PhotoImage(file='Capture.gif')

           main._copyright = Label(main, image=main._rights, text='Teacher', width=200, height=165).place(
            x=2, y=585)


           main._MICRO = PhotoImage(file='23-max-1mb (2).gif')

           main.MICROPHONE = Label(main, image=main._MICRO, text='mike', width=120, height=200).place(
            x=630, y=550)


           SEARCH = Button(main, text='Speak ',  fg='black',bg='#F5DEB3',
                           font=('Brush Script MT', '12', 'italic', 'bold'))
           SEARCH.place(x=665, y=630)















# <== title_page

# ==> file source button
          # fileBtn = Button(main, text='book given', command=self.open_file, fg='silver', bg='black',
           #                 font=('timesNewRoman', '12', 'italic', 'bold'))
           #fileBtn.place(x=1167, y=650)





# <== file source

# ==>open file
    def open_file(self):
          filename = "book given.txt"
          file = open(filename, "r")
          for line in file:
            print(line)
#file

# ==> main_page window
    def about(main):
        main.master.title("about")
        main.about_main()
        main.pack(fill=BOTH, expand=1)

        homeBtn = Button(main, text='HOME', command=main.Home, fg='silver', bg='black',width=6,
                       font=('Engravers MT', '12', 'italic', 'bold'))
        homeBtn.place(x=1060, y=4)

        login = Button(main, text='LOGIN', command=main.login, fg='silver', bg='black',width=6,
                        font=('Engravers MT', '12', 'italic', 'bold'))
        login.place(x=1166, y=4)


# ==> main_page window



#=======>contact us
    def Help(main):
        main.master.title("about")
        main.about_main()
        main.pack(fill=BOTH, expand=1)


# <== main_page
    def login(main):
        global adminuser
        global id
        main.master.title("login")
        main.login_main()
        main.pack(fill=BOTH, expand=1)


        about = Button(main, text='ABOUT', command=main.about, fg='silver', bg='black',width=6,
                         font=('Engravers MT', '12', 'italic', 'bold'))
        about.place(x=1166, y=4)

        homeBtn = Button(main, text='HOME', command=main.Home, fg='silver', bg='black',width=6,
                       font=('Engravers MT', '12', 'italic', 'bold'))
        homeBtn.place(x=1060, y=4)

        #main.login = PhotoImage(file='DeerDeluxe_large.gif')

#        main._HeaderLabel = Label(main, image=main.login, text='Teacher', width=370, height=345).place(
 #           x=400, y=200)




        login = Label(main, text='Login ', fg='grey', bg='skyblue',
                           font=('timesNewRoman', '16', 'italic', 'bold'))
        login.place(x=600, y=10)
        ID = Label(main, text='ID', fg='grey',
                           font=('Bradley Hand ITC', '16', 'italic', 'bold'))
        ID.place(x=400, y=360)
        ID = Label(main, text='password', fg='grey',
                           font=('Bradley Hand ITC', '14', 'italic', 'bold'))
        ID.place(x=400, y=380)
        adminuser =  Entry(main,show='*',
                          font=('timesNewRoman', '12', 'italic', 'bold'))
        adminuser.place(x=550, y=383)
        id =  Entry(main,
                          font=('timesNewRoman', '12', 'italic', 'bold'))
        id.place(x=550, y=360)
        AdminloginButton = Button(main, text='    login    ' ,command=main.checkadmin, fg='#6241f4',
                           font=('timesNewRoman', '12', 'italic', 'bold'))
        AdminloginButton.place(x=550, y=410)
        back = Button(main, text='    Back   ' ,command=main.Home, fg='#6241f4',
                           font=('timesNewRoman', '12', 'italic', 'bold'))
        back.place(x=650, y=410)
############### loging check funtion####
    def checkadmin(main):
        print(adminuser.get(),id.get())
        if adminuser.get().lower()=='admin'and id.get()=='123':
            main.searchadmin()
        elif adminuser.get().lower()=='student'and id.get()=='123':
            main.searchstudent()
        elif adminuser.get().lower()=='teacher'and id.get()=='123':
            main.searchteacher()
        else:
          messagebox.showinfo("Title", "sorry you are nor register please contact admin")
          main.login()
########## login student form or ########
    def searchstudent(main):
        load=Image.open('student.jpg')
        render = ImageTk.PhotoImage(load)
        img= Label(main, image=render)
        img.image=render
        img.place(x=0,y=0)



        main._adminl = PhotoImage(file='12345s.gif')

        main._HeaderLabel = Label(main, image=main._adminl, text='Teacher', width=144, height=170).place(
            x=70, y=80)
        A='Name'
        B='Reg.No'
        C='Semester'
        D='Program'
        E='Contact'


        l1 = Label(main,text=A,width=15,font=('Edwardian Script ITC','20','bold'),fg='white',bg="black")
        l1.grid(row=0,column=0,columnspan=2)

        l1.place(x=30,y=250)



        l2 = Label(main,text=B,width=15,font=('Edwardian Script ITC','20','bold'),fg='white',bg="black")
        l2.grid(row=1,column=0,columnspan=2)
        l2.place(x=30,y=285)



        l4 = Label(main,text=C,width=15,font=('Edwardian Script ITC','20','bold'),fg='white',bg="black")


        l4.grid(row=3,column=0,columnspan=2)
        l4.place(x=30,y=315)

        l5 = Label(main,text=D,width=15,font=('Edwardian Script ITC','20','bold'),fg='white',bg="black")
        l5.grid(row=4,column=0,columnspan=2)
        l5.place(x=30,y=345)

        l6 = Label(main,text=E,width=15,font=('Edwardian Script ITC','20','bold'),fg='white',bg="black")
        l6.grid(row=4,column=0,columnspan=2)
        l6.place(x=30,y=375)





        STUDENT = Label(main, text='Student', fg='grey', bg='skyblue',
                           font=('timesNewRoman', '16', 'italic', 'bold'))
        STUDENT.place(x=600, y=10)

        issue = Label(main, text='Current Issue Books', fg='White', bg='black',
                           font=('Blackadder ITC', '16', 'italic', 'bold'))
        issue.place(x=500, y=630)



        search = Button(main, text='    view   ',  fg='white',bg="black",
                           font=('timesNewRoman', '12', 'italic', 'bold'))
        search.place(x=680, y=630)


        logout = Button(main, text='    Logout    ',command=main. login,  fg='red',bg="black",

                           font=('Bradley Hand ITC', '12', 'italic', 'bold'))
        logout.place(x=1160, y=710)

        lb=Listbox(main,height=5,width=80)
        lb.grid(row=6,column=0,columnspan=6)

        sb=Scrollbar(main)
        sb.grid(row=6,column=6,rowspan=6)
        sb.place(x=350, y=670)
        lb.place(x=350, y=670)




######################login admin form##############

    def searchadmin(main):
        load=Image.open('ad.jpg')
        render = ImageTk.PhotoImage(load)
        img= Label(main, image=render)
        img.image=render
        img.place(x=0,y=0)


        main._adminl = PhotoImage(file='adminlogin.gif')

        main._HeaderLabel = Label(main, image=main._adminl, text='Teacher', width=277, height=125).place(
            x=10, y=120)



        A='Name'
        B='E-Mail'
        C='Contact'
        D='Designation'


        l1 = Label(main,text=A,width=17,font=('Edwardian Script ITC','20','bold'),fg='white',bg="black")
        l1.grid(row=0,column=0,columnspan=2)

        l1.place(x=10,y=250)



        l2 = Label(main,text=B,width=17,font=('Edwardian Script ITC','20','bold'),fg='white',bg="black")
        l2.grid(row=1,column=0,columnspan=2)
        l2.place(x=10,y=285)



        l4 = Label(main,text=C,width=17,font=('Edwardian Script ITC','20','bold'),fg='white',bg="black")


        l4.grid(row=3,column=0,columnspan=2)
        l4.place(x=10,y=315)

        l5 = Label(main,text=D,width=17,font=('Edwardian Script ITC','20','bold'),fg='white',bg="black")
        l5.grid(row=4,column=0,columnspan=2)
        l5.place(x=10,y=345)









        admin= Label(main, text=' Admin ', fg='grey', bg='skyblue',
                           font=('Bradley Hand ITC', '16', 'italic', 'bold'))
        admin.place(x=600, y=10)
        search = Button(main, text='       Entery newbook        ',command=main.newbook,  fg='white',bg="black",
                           font=('Bradley Hand ITC', '14', 'italic', 'bold'))
        search.place(x=470, y=280)
        searcha = Button(main, text='         Return Book           ', command=main.Return, fg='white',bg="black",
                           font=('Bradley Hand ITC', '14', 'italic', 'bold'))
        searcha.place(x=750, y=280)
        ###issue  by admin book to student or teacher
        issue = Button(main, text='         Issue Book.             ', command=main.verify, fg='white',bg="black",
                           font=('Bradley Hand ITC', '14', 'italic', 'bold'))
        issue.place(x=750, y=330)

        logout = Button(main, text='    Logout    ',command=main. Home,  fg='red',bg="black",

                           font=('Bradley Hand ITC', '12', 'italic', 'bold'))
        logout.place(x=1160, y=710)
        addstudent = Button(main, text='    Student Registration  ',command=main.addstudnet,  fg='white',bg="black",
                           font=('Bradley Hand ITC', '14', 'italic', 'bold'))
        addstudent.place(x=470, y=330)
################# teacher login form#######################3

    def searchteacher(main):
        load=Image.open('car7.jpg')
        render = ImageTk.PhotoImage(load)
        img= Label(main, image=render)
        img.image=render
        img.place(x=0,y=0)
        main._adminl = PhotoImage(file='staff.gif')

        main._HeaderLabel = Label(main, image=main._adminl, text='Teacher', width=144, height=250).place(
            x=70, y=80)
        A='Name'
        B='Staff ID'
        C='location'
        D='Address'
        E='Contact'
        F="Email"
        G="Designation"


        l1 = Label(main,text=A,width=15,font=('Edwardian Script ITC','20','bold'),fg='white',bg="black")
        l1.grid(row=0,column=0,columnspan=2)

        l1.place(x=30,y=250)



        l2 = Label(main,text=B,width=15,font=('Edwardian Script ITC','20','bold'),fg='white',bg="black")
        l2.grid(row=1,column=0,columnspan=2)
        l2.place(x=30,y=285)



        l4 = Label(main,text=C,width=15,font=('Edwardian Script ITC','20','bold'),fg='white',bg="black")


        l4.grid(row=3,column=0,columnspan=2)
        l4.place(x=30,y=315)

        l5 = Label(main,text=D,width=15,font=('Edwardian Script ITC','20','bold'),fg='white',bg="black")
        l5.grid(row=4,column=0,columnspan=2)
        l5.place(x=30,y=345)

        l6 = Label(main,text=E,width=15,font=('Edwardian Script ITC','20','bold'),fg='white',bg="black")
        l6.grid(row=4,column=0,columnspan=2)
        l6.place(x=30,y=375)

        l7 = Label(main,text=F,width=15,font=('Edwardian Script ITC','20','bold'),fg='white',bg="black")
        l7.grid(row=4,column=0,columnspan=2)
        l7.place(x=30,y=405)

        l8 = Label(main,text=G,width=15,font=('Edwardian Script ITC','20','bold'),fg='white',bg="black")
        l8.grid(row=4,column=0,columnspan=2)
        l8.place(x=30,y=435)







        STUDENT = Label(main, text='Student', fg='grey', bg='skyblue',
                           font=('timesNewRoman', '16', 'italic', 'bold'))
        STUDENT.place(x=600, y=10)

        issue = Label(main, text='Current Issue Books', fg='White', bg='black',
                           font=('Blackadder ITC', '16', 'italic', 'bold'))
        issue.place(x=500, y=630)



        search = Button(main, text='    view   ',  fg='white',bg="black",
                           font=('timesNewRoman', '12', 'italic', 'bold'))
        search.place(x=680, y=630)


        logout = Button(main, text='    Logout    ',command=main. login,  fg='red',bg="black",

                           font=('Bradley Hand ITC', '12', 'italic', 'bold'))
        logout.place(x=1160, y=710)

        lb=Listbox(main,height=5,width=80)
        lb.grid(row=6,column=0,columnspan=6)

        sb=Scrollbar(main)
        sb.grid(row=6,column=6,rowspan=6)
        sb.place(x=350, y=670)
        lb.place(x=350, y=670)








# ==> menubar (the small 'menu' is user given)
        menu = Menu(main.master)
        main.master.config(menu=menu)
# <== menubar

# ==> file button on menubar
        file = Menu(menu)
        file.add_command(label='About', command=main.about)
        file.add_command(label='LOGIN', command=main.login)
        file.add_command(label='Title page', command=main.Home)
        file.add_command(label='Save', command='')
        file.add_command(label='Exit', command=main.exit_window)
        menu.add_cascade(label='File', menu=file)
# <== file button

# ==> help button on menubar
        edit = Menu(menu)
        edit.add_command(label='Contact us', command='')
        menu.add_cascade(label='Help', menu=edit)
# <== help button

# ==> function for exit event handling
    def exit_window(self):
        exit()
# <== exit event

# ==> function to show  image

    def showImg_home(self):
        load = Image.open('home_page.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0, relwidth=1, relheight=1)
# <== image function main_page
    def about_main(self):
        load=Image.open('about.jpg')
        render = ImageTk.PhotoImage(load)
        img= Label(self, image=render)
        img.image=render
        img.place(x=0,y=0)
# ==> function to show home_page image
    def login_main(self):
        load=Image.open('login.jpg')
        render = ImageTk.PhotoImage(load)
        img= Label(self, image=render)
        img.image=render
        img.place(x=0,y=0)

# <== image function home_page


#                       >>>>>>>>>>>>>>>>> Search FUNCTION <<<<<<<<<<<<<<<<<<






# ==> function to show image of car 7




    def addstudnet(main):
        load=Image.open('studentadd.jpg')
        render = ImageTk.PhotoImage(load)
        img= Label(main, image=render)
        img.image=render
        img.place(x=0,y=0)
        lbl_addstud = Label(main, text='Add student', fg='grey', bg='skyblue',
                           font=('timesNewRoman', '16', 'italic', 'bold'))
        lbl_addstud.place(x=600, y=10)

        global name
        global regid
        global v
        global passw
        global email
        global contact
        global addre
        global depe
        global lb

        l1 = Label(main,text="Name",
                         font=('Harlow Solid Italic', '16', 'italic', 'bold'))
        l1.grid(row=0,column=0,columnspan=2)
        l1.place(x=2,y=100)

        name=StringVar()
        e1 = Entry(main,textvariable=name,width=40)
        e1.grid(row=0,column=0,columnspan=10)
        e1.place(x=80,y=110)





    #French Script MT

        l2 = Label(main,text="REG ID",
                       font=('Harlow Solid Italic', '16', 'italic', 'bold'))
                                                                            #40  DIFFERENCE IN Y

        l2.grid(row=1,column=0,columnspan=2)
        l2.place(x=2,y=140)

        regid=StringVar()
        e2 = Entry(main,textvariable=regid,width=40)
        e2.grid(row=0,column=0,columnspan=10)
        e2.place(x=115,y=150)

        l3 = Label(main,text="Password",
                   font=('Harlow Solid Italic', '16', 'italic', 'bold'))
        l3.grid(row=2,column=0,columnspan=2)
        l3.place(x=2,y=180)

        passw=StringVar()
        e3 = Entry(main,textvariable=passw,width=40)
        e3.grid(row=0,column=0,columnspan=10)
        e3.place(x=110,y=190)



        l4 = Label(main,text="Department Name",
                   font=('Harlow Solid Italic', '16', 'italic', 'bold'))
        l4.grid(row=3,column=0,columnspan=2)
        l4.place(x=2,y=220)

        depe=StringVar()
        e4 = Entry(main,textvariable=depe,width=40)
        e4.grid(row=0,column=0,columnspan=10)
        e4.place(x=200,y=230)


        l5 = Label(main,text="Address",
                   font=('Harlow Solid Italic', '16', 'italic', 'bold'))
        l5.grid(row=4,column=0,columnspan=2)
        l5.place(x=2,y=260)

        addre=StringVar()
        e5 = Entry(main,textvariable=addre,width=40)
        e5.grid(row=0,column=0,columnspan=10)
        e5.place(x=100,y=270)





        l6 = Label(main,text="E-mail",
                   font=('Harlow Solid Italic', '16', 'italic', 'bold'))
        l6.grid(row=4,column=0,columnspan=2)
        l6.place(x=2,y=300)

        email=StringVar()
        e6 = Entry(main,textvariable=email,width=40)
        e6.grid(row=0,column=0,columnspan=10)
        e6.place(x=80,y=310)





        l7 = Label(main,text="Contact-No",
                   font=('Harlow Solid Italic', '16', 'italic', 'bold'))
        l7.grid(row=4,column=0,columnspan=2)
        l7.place(x=2,y=340)

        contact=StringVar()
        e7 = Entry(main,textvariable=contact,width=40)
        e7.grid(row=0,column=0,columnspan=10)
        e7.place(x=130,y=350)

        l8 = Label(main,text="Gender",
                   font=('Harlow Solid Italic', '16', 'italic', 'bold'))
        l8.grid(row=4,column=0,columnspan=2)
        l8.place(x=2,y=380)

        v = StringVar()
        x=Radiobutton(main, text='Male', variable=v, value="Male")
        y=Radiobutton(main, text='Female', variable=v, value="Female")

        x.place(x=80,y=385)
        y.place(x=135,y=385)








      #  name=StringVar()
       # e1 = Entry(main,textvariable=name,width=50)
        #e1.grid(row=0,column=0,columnspan=10)

        #user=StringVar()
       # e2 = Entry(main,textvariable=user,width=50)
        #e2.grid(row=1,column=0,columnspan=10)

   #     password=StringVar()
  #      e3 = Entry(main,textvariable=password,width=50)
 #       e3.grid(row=2,column=0,columnspan=10)
#
  #      category=StringVar()
 #       e4 = Entry(main,textvariable=category,width=50)
#        e4.grid(row=3,column=0,columnspan=10)
#
        #cdate=StringVar()
        #e5 = Entry(main,textvariable=cdate,width=50)
       # e5.grid(row=4,column=0,columnspan=10)

        #b2 = Button(main,text="Back",width=12,command=main.searchadmin)
        #b2.grid(row=5,column=1)
        b1 = Button(main,text="Add",width=12,command=main.add_command)
        b1.grid(row=5,column=0)
        b1.place(x=250,y=385)

        lb=Listbox(main,height=15,width=80)
        lb.grid(row=5,column=8,columnspan=6)
        lb.place(x=2,y=430)











        back = Button(main, text='    back    ',command=main. searchadmin,  fg='blue',bg="black",

                           font=('Bradley Hand ITC', '12', 'italic', 'bold'))
        back.place(x=1150, y=700)

    def add_command(main):
        lb.delete(0,END)
        lb.insert(END,name.get(),regid.get(),passw.get(),depe.get(),addre.get(),email.get(),contact.get(),v.get())




    def Return(main):#studentlogin
        load=Image.open('book-image-25.jpg')
        render = ImageTk.PhotoImage(load)
        img= Label(main, image=render)
        img.image=render
        img.place(x=0,y=0)
        global id
        global book
        global u
        global i
        global d
        global rb
        global e5
        global e6



        l1 = Label(main,text=" Id",fg='blue')
        l1.grid(row=0,column=0,columnspan=2)

        l1.place(x=10,y=50)

        l2 = Label(main,text="Bookid",fg='blue')
        l2.grid(row=1,column=0,columnspan=2)
        l2.place(x=10,y=80)



        l5 = Label(main,text="RETURN Date",fg='blue')
        l5.grid(row=4,column=0,columnspan=2)
        l5.place(x=10,y=110)
        l6 = Label(main,text="ISSUE Date",fg='blue')
        l6.grid(row=4,column=0,columnspan=2)
        l6.place(x=10,y=140)

        id=StringVar()
        e1 = Entry(main,textvariable=id,width=50)
        e1.grid(row=0,column=0,columnspan=10)
        e1.place(x=80,y=50)

        book=StringVar()
        e1 = Entry(main,textvariable=book,width=50)
        e1.grid(row=0,column=0,columnspan=10)
        e1.place(x=80,y=80)


        i=StringVar()

        e5 =Entry(main,textvariable=i,width=43,bg='white')
        e5.grid(row=4,column=0,columnspan=10)
        e5.place(x=80,y=110)

        u=StringVar()
        e6 =Entry(main,textvariable=u,width=43,bg='white')
        e6.grid(row=4,column=0,columnspan=10)
        e6.place(x=80,y=140)





        issue = Button(main, text='    Return    ',  fg='blue',bg="red",command=main.returned,

                           font=('Bradley Hand ITC', '15', 'italic', 'bold'))
        issue.place(x=400, y=70)



        back = Button(main, text='    back    ',command=main. searchadmin,  fg='blue',bg="red",

                           font=('Bradley Hand ITC', '12', 'italic', 'bold'))
        back.place(x=1150, y=700)

        rb=Listbox(main,height=30,width=50)
        rb.grid(row=6,column=0,columnspan=6)
        rb.place(x=80, y=200)



    def returned(main):
        rb.delete(0,END)
        import datetime

        tday = datetime.date.today()
        tdelta = datetime.timedelta(days=7)
        issue = tday-tdelta

        print(tday)

        e6.insert(END,"ISSUE "+"----"+str(issue))
        e5.insert(END,"RETURN "+"----"+str(tday))
        rb.insert(END,"Id "+"----"+id.get(),"book "+"----"+book.get(),i.get(),u.get(),"plenty to "+"----")



    def verifyid(main):
        print(id.get())
        if id.get()=='123':
            main.verify()
        elif  id.get()=='125':
            main.searchstudent()
        elif id.get()=='126':
            main.searchteacher()
        else:
          messagebox.showinfo("Title", "Sorry you are not register please contact admin")
          main.verification()



    def verify(main):
        load=Image.open('Book-image-wallpapers-hd.jpg')
        render = ImageTk.PhotoImage(load)
        img= Label(main, image=render)
        img.image=render
        img.place(x=0,y=0)


        global id
        global book
        global u
        global i
        global d
        global tb
        global e5
        global e6






        l1 = Label(main,text=" Id",fg='blue')
        l1.grid(row=0,column=0,columnspan=2)

        l1.place(x=10,y=50)






        l2 = Label(main,text="Bookid",fg='blue')
        l2.grid(row=1,column=0,columnspan=2)
        l2.place(x=10,y=80)



        l5 = Label(main,text="Issue Date",fg='blue')
        l5.grid(row=4,column=0,columnspan=2)
        l5.place(x=10,y=110)
        l6 = Label(main,text="Return Date",fg='blue')
        l6.grid(row=4,column=0,columnspan=2)
        l6.place(x=10,y=140)

        id=StringVar()
        e1 = Entry(main,textvariable=id,width=50)
        e1.grid(row=0,column=0,columnspan=10)
        e1.place(x=80,y=50)

        book=StringVar()
        e1 = Entry(main,textvariable=book,width=50)
        e1.grid(row=0,column=0,columnspan=10)
        e1.place(x=80,y=80)


        i=StringVar()

        e5 =Entry(main,textvariable=i,width=43,bg='white')
        e5.grid(row=4,column=0,columnspan=10)
        e5.place(x=80,y=110)

        u=StringVar()
        e6 =Entry(main,textvariable=u,width=43,bg='white')
        e6.grid(row=4,column=0,columnspan=10)
        e6.place(x=80,y=140)




        d = StringVar()
        x=Radiobutton(main, text='Staff', variable=d, value="STAFF")
        y=Radiobutton(main, text='Student', variable=d, value="STUDENT")
        x.place(x=85,y=170)
        y.place(x=135,y=170)
        issue = Button(main, text='    ISSUE    ',  fg='blue',bg="red",command=main.isuued,

                           font=('Bradley Hand ITC', '15', 'italic', 'bold'))
        issue.place(x=400, y=70)



        back = Button(main, text='    back    ',command=main. searchadmin,  fg='blue',bg="red",

                           font=('Bradley Hand ITC', '12', 'italic', 'bold'))
        back.place(x=1150, y=700)

        tb=Listbox(main,height=30,width=50)
        tb.grid(row=6,column=0,columnspan=6)


        tb.place(x=80, y=200)

    def isuued(main):
        tb.delete(0,END)
        import datetime

        tday = datetime.date.today()
        tdelta = datetime.timedelta(days=7)
        plenty = tday+tdelta
        print(tday)

        e6.insert(END,"Return "+"----"+str(plenty))
        e5.insert(END,"issue "+"----"+str(tday))
        tb.insert(END,"Id "+"----"+id.get(),"book "+"----"+book.get(),i.get(),u.get(),"issue to "+"----"+d.get())


    def newbook(main):
        load=Image.open('books_shelf_stairs_125930_1280x800.jpg')
        render = ImageTk.PhotoImage(load)
        img= Label(main, image=render)
        img.image=render
        img.place(x=0,y=0)
        global bookid
        global bookname
        global author
        global Shelf
        global d
        global rb
        global e5
        global e6



        l1 = Label(main,text="Book Id",fg='blue')
        l1.grid(row=0,column=0,columnspan=2)

        l1.place(x=10,y=50)

        l2 = Label(main,text="BookName",fg='blue')
        l2.grid(row=1,column=0,columnspan=2)
        l2.place(x=10,y=80)



        l5 = Label(main,text="Author",fg='blue')
        l5.grid(row=4,column=0,columnspan=2)
        l5.place(x=10,y=110)
        l6 = Label(main,text="Shelf No",fg='blue')
        l6.grid(row=4,column=0,columnspan=2)
        l6.place(x=10,y=140)

        bookid=StringVar()
        e1 = Entry(main,textvariable=bookid,width=50)
        e1.grid(row=0,column=0,columnspan=10)
        e1.place(x=80,y=50)

        bookname=StringVar()
        e1 = Entry(main,textvariable=bookname,width=50)
        e1.grid(row=0,column=0,columnspan=10)
        e1.place(x=80,y=80)


        author=StringVar()

        e5 =Entry(main,textvariable=author,width=43,bg='white')
        e5.grid(row=4,column=0,columnspan=10)
        e5.place(x=80,y=110)

        Shelf=StringVar()
        e6 =Entry(main,textvariable=Shelf,width=43,bg='white')
        e6.grid(row=4,column=0,columnspan=10)
        e6.place(x=80,y=140)





        issue = Button(main, text='    Submit    ',  fg='blue',bg="red",command=main.NEW,

                           font=('Bradley Hand ITC', '15', 'italic', 'bold'))
        issue.place(x=400, y=70)



        back = Button(main, text='    back    ',command=main. searchadmin,  fg='blue',bg="red",

                           font=('Bradley Hand ITC', '12', 'italic', 'bold'))
        back.place(x=1150, y=700)

        rb=Listbox(main,height=30,width=50)
        rb.grid(row=6,column=0,columnspan=6)
        rb.place(x=80, y=200)


    def NEW(main):
        rb.delete(0,END)
        import datetime

        tday = datetime.date.today()
        tdelta = datetime.timedelta(days=7)
        issue = tday-tdelta

        print(tday)


        rb.insert(END,"BookId "+"----"+bookid.get(),"bookNAME "+"----"+bookname.get()," Auther name"+"----"+author.get(),"Shelf no "+"----"+Shelf.get(),)










# <== image function of car 20

#   <===                                             try block

#

#   ===>                                              except block

#Import Error      ===>  When the imported module is not available.
#FileNotFoundError ===>  Raised when a file or directory is requested but doesn’t exist.
#SyntaxError       ===>  For errors in Python syntax.
#IndentationError  ===>  When indentation is not proper.
#Exception         ===>  It is the base class for all exceptions.
except (ImportError,FileNotFoundError,SyntaxError,IndentationError,Exception):
    print('error present')
#   <===                                              except block


else:
 app = Window(main)
 main.mainloop()
