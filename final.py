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
       main_pageBtn = Button(master, text='about', command=self.about, fg='silver', bg='black',width=8,
                         font=('Engravers MT', '12', 'italic', 'bold'))
       main_pageBtn.place(x=1140, y=4)

# <== enter main_page


# ==> enter title_page button
       homeBtn = Button(main, text='Home', command=self.Home, fg='silver', bg='black',width=8,
                        font=('Engravers MT', '12', 'italic', 'bold'))
       homeBtn.place(x=860, y=4)
# <== enter title_page


# ==> quit button
      # quitBtn = Button(main, text='QUIT', command=self.exit_window, fg='silver', bg='black',
                       # font=('timesNewRoman', '12', 'italic', 'bold'))
       #quitBtn.place(x=1110, y=650)

# <== quit


# ==> title_page window
    def Home(self):
           self.master.title("Home")
           self.config(bg='white')
           self.showImg_home()
           self.pack(fill=BOTH, expand=1)

           self._Header = PhotoImage(file='Header.gif')

           self._HeaderLabel = Label(self, image=self._Header, text='Teacher', width=890, height=165).place(
            x=230, y=3)













# <== title_page

# ==> file source button
          # fileBtn = Button(main, text='book given', command=self.open_file, fg='silver', bg='black',
           #                 font=('timesNewRoman', '12', 'italic', 'bold'))
           #fileBtn.place(x=1167, y=650)



 #login


           fileBtn = Button(main, text='login', command=self.login, fg='silver', bg='black',width=8,
                            font=('Engravers MT', '12', 'italic', 'bold'))
           fileBtn.place(x=1000, y=4)


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
        login = Label(main, text='Login ', fg='grey', bg='skyblue',
                           font=('timesNewRoman', '16', 'italic', 'bold'))
        login.place(x=600, y=10)
        ID = Label(main, text='ID', fg='grey',
                           font=('Bradley Hand ITC', '16', 'italic', 'bold'))
        ID.place(x=400, y=360)
        ID = Label(main, text='password', fg='grey',
                           font=('Bradley Hand ITC', '16', 'italic', 'bold'))
        ID.place(x=400, y=390)
        adminuser =  Entry(main,show='*',
                          font=('timesNewRoman', '12', 'italic', 'bold'))
        adminuser.place(x=550, y=390)
        id =  Entry(main,
                          font=('timesNewRoman', '12', 'italic', 'bold'))
        id.place(x=550, y=360)
        AdminloginButton = Button(main, text='    login    ' ,command=main.checkadmin, fg='#6241f4',
                           font=('timesNewRoman', '12', 'italic', 'bold'))
        AdminloginButton.place(x=680, y=435)

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
        STUDENT = Label(main, text='Student', fg='grey', bg='skyblue',
                           font=('timesNewRoman', '16', 'italic', 'bold'))
        STUDENT.place(x=600, y=10)
        search = Button(main, text='    Search by book Name   ',  fg='red',bg="black",
                           font=('timesNewRoman', '12', 'italic', 'bold'))
        search.place(x=550, y=274)
        searchA = Button(main, text='    Search by book Name   ',  fg='red',bg="black",
                           font=('timesNewRoman', '12', 'italic', 'bold'))
        searchA.place(x=550, y=240)

        logout = Button(main, text='    Logout    ',command=main. Home,  fg='red',bg="black",

                           font=('timesNewRoman', '12', 'italic', 'bold'))
        logout.place(x=770, y=309)

        lb=Listbox(main,height=40,width=30)
        lb.grid(row=6,column=0,columnspan=6)

        sb=Scrollbar(main)
        sb.grid(row=6,column=6,rowspan=6)
        sb.place(x=1080, y=40)
        lb.place(x=1080, y=40)




######################login admin form##############

    def searchadmin(main):
        load=Image.open('ad.jpg')
        render = ImageTk.PhotoImage(load)
        img= Label(main, image=render)
        img.image=render
        img.place(x=0,y=0)
        admin= Label(main, text=' Admin ', fg='grey', bg='skyblue',
                           font=('Bradley Hand ITC', '16', 'italic', 'bold'))
        admin.place(x=600, y=10)
        search = Button(main, text='    Search by book Name   ',  fg='red',bg="black",
                           font=('Bradley Hand ITC', '12', 'italic', 'bold'))
        search.place(x=550, y=274)
        searcha = Button(main, text='   Search by book author  ',  fg='red',bg="black",
                           font=('Bradley Hand ITC', '12', 'italic', 'bold'))
        searcha.place(x=550, y=240)
        ###issue  by admin book to student or teacher
        issue = Button(main, text='       issue Book         ', command=main.studentlogin, fg='red',bg="black",
                           font=('Bradley Hand ITC', '12', 'italic', 'bold'))
        issue.place(x=550, y=309)

        logout = Button(main, text='    Logout    ',command=main. Home,  fg='red',bg="black",

                           font=('Bradley Hand ITC', '12', 'italic', 'bold'))
        logout.place(x=770, y=309)
        addstudent = Button(main, text='     Add student info        ',command=main.addstudnet,  fg='red',bg="black",
                           font=('Bradley Hand ITC', '12', 'italic', 'bold'))
        addstudent.place(x=550, y=210)
