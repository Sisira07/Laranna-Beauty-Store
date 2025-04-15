from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector as sqltor
from email_validator import validate_email, EmailNotValidError


def validate_email_format(email):
    try:
        valid = validate_email(email)
        email_address = valid.email
        return email_address
    except EmailNotValidError:
        return None

def clear():
    emailentry.delete(0, END)
    unameentry.delete(0, END)
    pentry.delete(0, END)
    cpentry.delete(0, END)
    check.set(0)

def toggle_password():
    if pentry.cget("show") == "*":
        # Show the password
        pentry.config(show="")
        eye_button.config(text="👁")
    else:
        # Hide the password by showing asterisks
        pentry.config(show="*")
        eye_button.config(text="👁")
def toggle_cpassword():
    if cpentry.cget("show") == "*":
        # Show the password
        cpentry.config(show="")
        eye_button1.config(text="👁")
    else:
        # Hide the password by showing asterisks
        cpentry.config(show="*")
        eye_button1.config(text="👁")


def connect_database():
    global email
    email = emailentry.get()
    validated_email = validate_email_format(email)
   
    if emailentry.get()=='' or unameentry.get()=='' or pentry.get()=='' or cpentry.get()=='':
        messagebox.showerror("Error",'All field Are Required')
    elif validated_email==None:
        messagebox.showerror("Error",'Invalid email format')
    elif pentry.get() != cpentry.get():
        messagebox.showerror("Error",'Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please Accept Terms & Conditions')
    else:
        try:
            cnx = sqltor.connect(user='root', password='sisira@dl07',
                                 host='localhost',
                                 database='userdata1')
        except:
            messagebox.showerror("Error","Database Connectivity Issue, try again")
            return
       
        try:
            mycursor=cnx.cursor()
            mycursor.execute("create table data(id int auto_increment primary key not null,  email varchar(50), username varchar(50) UNIQUE, password varchar(20))")
        except:
            mycursor.execute("use userdata1")

        mycursor.execute('select * from data1 where username=%s', (emailentry.get(),))
        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error','Username already exist')
        else:
            query2 = ("insert into data1(email, username, password) values (%s, %s, %s)")
            data2 = (emailentry.get(), unameentry.get(), pentry.get())
            mycursor.execute(query2, data2)
            cnx.commit()
            cnx.close()
            messagebox.showinfo('Success', "Registration is successful")
            clear()
            signup_window.destroy()
            import signin

def login_page():#to link login file
    signup_window.destroy()
    import signin

signup_window=Tk()
#title and icon
signup_window.title('Signin')
#signup_window.iconbitmap(r'C:\Users\user\OneDrive\Documents\Sisira\Senior high-\Grade 12\Computer Project\login\favicon.ico')

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
frame.place(x=730, y=175)

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

pentry=Entry(frame,width=32, font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='indianred', show="*")
pentry.grid(row=21,column=0,sticky='w',padx=25,pady=3)

# Create an "eye" Button to toggle the password visibility
eye_button = Button(frame, text="👁", command=toggle_password, background='white', bd=0, activebackground='white',activeforeground='black', font=('Microsoft Yahei UI Light',11,'bold'),fg='black')
eye_button.grid(row=21, column=0, sticky='e',padx=0, pady=0)

#confirm pass
cplabel=Label(frame,text='Confirm Password', font=('Microsoft Yahei UI Light',11,'bold'), bg='white', fg='indianred')
cplabel.grid(row=27,column=0,sticky='w',padx=20)

cpentry=Entry(frame,width=32, font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='indianred', show='*')
cpentry.grid(row=30,column=0,sticky='w',padx=25,pady=3)

eye_button1 = Button(frame, text="👁", command=toggle_cpassword, background='white', bd=0, activebackground='white',activeforeground='black', font=('Microsoft Yahei UI Light',11,'bold'),fg='black')
eye_button1.grid(row=30, column=0, sticky='e',padx=0, pady=0)

#T&C
check= IntVar()

tandc=Checkbutton(frame,text='I agree to the terms and conditions',
                  font=('Microsoft Yahei UI Light',9,'bold'),bg='white',fg='indianred',
                  activebackground='white',activeforeground='indianred',cursor='hand2',  variable= check)
tandc.grid(row=36,column=0,sticky='w',padx=20,pady=10)


#signin

signinbutton=Button(frame, command=connect_database, text='SIGN IN', width=21, activebackground='white',activeforeground='indianred', font=('Microsoft Yahei UI Light',15,'bold'),fg='white',
                    bg='indianred', cursor='hand2', bd=0)
signinbutton.grid(row=46,column=0)

#login
lacc=Label(signup_window,text='Already have an account?',font=('Microsoft Yahei UI Light',9,'bold'),
        bg='white',fg='indianred',bd=0)
lacc.place(x=755,y=500)

lbutton=Button(signup_window,text='Login', font=('Microsoft Yahei UI Light',9,'bold','underline'),
               bg='white',fg='indianred',bd=0,cursor='hand2',activebackground='white',
               activeforeground='black',command=login_page)
lbutton.place(x=940,y=495)


signup_window.mainloop()




