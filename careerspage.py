import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
#from ttkbootstrap.scrolled import ScrolledFrame
from tkinter import messagebox


my_frame=Tk()
my_frame.title("Careers")

my_frame.iconbitmap(r'C:/Users/user/OneDrive/Documents/Sisira/Senior high-/Grade 12/Computer Project/final/favicon.ico')

#get wigth & height of screen
width=my_frame.winfo_screenwidth()
height=my_frame.winfo_screenheight()

#set screensize as fullscreen and not resizable
my_frame.geometry("%dx%d"%(width,height))
my_frame.resizable(True, False)

'''#scrollbar
my_frame=ScrolledFrame(my_frame, autohide=False)
my_frame.pack(fill=BOTH , expand=YES)
#required to make the scrollbar work
my_frame1=Frame(my_frame, bg="lavender")
my_frame1.pack(fill=BOTH , expand=True)


#increase the range value to increase the length
for i in range(32):
    my_label=Label(my_frame1, text='', bg='pink')
    my_label.pack()'''

def careersroles():
    my_frame.destroy()
    import careersroles


def hairb():
    value=Var1.get()
    if value=='option1':
        my_frame.destroy()
        import cshampoo
    elif value=='option2':
        my_frame.destroy()
        import csconditioner
    elif value=='option3':
        my_frame.destroy()
        import cshairserum
    elif value=='option4':
        my_frame.destroy()
        import cshairmask
    elif value=='option5':
        my_frame.destroy()
        import csstylingprimer

def bodyb():
    value=Var11.get()
    if value=='optiona':
        my_frame.destroy()
        import csbw
    elif value=='optionb':
        my_frame.destroy()
        import cshowergel
    elif value=='optionc':
        my_frame.destroy()
        import csbl
    elif value=='optiond':
        my_frame.destroy()
        import csbodyscrub
        
#mycart button( menu bar)

def finalbill():
    messagebox.showinfo('Welcome','Your cart is empty!, Start shopping by using the menubar or homepage!')
    

#careers
def careers():
    my_frame.destroy()
    import careerspage

#ingredients
def ing():
    my_frame.destroy()
    import ingredients

def abt():
    my_frame.destroy()
    import about
    
#frame
frame1=Frame(my_frame)
frame1.place(x=0, y=0)

#1st statement
heading = Label(frame1, text='                                                                                  SUBSCRIBE & GET 20% OFF YOUR FIRST LARGE SHAMPOO + CONDITIONER!'
                ,font=('Times New roman',12),anchor='w'
                , bg='lavender', fg='black', width=my_frame.winfo_screenwidth(),height=2)
heading.grid(row=0, column=0)

#menubar
frame2=Frame(my_frame)
frame2.place(x=0,y=45)

lname=Image.open('logomenu.png')
rlname=lname.resize((139,50))
nlname=ImageTk.PhotoImage(rlname)

imglabel=Label(my_frame,image=nlname,bd=0, highlightthickness=0)
imglabel.place(x=25,y=45)

menu= Label(frame2,bg='dark slate blue', width=my_frame.winfo_screenwidth(),height=3)
menu.grid(row=0,column=0)



    
#Hair


MenuBttn = Menubutton(my_frame, text = "          HAIR          ", font=('Times New roman',12),relief = RAISED,
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
MenuBttn2 = Menubutton(my_frame, text = "          BODY         ", font=('Times New roman',12),relief = RAISED,
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

#About
MenuBttn3= Button(my_frame, text =" ABOUT ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2', command=abt)


#to change colour/font etc for drop down menu

MenuBttn3.place(x=550,y=56)


#Ingreadiants
MenuBttn4=Button(my_frame, text = " INGREDIENTS ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2', command=ing)


MenuBttn4.place(x=710,y=56)

#Reviews

MenuBttn5= Button(my_frame, text = "  CAREERS  ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2', command=careers)


MenuBttn5.place(x=900,y=56)

#MYCART

MenuBttn6=Button(my_frame, text = "  MY CART  ", font=('Times New roman',12),relief = RAISED,
                      bg='LAVENDER',fg='DARKSLATEBLUE',activeforeground='darkslateblue',
                      activebackground='lavender',bd=0,cursor='hand2', command=finalbill)


MenuBttn6.place(x=1155,y=56)


#linking pages to the menubuttons




frame3= Frame(my_frame)
frame3.place(x=0,y=95)
imagebg = Image.open('careerbg.png')
imagetxt = Image.open('careerhead.png')
imagetxt2=Image.open('careertxt.png')
imagetxtr=imagetxt.resize((498,110))
imagetxt2r=imagetxt2.resize((520,243))
image1=Image.open('careerpic1.png')
image1r=image1.resize((570,380))

imagebg.paste(imagetxtr, (50,50), imagetxtr)
imagebg.paste(image1r,(610,80))
imagebg.paste(imagetxt2r, (40,140),imagetxt2r)
# Convert the Image object into a TkPhoto object
tkimage = ImageTk.PhotoImage(imagebg)

panel1 = Label(frame3, image=tkimage)
panel1.grid(row=0, column=2, sticky=E)

#button
roles=Button(frame3,text='              VIEW OPEN ROLES                 ', font=('Georgia', 17),bg='black',fg='thistle',bd=0,activeforeground='thistle'
           ,activebackground='black',cursor='hand2',command=careersroles)
roles.place(x=90,y=400)



my_frame.mainloop()