################# teacher login form#######################3

    def searchteacher(main):
        load=Image.open('car7.jpg')
        render = ImageTk.PhotoImage(load)
        img= Label(main, image=render)
        img.image=render
        img.place(x=0,y=0)
        lbl_Teacher = Label(main, text='Teacher', fg='grey', bg='skyblue',
                           font=('timesNewRoman', '16', 'italic', 'bold'))
        lbl_Teacher.place(x=600, y=10)
        search = Button(main, text='    Search by book Name   ',  fg='red',bg="black",
                           font=('timesNewRoman', '12', 'italic', 'bold'))
        search.place(x=550, y=274)
        searcha = Button(main, text='   Search by book author  ',  fg='red',bg="black",
                           font=('timesNewRoman', '12', 'italic', 'bold'))
        searcha.place(x=550, y=240)

        logout = Button(main, text='    Logout    ',command=main. Home,  fg='red',bg="black",

                           font=('timesNewRoman', '12', 'italic', 'bold'))
        logout.place(x=770, y=309)





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
        NAME = Entry(main,  fg='#6241f4',
                           font=('timesNewRoman', '12', 'italic', 'bold'))
        NAME.place(x=560, y=101)
        ID = Entry(main,  fg='#6241f4',
                           font=('timesNewRoman', '12', 'italic', 'bold'))
        ID.place(x=560, y=125)
        logout = Button(main, text='    Logout    ',command=main. Home,  fg='red',bg="black",

                           font=('Bradley Hand ITC', '12', 'italic', 'bold'))
        logout.place(x=770, y=309)


    def studentlogin(main):
        load=Image.open('book-image-25.jpg')
        render = ImageTk.PhotoImage(load)
        img= Label(main, image=render)
        img.image=render
        img.place(x=0,y=0)
        global id
        lbl_stud = Label(main, text='verfictaion', fg='grey', bg='skyblue',
                           font=('timesNewRoman', '16', 'italic', 'bold'))
        lbl_stud.place(x=600, y=10)
        id = Entry(main,  fg='#6241f4',
                           font=('timesNewRoman', '12', 'italic', 'bold'))
        id.place(x=560, y=101)
        verify = Button(main, text='    verify    ',command=main. verifyid,  fg='blue',bg="red",

                           font=('Bradley Hand ITC', '12', 'italic', 'bold'))
        verify.place(x=600, y=130)


        logout = Button(main, text='    back    ',command=main. searchadmin,  fg='blue',bg="red",

                           font=('Bradley Hand ITC', '12', 'italic', 'bold'))
        logout.place(x=770, y=309)

    def verifyid(main):
        print(id.get())
        if id.get()=='123':
            main.verify()
        elif  id.get()=='125':
            main.searchstudent()
        elif id.get()=='126':
            main.searchteacher()
        else:
          messagebox.showinfo("Title", "sorry you are nor register please contact admin")
          main.login()



    def verify(main):
        load=Image.open('Book-image-wallpapers-hd.jpg')
        render = ImageTk.PhotoImage(load)
        img= Label(main, image=render)
        img.image=render
        img.place(x=0,y=0)
        global id

        l1 = Label(main,text="Name")
        l1.grid(row=0,column=0,columnspan=2)

        l1.place(x=450,y=50)



        l2 = Label(main,text="Book Name")
        l2.grid(row=1,column=0,columnspan=2)
        l2.place(x=450,y=30)



        l4 = Label(main,text="Category")


        l4.grid(row=3,column=0,columnspan=2)
        l4.place(x=450,y=70)
        l5 = Label(main,text="Date")
        l5.grid(row=4,column=0,columnspan=2)
        l5.place(x=450,y=90)

        name=StringVar()
        e1 = Entry(main,textvariable=name,width=50)
        e1.grid(row=0,column=0,columnspan=10)
        e1.place(x=530,y=50)

        user=StringVar()
        e2 = Entry(main,textvariable=user,width=50)
        e2.grid(row=1,column=0,columnspan=10)
        e2.place(x=530,y=30)



        category=StringVar()
        e4 = Entry(main,textvariable=category,width=50)
        e4.grid(row=3,column=0,columnspan=10)
        e4.place(x=530,y=70)

        cdate=StringVar()
        e5 = Entry(main,textvariable=cdate,width=50)
        e5.grid(row=4,column=0,columnspan=10)
        e5.place(x=530,y=90)

        b1 = Button(main,text="Add",width=12)
        b1.grid(row=5,column=0)
        b1.place(x=530,y=110)
        b2 = Button(main,text="Update",width=12)
        b2.grid(row=5,column=1)
        b2.place(x=620,y=110)

        b3 = Button(main,text="Search",width=12)
        b3.grid(row=5,column=2)
        b3.place(x=710,y=110)

        b4 = Button(main,text="View All",width=12)
        b4.grid(row=5,column=3)
        b4.place(x=800,y=110)

        b5 = Button(main,text="Delete",width=12)
        b5.grid(row=5,column=4)
        b5.place(x=530,y=135)


        b6 = Button(main,text="Cancel",width=12)
        b6.grid(row=5,column=5)
        b6.place(x=600)
        b6.place(x=620,y=135)
        b7 = Button(main,text="Clear All",width=12)
        b7.grid(row=0,column=5)

        b7.place(x=710,y=135)

        b8=Button(main,text='Back',width=12,command=main.studentlogin)
        b8.grid(row=0,column=5)
        b8.place(x=800,y=135)

        lb=Listbox(main,height=30,width=94)
        lb.grid(row=6,column=0,columnspan=6)

        sb=Scrollbar(main)
        sb.grid(row=6,column=6,rowspan=6)
        sb.place(x=400, y=160)
        lb.place(x=400, y=160)






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
