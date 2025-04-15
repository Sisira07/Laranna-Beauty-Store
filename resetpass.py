from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

import mysql.connector

def change_pass():
    if unameentry.get()=='' or pentry.get()=='' or cpentry.get()=='':
        messagebox.showerror('Error','All Fields are required!')
    elif pentry.get()!=cpentry.get():
        messagebox.showerror('Error','Password Mismatch!')
    else:
        cnx = mysql.connector.connect(user='root', password='sisira@dl07',
                                          host='localhost', database='userdata1')
        mycursor=cnx.cursor()
        mycursor.execute('use userdata1')
        mycursor.execute('select * from data1 where username=%s',unameentry.get())
        row=mycursor.fetchone()
        if row!=None:
            messagebox.showerror('Error!','Incorrect Username')
        else:
            query2='update data1 set password=%s where username=%s'
            mycursor.execute(query2,(pentry.get(),unameentry.get()))
            cnx.commit()
            cnx.close()
            message.showinfo('Success!','Password has been reset successfully!')
            fp.destroy()

fp=Tk()

#title and icon
fp.title('Reset Password')
fp.iconbitmap(r'C:\Users\user\OneDrive\Documents\Sisira\Senior high-\Grade 12\Computer Project\login\favicon.ico')

#get width & height of screen
width=fp.winfo_screenwidth()
height=fp.winfo_screenheight()

#set screensize as fullscreen and resizable
fp.geometry("%dx%d"%(width,height))
fp.resizable(True,True)

#bgimage
bg=Image.open('bg1.png')
img=bg.resize((width,height)) #full screen
bg1=ImageTk.PhotoImage(img)

#create label to add bgimage
label1=Label(fp,image=bg1)
label1.pack(fill='both', expand=True)

#heading
heading=Label(fp,text='Reset Password',
              font=('Microsoft Yahei UI Light',21,'bold'),
              bg='white',fg='indianred')
heading.place(x=760,y=130)

#frame to add elemtns
frame=Frame(fp,bg='white')
frame.place(x=725, y=190)

#username
unamelabel=Label(frame,text='Username', font=('Microsoft Yahei UI Light',11,'bold'), bg='white', fg='indianred')
unamelabel.grid(row=10,column=0,sticky='w')

unameentry=Entry(frame,width=32, font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='indianred',bd=0)
unameentry.grid(row=14,column=0,sticky='w',padx=3,pady=7)

#pass
plabel=Label(frame,text='New Password', font=('Microsoft Yahei UI Light',11,'bold'), bg='white', fg='indianred')
plabel.grid(row=23,column=0,sticky='w')

pentry=Entry(frame,width=32, font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='indianred',bd=0)
pentry.grid(row=25,column=0,sticky='w',padx=3,pady=7)

#confirm pass
cplabel=Label(frame,text='Confirm Password', font=('Microsoft Yahei UI Light',11,'bold'), bg='white', fg='indianred')
cplabel.grid(row=34,column=0,sticky='w')

cpentry=Entry(frame,width=32, font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='indianred',bd=0)
cpentry.grid(row=37,column=0,sticky='w',padx=3,pady=7)

#reset
resetbutton=Button(fp, text='RESET', width=21, activebackground='white',activeforeground='indianred', font=('Microsoft Yahei UI Light',15,'bold'),fg='white',
                    bg='indianred', cursor='hand2', bd=0, command=change_pass)
resetbutton.place(x=728,y=420)



fp.mainloop()
