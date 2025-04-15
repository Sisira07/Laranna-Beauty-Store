from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root=Tk()
root.title("Skincare")

root.iconbitmap(r'C:\Users\user\OneDrive\Documents\Sisira\Senior high-\Grade 12\Computer Project\login\favicon.ico')

#get wigth & height of screen
width=root.winfo_screenwidth()
height=root.winfo_screenheight()

#set screensize as fullscreen and not resizable
root.geometry("%dx%d"%(width,height))
root.resizable(True, False)

bodyframe=Frame(root)
bodyframe.place(x=0,y=0)
bfbg=Image.open('mpbg4.png')
bfhead=Image.open('skinhead.png')
rbfhead=bfhead.resize((807,200))

bfbg.paste(rbfhead,(265,20))
bftk=ImageTk.PhotoImage(bfbg)

bflab=Label(bodyframe,image=bftk)
bflab.grid(row=0,column=2,sticky=E)

bodyf=Frame(root,bg='lavender',width=root.winfo_screenwidth(), height=700, autostyle=False)
bodyf.place(x=0,y=250)

#Skin Serum

ssimg=Image.open('ss1.png')
rssimg=ssimg.resize((179,250))
sstk=ImageTk.PhotoImage(rssimg)

ssbutton=Button(root,text='  Body Wash  ', font=('Georgia', 16), bg='Lavender', fg='black',bd=0,activeforeground='black'
           ,activebackground='lavender',cursor='hand2',image=sstk,command=BOTTOM, autostyle=False)
ssbutton.place(x=120,y=300)

sstxt=Label(root,text='  Skin Serum  ', font=('Georgia', 16),bg='lavender', fg='black', autostyle=False)
sstxt.place(x=150,y=570)


#Moisturizer

moimg=Image.open('mo1.png')
rmoimg=moimg.resize((176,250))
motk=ImageTk.PhotoImage(rmoimg)

mobutton=Button(root,text='  Moisturizer  ', font=('Georgia', 16), bg='Lavender', fg='black',bd=0,activeforeground='black'
           ,activebackground='lavender',cursor='hand2',image=motk,command=BOTTOM, autostyle=False)
mobutton.place(x=380,y=300)

motxt=Label(root,text='  Moisturizer  ', font=('Georgia', 16),bg='lavender', fg='black', autostyle=False)
motxt.place(x=400,y=570)

#Cleanser

climg=Image.open('cl1.png')
rclimg=climg.resize((181,250))
cltk=ImageTk.PhotoImage(rclimg)

clbutton=Button(root,text='  Cleanser  ', font=('Georgia', 16), bg='Lavender', fg='black',bd=0,activeforeground='black'
           ,activebackground='lavender',cursor='hand2',image=cltk,command=BOTTOM, autostyle=False)
clbutton.place(x=650,y=300)

cltxt=Label(root,text='  Cleanser  ', font=('Georgia', 16),bg='lavender', fg='black', autostyle=False)
cltxt.place(x=680,y=570)

#Face Wash

fwimg=Image.open('fw1.png')
rfwimg=fwimg.resize((200,250))
fwtk=ImageTk.PhotoImage(rfwimg)

fwbutton=Button(root,text='  Face Wash   ', font=('Georgia', 16), bg='Lavender', fg='black',bd=0,activeforeground='black'
           ,activebackground='lavender',cursor='hand2',image=fwtk,command=BOTTOM, autostyle=False)
fwbutton.place(x=920,y=300)

fwtxt=Label(root,text='  Face Wash  ', font=('Georgia', 16),bg='lavender', fg='black', autostyle=False)
fwtxt.place(x=950,y=570)





root.mainloop()
