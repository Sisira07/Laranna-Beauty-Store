import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox


root=Tk()
root.title("   Laranna")

root.iconbitmap(r'C:/Users/user/OneDrive/Documents/Sisira/Senior high-/Grade 12/Computer Project/final/favicon.ico')

#get wigth & height of screen
width=root.winfo_screenwidth()
height=root.winfo_screenheight()

#set screensize as fullscreen and not resizable
root.geometry("%dx%d"%(width,height))
root.resizable(True, False)

#functions
def menupg():
    root.destroy()
    import menupage


def hairb():
    value=Var1.get()
    if value=='option1':
        root.destroy()
        import cshampoo
    elif value=='option2':
        root.destroy()
        import csconditioner
    elif value=='option3':
        root.destroy()
        import cshairserum
    elif value=='option4':
        root.destroy()
        import cshairmask
    elif value=='option5':
        root.destroy()
        import csstylingprimer

def bodyb():
    value=Var11.get()
    if value=='optiona':
        root.destroy()
        import csbw
    elif value=='optionb':
        root.destroy()
        import cshowergel
    elif value=='optionc':
        root.destroy()
        import csbl
    elif value=='optiond':
        root.destroy()
        import csbodyscrub

def skinb():
    value=Var21.get()
    if value=='options1':
        root.destroy()
        import csskinserum
    elif value=='options2':
        root.destroy()
        import csmoisturizer
    elif value=='options3':
        root.destroy()
        import cscleanser
    elif value=='options4':
        root.destroy()
        import csfw

def abt():
    root.destroy()
    import about
def ing():
    root.destroy()
    import ingredients
#mycart button( menu bar)
def finalbill():
    messagebox.showinfo('Welcome','Your cart is empty!, Start shopping by using the menubar or homepage!')
    

#careers
def careers():
    root.destroy()
    import careerspage


        

#frame
frame1=Frame(root)
frame1.place(x=0, y=0)

#1st statement
heading = Label(frame1, text='                                                                              WE BELIEVE ABOUT CHANGE, CREATE YOUR CUSTOM FORMULA WITH US, TODAY!'
                ,font=('Times New roman',12),anchor='w'
                , bg='lavender', fg='black', width=root.winfo_screenwidth(),height=2)
heading.grid(row=0, column=0)

#menubar
frame2=Frame(root)
frame2.place(x=0,y=45)

lname=Image.open('logomenu.png')
rlname=lname.resize((139,50))
nlname=ImageTk.PhotoImage(rlname)

imglabel=Label(root,image=nlname,bd=0, highlightthickness=0)
imglabel.place(x=25,y=45)

menu= Label(frame2,bg='dark slate blue', width=root.winfo_screenwidth(),height=3)
menu.grid(row=0,column=0)



    
#Hair


MenuBttn = Menubutton(root, text = "          HAIR          ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activeforeground='lavender',
                      activebackground='darkslateblue',bd=0,cursor='hand2')



Var1=StringVar()
Var2=StringVar()
Var3=StringVar()

Menu1 = Menu(MenuBttn, tearoff = 0)

Menu1.add_radiobutton(label = "Shampoo", variable =Var1, value ='option1', command=hairb)
Menu1.add_radiobutton(label = "Conditioner", variable = Var1, value = 'option2', command=hairb)
Menu1.add_radiobutton(label = "Hair Serum", variable = Var1, value = 'option3', command=hairb)
Menu1.add_radiobutton(label = "Hair Mask", variable = Var1, value = 'option4', command=hairb)
Menu1.add_radiobutton(label = "Styling Primer", variable = Var1, value = 'option5', command=hairb)

MenuBttn["menu"] = Menu1
#to change colour/font etc for drop down menu
Menu1.config(bg='lavender')

MenuBttn.place(x=240,y=56)

#Body
MenuBttn2 = Menubutton(root, text = "          BODY         ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2')

Var11 = StringVar()
Var12 = StringVar()
Var13 = StringVar()

Menu2 = Menu(MenuBttn2, tearoff = 0)

Menu2.add_radiobutton(label = "Body Wash", variable = Var11, value ='optiona', command=bodyb)
Menu2.add_radiobutton(label = "Shower gel", variable = Var11, value ='optionb',command=bodyb)
Menu2.add_radiobutton(label = "Body Lotion", variable = Var11, value ='optionc', command=bodyb)
Menu2.add_radiobutton(label = "Body Scrub", variable = Var11, value ='optiond', command=bodyb)

MenuBttn2["menu"] = Menu2

#to change colour/font etc for drop down menu
Menu2.config(bg='lavender')


MenuBttn2.place(x=370,y=56)

#Skin
MenuBttn3= Button(root, text =" ABOUT ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2', command=abt)



#to change colour/font etc for drop down menu

MenuBttn3.place(x=550,y=56)




#Ingreadiants
MenuBttn4= Button(root, text = " INGREDIENTS ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2',command=ing)


MenuBttn4.place(x=710,y=56)

#Reviews

MenuBttn5=Button(root, text = "  CAREERS  ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2', command=careers)


MenuBttn5.place(x=900,y=56)

#MYCART

MenuBttn6=Button(root, text = "  MY CART  ", font=('Times New roman',12),relief = RAISED,
                      bg='LAVENDER',fg='DARKSLATEBLUE',activeforeground='darkslateblue',
                      activebackground='lavender',bd=0,cursor='hand2', command=finalbill)


MenuBttn6.place(x=1155,y=56)


#linking pages to the menubuttons
frame4= Frame(root)
frame4.place(x=0,y=90)
hpbg2 = Image.open('hpbg2.jpg')
hpbg3 = Image.open('hpbg3.png')
rhpbg3=hpbg3.resize((800,511))



bgimg=hpbg2.copy()

bgimg.paste(rhpbg3, (5,10), rhpbg3)
# Convert the Image object into a TkPhoto object
hp2 = ImageTk.PhotoImage(bgimg)

panel2 = Label(frame4, image=hp2)
panel2.grid(row=0, column=2, sticky=E)

shaming=Image.open('abt.png')
rshaming=shaming.resize((460,330))
tkshaming=ImageTk.PhotoImage(rshaming)
labeling= Label(frame4, image=tkshaming, bg='pink', fg='black')
labeling.place(x=760,y=160)


root.mainloop()
