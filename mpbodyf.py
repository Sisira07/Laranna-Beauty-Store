from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root=Tk()
root.title("Bodycare")

root.iconbitmap(r'C:/Users/user/OneDrive/Documents/Sisira/Senior high-/Grade 12/Computer Project/final/favicon.ico')

#get wigth & height of screen
width=root.winfo_screenwidth()
height=root.winfo_screenheight()

#set screensize as fullscreen and not resizable
root.geometry("%dx%d"%(width,height))
root.resizable(True, False)



def bw():
    root.destroy()
    import csbw

def sg():
    root.destroy()
    import cshowergel

def bl():
    root.destroy()
    import csbl

def bs():
    root.destroy()
    import csbodyscrub












bodyframe=Frame(root)
bodyframe.place(x=0,y=0)
bfbg=Image.open('mpbg3.png')
bfhead=Image.open('bfhead.png')
rbfhead=bfhead.resize((800,200))

bfbg.paste(rbfhead,(270,20))
bftk=ImageTk.PhotoImage(bfbg)

bflab=Label(bodyframe,image=bftk)
bflab.grid(row=0,column=2,sticky=E)

bodyf=Frame(root,bg='mediumpurple4',width=root.winfo_screenwidth(), height=700)
bodyf.place(x=0,y=250)

#body wash

bwimg=Image.open('bw1.png')
rbwimg=bwimg.resize((173,250))
bwtk=ImageTk.PhotoImage(rbwimg)

bwbutton=Button(root,text='  Body Wash  ', font=('Georgia', 16), bg='mediumpurple4', fg='black',bd=0,activeforeground='black'
           ,activebackground='mediumpurple4',cursor='hand2',image=bwtk,command=bw)
bwbutton.place(x=160,y=300)

bwtxt=Label(root,text='  Body Wash  ', font=('Georgia', 16),bg='mediumpurple4', fg='white')
bwtxt.place(x=180,y=570)

#shower gel
sgimg=Image.open('sg1.png')
rsgimg=sgimg.resize((181,250))
sgtk=ImageTk.PhotoImage(rsgimg)

sgbutton=Button(root,text='  Shower Gel  ', font=('Georgia', 16), bg='mediumpurple4', fg='black',bd=0,activeforeground='black'
           ,activebackground='mediumpurple4',cursor='hand2',image=sgtk,command=sg)
sgbutton.place(x=410,y=300)

sgtxt=Label(root,text='  Shower Gel  ', font=('Georgia', 16),bg='mediumpurple4', fg='white')
sgtxt.place(x=435,y=570)

#body lotion
blimg=Image.open('bl1.png')
rblimg=blimg.resize((169,250))
bltk=ImageTk.PhotoImage(rblimg)

blbutton=Button(root,text='  Body Lotion  ', font=('Georgia', 16), bg='mediumpurple4', fg='black',bd=0,activeforeground='black'
           ,activebackground='mediumpurple4',cursor='hand2',image=bltk,command=bl)
blbutton.place(x=660,y=300)

bltxt=Label(root,text='  Body Lotion  ', font=('Georgia', 16),bg='mediumpurple4', fg='white')
bltxt.place(x=680,y=570)

#Body Scrub
bsimg=Image.open('bodyscrub1.jpg')
rbsimg=bsimg.resize((194,250))
bstk=ImageTk.PhotoImage(rbsimg)

bsbutton=Button(root,text='  Body Scrub  ', font=('Georgia', 16), bg='mediumpurple4', fg='black',bd=0,activeforeground='black'
           ,activebackground='mediumpurple4',cursor='hand2',image=bstk,command=bs)
bsbutton.place(x=890,y=300)

bltxt=Label(root,text='  Body Scrub  ', font=('Georgia', 16),bg='mediumpurple4', fg='white')
bltxt.place(x=920,y=570)

root.mainloop()
