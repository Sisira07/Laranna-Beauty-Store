from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import mysql.connector

#def fucntions

def toggle_password():
    if passentry.cget("show") == "*":
        # Show the password
        passentry.config(show="")
        eye_button.config(text="👁")
    else:
        # Hide the password by showing asterisks
        passentry.config(show="*")
        eye_button.config(text="👁")

def forget_pass():#to link login file
    def toggle_password():
        if ppentry.cget("show") == "*":
            # Show the password
            ppentry.config(show="")
            eye_button.config(text="👁")
        else:
            # Hide the password by showing asterisks
            ppentry.config(show="*")
            eye_button.config(text="👁")
    def toggle_cpassword():
        if cppentry.cget("show") == "*":
            # Show the password
            cppentry.config(show="")
            eye_button1.config(text="👁")
        else:
            # Hide the password by showing asterisks
            cppentry.config(show="*")
            eye_button1.config(text="👁")


    def change_pass():
        if unameentry.get()=='' or ppentry.get()=='' or cppentry.get()=='':
            messagebox.showerror('Error','All Fields are required!',parent=window)
        elif ppentry.get()!=cppentry.get():
            messagebox.showerror('Error','Password Mismatch!', parent=window)
        else:
            cnx = mysql.connector.connect(user='root', password='sisira@dl07',
                                          host='localhost', database='userdata1')
            mycursor=cnx.cursor()
            mycursor.execute('use userdata1')
            mycursor.execute('select * from data1 where username=%s',(unameentry.get(),))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error!','Incorrect Username',parent=window)
            else:
                query2='update data1 set password=%s where username=%s'
                q3=(ppentry.get(),unameentry.get())
                mycursor.execute(query2,q3)
                cnx.commit()
                cnx.close()
                messagebox.showinfo('Success!','Password has been reset successfully!')
                #login_window.destroy()
                window.destroy()

    window=Toplevel()

    window.title('Reset Password')
    window.iconbitmap(r'C:\Users\user\OneDrive\Documents\Sisira\Senior high-\Grade 12\Computer Project\login\favicon.ico')
    #get width & height of screen
    width=window.winfo_screenwidth()
    height=window.winfo_screenheight()
    #set screensize as fullscreen and resizable
    window.geometry("%dx%d"%(width,height))
    window.resizable(True,True)
    #bgimage
    bg=Image.open('bg1.png')
    img=bg.resize((width,height)) #full screen
    bg1=ImageTk.PhotoImage(img)
    #create label to add bgimage
    label1=Label(window,image=bg1)
    label1.pack(fill='both', expand=True)
    #heading
    heading=Label(window,text='Reset Password',
              font=('Microsoft Yahei UI Light',21,'bold'),
              bg='white',fg='indianred')
    heading.place(x=760,y=130)

    #frame to add elemtns
    frame=Frame(window,bg='white')
    frame.place(x=725, y=190)
    #username
    unamelabel=Label(frame,text='Username', font=('Microsoft Yahei UI Light',11,'bold'), bg='white', fg='indianred')
    unamelabel.grid(row=10,column=0,sticky='w')
    unameentry=Entry(frame,width=32, font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='indianred',bd=0)
    unameentry.grid(row=14,column=0,sticky='w',padx=3,pady=7)
    #pass
    pplabel=Label(frame,text='New Password', font=('Microsoft Yahei UI Light',11,'bold'), bg='white', fg='indianred')
    pplabel.grid(row=23,column=0,sticky='w')
    ppentry=Entry(frame,width=32, font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='indianred',bd=0, show="*")
    ppentry.grid(row=25,column=0,sticky='w',padx=3,pady=7)
    eye_button = Button(frame, text="👁", command=toggle_password, background='white', bd=0, activebackground='white',activeforeground='black', font=('Microsoft Yahei UI Light',11,'bold'),fg='black')
    eye_button.grid(row=25, column=0, sticky='e',padx=0, pady=0)


    #confirm pass
    cpplabel=Label(frame,text='Confirm Password', font=('Microsoft Yahei UI Light',11,'bold'), bg='white', fg='indianred')
    cpplabel.grid(row=34,column=0,sticky='w')
    cppentry=Entry(frame,width=32, font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='indianred',bd=0, show="*")
    cppentry.grid(row=37,column=0,sticky='w',padx=3,pady=7)
    eye_button1 = Button(frame, text="👁", command=toggle_cpassword, background='white', bd=0, activebackground='white',activeforeground='black', font=('Microsoft Yahei UI Light',11,'bold'),fg='black')
    eye_button1.grid(row=37, column=0, sticky='e',padx=0, pady=0)

    #reset
    resetbutton=Button(window, text='RESET', width=21, activebackground='white',activeforeground='indianred', font=('Microsoft Yahei UI Light',15,'bold'),fg='white',
                    bg='indianred', cursor='hand2', bd=0, command=change_pass)
    resetbutton.place(x=728,y=420)

    window.mainloop()

