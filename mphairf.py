from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root=Tk()
root.title("   Laranna")

root.iconbitmap(r'C:/Users/user/OneDrive/Documents/Sisira/Senior high-/Grade 12/Computer Project/final/favicon.ico')

#get wigth & height of screen
width=root.winfo_screenwidth()
height=root.winfo_screenheight()

#set screensize as fullscreen and not resizable
root.geometry("%dx%d"%(width,height))
root.resizable(True, False)

hairframe=Frame(root)
hairframe.place(x=0,y=0)
hfbg=Image.open('mpbg2.png')
hfhead=Image.open('hfhead.png')
rhfhead=hfhead.resize((800,200))

hfbg.paste(rhfhead,(270,30))
hftk=ImageTk.PhotoImage(hfbg)

hflab=Label(hairframe,image=hftk)
hflab.grid(row=0,column=2,sticky=E)

prodf=Frame(root,bg='lavender',width=root.winfo_screenwidth(), height=700)
prodf.place(x=0,y=250)




def sham():
    root.destroy()
    import cshampoo

def cond():
    root.destroy()
    import csconditioner

def hm():
    root.destroy()
    import cshairmask

def hs():
    root.destroy()
    import cshairserum

def sp():
    root.destroy()
    import csstylingprimer

#shampoo

shimg=Image.open('mpsham.png')
rshimg=shimg.resize((188,250))
shamtk=ImageTk.PhotoImage(rshimg)

sbutton=Button(root,text='  Shampoo  ', font=('Georgia', 16), bg='lavender', fg='black',bd=0,activeforeground='black'
           ,activebackground='lavender',cursor='hand2',
               image=shamtk,command=sham)
sbutton.place(x=50,y=300)

shtxt=Label(root,text='  Shampoo  ', font=('Georgia', 16),bg='lavender', fg='black')
shtxt.place(x=90,y=570)


#conditioner
coimg=Image.open('mpcond.png')
rcoimg=coimg.resize((188,250))
condtk=ImageTk.PhotoImage(rcoimg)

cbutton=Button(root,text='  Conditioner  ', font=('Georgia', 16), bg='lavender', fg='black',bd=0,activeforeground='black'
           ,activebackground='lavender',cursor='hand2',image=condtk,
               command=cond)
cbutton.place(x=300,y=300)

cotxt=Label(root,text='  Conditioner  ', font=('Georgia', 16),bg='lavender', fg='black')
cotxt.place(x=330,y=570)


#Hairmask
hmimg=Image.open('mphm.png')
rhmimg=hmimg.resize((188,250))
hmtk=ImageTk.PhotoImage(rhmimg)

hmbutton=Button(root,text='  Hair Mask  ', font=('Georgia', 16), bg='lavender', fg='black',bd=0,activeforeground='black'
           ,activebackground='lavender',cursor='hand2',image=hmtk,
                command=hm)
hmbutton.place(x=550,y=300)

hmtxt=Label(root,text='  Hair Mask  ', font=('Georgia', 16),bg='lavender', fg='black')
hmtxt.place(x=580,y=570)

#Hair serum
hsimg=Image.open('mphs.png')
rhsimg=hsimg.resize((188,250))
hstk=ImageTk.PhotoImage(rhsimg)

hsbutton=Button(root,text='  Hair Serum  ', font=('Georgia', 16), bg='lavender', fg='black',bd=0,activeforeground='black'
           ,activebackground='lavender',cursor='hand2',image=hstk,
                command=hs)
hsbutton.place(x=800,y=300)

hstxt=Label(root,text='  Hair Serum  ', font=('Georgia', 16),bg='lavender', fg='black')
hstxt.place(x=830,y=570)


#Styling primer
spimg=Image.open('mpsp.png')
rspimg=spimg.resize((188,250))
sptk=ImageTk.PhotoImage(rspimg)

spbutton=Button(root,text='  Styling Primer  ', font=('Georgia', 16), bg='lavender', fg='black',bd=0,activeforeground='black'
           ,activebackground='lavender',cursor='hand2',image=sptk,
                command=sp)
spbutton.place(x=1050,y=300)

sptxt=Label(root,text='  Styling Primer  ', font=('Georgia', 16),bg='lavender', fg='black')
sptxt.place(x=1070,y=570)



root.mainloop()
