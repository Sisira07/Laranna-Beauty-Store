from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

#sql-python connection
import mysql.connector

def clear():
    emailentry.delete(0,END)
    unameentry.delete(0,END)
    pentry.delete(0,END)
    cpentry.delete(0,END)
    check.set(0)

def login_page():#to link login file
    signup_window.destroy()
    import signin

def connect_db(): #to display error and connecting sql
    if emailentry.get()=='' or unameentry.get()=='' or pentry.get()=='' or cpentry.get()=='':
        messagebox.showerror('Error','All Fields are Required!')
    elif pentry.get()!=cpentry.get():
        messagebox.showerror('Error','Password Mismatch!')
    elif check.get()==0:
        messagebox.showerror('Error','Accept T&C!')
    else:
        try:
            cnx = mysql.connector.connect(user='root', password='sisira@dl07',host='localhost', database='userdata1')
            mycursor=cnx.cursor()
            mycursor.execute("CREATE TABLE data1(id int auto_increment primary key not null, email varchar(50),username varchar(50), password varchar(20))")

        except:
            cnx = mysql.connector.connect(user='root', password='sisira@dl07',host='localhost', database='userdata1')
            mycursor=cnx.cursor()
            mycursor.execute('use userdata1')
        #if uname exists
        mycursor.execute('select * from data1 where username=%s', (unameentry.get(),))
        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error','Username already exists!')
        else:
            query1=("insert into data1(email, username, password) values (%s, %s, %s)")
            data1=(emailentry.get(), unameentry.get(), pentry.get())
            mycursor.execute(query1, data1)
            cnx.commit()
            cnx.close()
            messagebox.showinfo('Success','Registration is successful!')
            clear()
            signup_window.destroy()
            import signin
        

signup_window=Tk()
#title and icon
signup_window.title('Signin')
signup_window.iconbitmap(r'C:\Users\user\OneDrive\Documents\Sisira\Senior high-\Grade 12\Computer Project\login\favicon.ico')

#get width & height of screen
width=signup_window.winfo_screenwidth()
height=signup_window.winfo_screenheight()

#set screensize as fullscreen and resizable
signup_window.geometry("%dx%d"%(width,height))
signup_window.resizable(True,True)

#bgimage
bg=Image.open('sbg.png')
img=bg.resize((width,height)) #full screen
bg1=ImageTk.PhotoImage(img)

#create label to add bgimage
label1=Label(signup_window,image=bg1)
label1.pack(fill='both', expand=True)

#create frame to add elements to it 
frame=Frame(signup_window,bg='white')
frame.place(x=700, y=175)

#heading
heading=Label(signup_window,text='Create an Account', font=('Microsoft Yahei UI Light',20,'bold'),bg='white',fg='indianred')
heading.place(x=730, y=117)

#email
emaillabel=Label(frame,text='Email', font=('Microsoft Yahei UI Light',11,'bold'), bg='white', fg='indianred')
emaillabel.grid(row=0,column=0,sticky='w',padx=20)

emailentry=Entry(frame,width=32, font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='indianred',bd=0)
emailentry.grid(row=3,column=0,sticky='w',padx=25,pady=3)

#username
unamelabel=Label(frame,text='Username', font=('Microsoft Yahei UI Light',11,'bold'), bg='white', fg='indianred')
unamelabel.grid(row=9,column=0,sticky='w',padx=20)

unameentry=Entry(frame,width=32, font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='indianred',bd=0)
unameentry.grid(row=12,column=0,sticky='w',padx=25,pady=3)

#pass
plabel=Label(frame,text='Password', font=('Microsoft Yahei UI Light',11,'bold'), bg='white', fg='indianred')
plabel.grid(row=18,column=0,sticky='w',padx=20)

pentry=Entry(frame,width=32, bd=0, font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='indianred')
pentry.grid(row=21,column=0,sticky='w',padx=25,pady=3)

#confirm pass
cplabel=Label(frame,text='Confirm Password', font=('Microsoft Yahei UI Light',11,'bold'), bg='white', fg='indianred')
cplabel.grid(row=27,column=0,sticky='w',padx=20)

cpentry=Entry(frame,width=32, bd=0, font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='indianred')
cpentry.grid(row=30,column=0,sticky='w',padx=25,pady=3)

#T&C
check=IntVar()
tandc=Checkbutton(frame,text='I agree to the terms and conditions',
                  font=('Microsoft Yahei UI Light',9,'bold'),bg='white',fg='indianred',
                  activebackground='white',
                  activeforeground='indianred',cursor='hand2', variable=check)
tandc.grid(row=36,column=0,sticky='w',padx=20,pady=10)

#signin

signinbutton=Button(frame, text='SIGN IN', width=21, activebackground='white',activeforeground='indianred', font=('Microsoft Yahei UI Light',15,'bold'),fg='white',
                    bg='indianred', cursor='hand2', bd=0, command=connect_db)
signinbutton.grid(row=46,column=0)

#login
lacc=Label(signup_window,text='Already have an account?',font=('Microsoft Yahei UI Light',9,'bold'),
        bg='white',fg='indianred',bd=0)
lacc.place(x=725,y=500)

lbutton=Button(signup_window,text='Login', font=('Microsoft Yahei UI Light',9,'bold','underline'),
               bg='white',fg='indianred',bd=0,cursor='hand2',activebackground='white',
               activeforeground='black',command=login_page)
lbutton.place(x=940,y=495)


signup_window.mainloop()