def u_entry(xyz): #to delete 'username' when user clicks
    if usernameentry.get()=='Username':
        usernameentry.delete(0,END)
def p_entry(abc):
    if passentry.get()=='Password':
        passentry.delete(0,END)



def signup_page():
    login_window.destroy()
    import signup

def login_user():
    if usernameentry.get()=='' or passentry.get()=='':
        messagebox.showerror('Error','All Fields are Required!')
    else:
        try:
            con=mysql.connector.connect(user='root', password='sisira@dl07',host='localhost', database='userdata1')
            mycursor=con.cursor()
        except:
            con=mysql.connector.connect(user='root', password='sisira@dl07',host='localhost', database='userdata1')
            mycursor=con.cursor()
            mycursor.execute('use userdata1')
    ch='select*from data1 where username=%s and password=%s'
    mycursor.execute(ch, (usernameentry.get(), passentry.get()))
    row=mycursor.fetchone()
    if row==None:
        messagebox.showerror('Error','Invalid Username or Password')
    else:
        messagebox.showinfo('Welcome!','Login was Successful')
        login_window.destroy()
        import r_ohomepage
        
        
login_window=Tk()
#title and icon
login_window.title('Beauty')
#login_window.iconbitmap(r'C:\Users\user\OneDrive\Documents\Sisira\Senior high-\Grade 12\Computer Project\login\favicon.ico')

#get width & height of screen
width=login_window.winfo_screenwidth()
height=login_window.winfo_screenheight()

#set screensize as fullscreen and resizable
login_window.geometry("%dx%d"%(width,height))
login_window.resizable(True,True)

#bgimage
bg=Image.open('bg1.png')
img=bg.resize((width,height)) #full screen
bg1=ImageTk.PhotoImage(img)

#create label to add bgimage
label1=Label(login_window,image=bg1)
label1.pack(fill='both', expand=True)

#adding heading on a label
heading=Label(login_window,text='USER LOGIN', font=('Microsoft Yahei UI Light',20,'bold'),bg='white',fg='indianred')
heading.place(x=780,y=130)

#enter username,pass
usernameentry=Entry(login_window, width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='indianred')
usernameentry.place(x=740,y=200)
usernameentry.insert(0,'Username') #text that appears before user entry
usernameentry.bind('<FocusIn>',u_entry)

frame1=Frame(login_window,width=250,height=2, bg='indianred')
frame1.place(x=740, y=230)

passentry=Entry(login_window, width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='indianred', show="*")
passentry.place(x=740,y=260)
passentry.insert(0,'Password') #text that appears before user entry
passentry.bind('<FocusIn>',p_entry)

frame2=Frame(login_window,width=250,height=2, bg='indianred')
frame2.place(x=740, y=290)

#create button to see pass/not
eye_button = Button(login_window, text="👁", command=toggle_password, background='white', bd=0, activebackground='white',activeforeground='black', font=('Microsoft Yahei UI Light',11,'bold'),fg='black')
eye_button.place(x=965,y=260)

#forgot password button
forgotpass=Button(login_window,text='Forgot password?', bd=0, bg='white',
                  activebackground='white', activeforeground='indianred',cursor='hand2', font=('Microsoft Yahei UI Light',11,'bold'),
                  fg='indianred',command=forget_pass)
forgotpass.place(x=855,y=305)

#login button
loginbutton=Button(login_window, text='LOGIN', width=22,
                   activebackground='white',activeforeground='indianred',
                   font=('Microsoft Yahei UI Light',15),fg='white',
                   bg='indianred', cursor='hand2', bd=0, command=login_user)
loginbutton.place(x=740, y=350)

#OR
orlabel=Label(login_window,text='------------ OR -----------', bg='white', font=('Microsoft Yahei UI Light',15),fg='indianred')
orlabel.place(x=738, y=403)


#create acc
lacc=Label(login_window,text="Don't have an account?",font=('Microsoft Yahei UI Light',9,'bold'),
        bg='white',fg='indianred',bd=0)
lacc.place(x=740,y=490)



newaccbutton=Button(login_window, text='SignUp!', width=12, activebackground='white',activeforeground='indianred',
                    font=('Microsoft Yahei UI Light',8,'bold','underline'),fg='indianred', bg='white', cursor='hand2', bd=0,
                    command=signup_page)
newaccbutton.place(x=900, y=486)

login_window.mainloop()
