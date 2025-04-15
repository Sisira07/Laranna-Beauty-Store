import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk


root=Tk()
root.title("   Ingredients")

width=root.winfo_screenwidth()
height=root.winfo_screenheight()

#set screensize as fullscreen and not resizable
root.geometry("%dx%d"%(width,height))
root.resizable(True, False)

bg=Image.open("bg(ing).png")
resize_bgImage=bg.resize((width, 700))
bgImage= ImageTk.PhotoImage(resize_bgImage)
bgLabel= Label(root, image=bgImage)
bgLabel.image=bgImage
bgLabel.place(x=0, y=0)


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


#mycart button( menu bar)
def finalbill():
    messagebox.showinfo('                                                                              WE BELIEVE ABOUT CHANGE, CREATE YOUR CUSTOM FORMULA WITH US, TODAY!')
    
def abt():
    root.destroy()
    import about
    
#careers
def careers():
    root.destroy()
    import careerspage

#ingredients
def ing():
    root.destroy()
    import ingredients
        

#frame
framex=Frame(root)
framex.place(x=0, y=0)

#1st statement
heading = Label(framex, text='                                                                              WE BELIEVE ABOUT CHANGE, CREATE YOUR CUSTOM FORMULA WITH US, TODAY!'
                ,font=('Times New roman',12),anchor='w'
                , bg='lavender', fg='black', width=root.winfo_screenwidth(),height=2)
heading.grid(row=0, column=0)

#menubar
framey=Frame(root)
framey.place(x=0,y=45)

lname=Image.open('logomenu.png')
rlname=lname.resize((139,53))
nlname=ImageTk.PhotoImage(rlname)

imglabel=Label(root,image=nlname,bd=0, highlightthickness=0)
imglabel.place(x=25,y=45)

menu= Label(framey,bg='dark slate blue', width=root.winfo_screenwidth(),height=3)
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

#About
MenuBttn3= Button(root, text =" ABOUT ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2',command=abt)



#to change colour/font etc for drop down menu

MenuBttn3.place(x=550,y=56)



#Ingreadiants
MenuBttn4= Button(root, text = " INGREDIENTS ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2', command=ing)


MenuBttn4.place(x=700,y=56)

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


frame1=Frame(root, bg="#FFF6FC", width=width, height=140)
frame1.place(x=50, y=290)

frame2=Frame(root, bg="#FFF6FC", width=width, height=140)
frame2.place(x=50, y=410)

frame3=Frame(root, bg="#FFF6FC", width=width, height=140)
frame3.place(x=50, y=530)

#bg="#FFF6FC"
#FFF6FC
image_refs1 = {}                 #essential to display all the images otherwise only the last image will be displayed
#In this code, I've made sure to store the references to the ImageTk.PhotoImage objects in the image_refs dictionary to prevent them from being destroyed by the garbage collector.
images={"Anti Frizz":"acacia extract.png", "Deep Condition":"betaine.png", "Fix split ends":"beet root extract.png",
        "Hydrate":"blue green algae.png", "Shine":"Quinoa protein.png","Volumize":"sweet almond extract.png"}
for goal in images:

    img = Image.open(images[goal])
    img1 = img.resize((100, 100))  
    img2 = ImageTk.PhotoImage(img1)
    image_refs1[goal] = img2
    bgLabel2= Label(frame1, image=img2)
    bgLabel2.pack(side="left", padx=40, pady=0)
    
image_refs = {}
images1={"Strengthen":"Horsetail extract.png", "Colour protection":"soyabean extract.png", "Soothe scalp":"salicylic acid.png", "Straighten":"tamarind extract.png", "Moisturize":"argan oil.png", "Hydrate":"beet root extract.png",}
for goal1 in images1:
    img = Image.open(images1[goal1])
    img1 = img.resize((100, 100))  
    img2 = ImageTk.PhotoImage(img1)
    image_refs[goal1] = img2
    bgLabel1= Label(frame2, image=img2)
    bgLabel1.pack(side="left", padx=40, pady=0)
image_refs2 = {}
images2={ "Improve Elasticity":"cupuacu butter.png", "Exfoliate":"salicylic acid.png", "Smoothen":"apple extract.png", "Nourish":"grapeseed oil.png","Cleanse":"castor seed oil.png", "Soothe":"neem leaf extract.png"}
for goal2 in images2:
    img = Image.open(images2[goal2])
    img1 = img.resize((100, 100))  
    img2 = ImageTk.PhotoImage(img1)
    image_refs2[goal2] = img2
    bgLabel3= Label(frame3, image=img2)
    bgLabel3.pack(side="left", padx=40, pady=0)
root.mainloop()
