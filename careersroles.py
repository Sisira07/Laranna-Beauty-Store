import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox


root=Tk()
root.title("Careers")

root.iconbitmap(r'C:/Users/user/OneDrive/Documents/Sisira/Senior high-/Grade 12/Computer Project/final/favicon.ico')

#get wigth & height of screen
width=root.winfo_screenwidth()
height=root.winfo_screenheight()

#set screensize as fullscreen and not resizable
root.geometry("%dx%d"%(width,height))
root.resizable(True, False)


# Create a Canvas widget within a Frameher


def config_int(event):
    size=(my_frame.winfo_reqwidth(), my_frame.winfo_reqheight())
    canvas.config(scrollregion=(0,0,size[0],size[1]))
    if my_frame.winfo_reqwidth() != canvas.winfo_width():
        canvas.config(width=my_frame.winfo_reqwidth())

def config_can(event):
    if my_frame.winfo_reqwidth()!=canvas.winfo_width():
        canvas.itemconfigure(int_id,width=canvas.winfo_width())
        

scrollbar = ttk.Scrollbar(root, orient="vertical")
scrollbar.pack(side=tk.RIGHT, fill="y", expand=False)
canvas=tk.Canvas(root, bg='pink', width=0, height=0, yscrollcommand=scrollbar.set)
canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=canvas.yview)

my_frame=ttk.Frame(canvas)
my_frame.bind('<Configure>',config_int)
canvas.bind('<Configure>',config_can)
int_id=canvas.create_window((0,0),window=my_frame, anchor='nw')



for i in range(39):
    my_label=tk.Label(my_frame, text="")
    my_label.pack()


my_frame1=Frame(my_frame, bg="lavender")
my_frame1.pack(fill=BOTH , expand=True)




#mycart button( menu bar)
def finalbill():
    mboxm=messagebox.askyesno('Checkout','Do you want to proceed to checkout?')
    if mboxm:
        import mycart

def apply():
    root.destroy()
    import careers


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

        

#frame
frame1=Frame(my_frame)
frame1.place(x=0, y=0)

#1st statement
heading = Label(frame1, text='                                                                              WE BELIEVE ABOUT CHANGE, CREATE YOUR CUSTOM FORMULA WITH US, TODAY!'
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
                      activeforeground='lavender',bd=0,cursor='hand2')



#to change colour/font etc for drop down menu

MenuBttn3.place(x=550,y=56)



#Ingreadiants
MenuBttn4= Menubutton(my_frame, text = " INGREDIENTS ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2')


MenuBttn4.place(x=710,y=56)

#Reviews

MenuBttn5= Button(my_frame, text = "  CAREERS  ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2')


MenuBttn5.place(x=900,y=56)

#MYCART

MenuBttn6= Button(my_frame, text = "  MY CART  ", font=('Times New roman',12),relief = RAISED,
                      bg='LAVENDER',fg='DARKSLATEBLUE',activeforeground='darkslateblue',
                      activebackground='lavender',bd=0,cursor='hand2', command=finalbill)


MenuBttn6.place(x=1155,y=56)


#linking pages to the menubuttons




frame3= Frame(my_frame)
frame3.place(x=0,y=95)
imagebg = Image.open('careerbg.png')
imagetxt = Image.open('careerhead.png')

image1=Image.open('career1.png')
image2=Image.open('career2.png')
image3=Image.open('career3.png')
image4=Image.open('career4.png')

image1r=image1.resize((770,134))
image2r=image2.resize((435,146))
image3r=image3.resize((695,130))
image4r=image4.resize((500,137))
imagetxtr=imagetxt.resize((660,120))

imagebg.paste(imagetxtr, (30,25), imagetxtr)
# Convert the Image object into a TkPhoto object


imagebg.paste(image1r,(3,130),image1r)
imagebg.paste(image2r,(15,230),image2r)
imagebg.paste(image3r,(0,370),image3r)
imagebg.paste(image4r,(9,480),image4r)
tkimage = ImageTk.PhotoImage(imagebg)


panel1 = Label(frame3, image=tkimage)
panel1.grid(row=0, column=2, sticky=E)

r1=Button(frame3,text='         APPLY         ', command=apply,font=('Georgia', 17),bg='black',fg='thistle',bd=0,activeforeground='thistle'
           ,activebackground='black',cursor='hand2')
r1.place(x=950,y=165)

r2=Button(frame3,text='         APPLY         ', command=apply,font=('Georgia', 17),bg='black',fg='thistle',bd=0,activeforeground='thistle'
           ,activebackground='black',cursor='hand2')
r2.place(x=950,y=290)

r3=Button(frame3,text='         APPLY         ', command=apply,font=('Georgia', 17),bg='black',fg='thistle',bd=0,activeforeground='thistle'
           ,activebackground='black',cursor='hand2')
r3.place(x=950,y=410)

r4=Button(frame3,text='         APPLY         ',command=apply, font=('Georgia', 17),bg='black',fg='thistle',bd=0,activeforeground='thistle'
           ,activebackground='black',cursor='hand2')
r4.place(x=950,y=530)



root.mainloop()
