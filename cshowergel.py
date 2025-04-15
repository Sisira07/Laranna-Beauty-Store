import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.title("   Shower Gel ")

root.iconbitmap(r'C:/Users/user/OneDrive/Documents/Sisira/Senior high-/Grade 12/Computer Project/final/favicon.ico')

#get wigth & height of screen
width=root.winfo_screenwidth()
height=root.winfo_screenheight()

#set screensize as fullscreen and not resizable
root.geometry("%dx%d"%(width,height))
root.resizable(True, False)

# scrollbar Create a Canvas widget within a Frameher


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

my_frame=tk.Frame(canvas, bg='white')
my_frame.bind('<Configure>',config_int)
canvas.bind('<Configure>',config_can)
int_id=canvas.create_window((0,0),window=my_frame, anchor='nw')



for i in range(45):
    my_label=tk.Label(my_frame, text="", bg='white')
    my_label.pack()

#click_bind
def click_bind(e):
    if cval.get()=='16oz                                                  ':
        price_label.config(text='$32.00')
    elif cval.get()=='10oz                                                   ':
        price_label.config(text='$23.00')

#mycart button( menu bar)
def finalbill():
    mboxm=messagebox.askyesno('Checkout','Do you want to proceed to checkout?')
    if mboxm:
        import mycart
#careers
def careers():
    root.destroy()
    import careerspage

#ingredients
def ing():
    root.destroy()
    import ingredients

def abt():
    root.destroy()
    import about
    
def bquiz():
    root.destroy()
    import bodyquiz

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
        

#coupon
frame1=Frame(my_frame)
frame1.place(x=0, y=0)

heading = Label(frame1, text='                                                                              WE BELIEVE ABOUT CHANGE, CREATE YOUR CUSTOM FORMULA WITH US, TODAY!'
                ,font=('Times New roman',12),anchor='w'
                , bg='lavender', fg='black', width=root.winfo_screenwidth(),height=2)
heading.grid(row=0, column=0)


#menubar
frame2=Frame(my_frame)
frame2.place(x=0,y=45)
lname=Image.open('logomenu.png')
rlname=lname.resize((137,46))
nlname=ImageTk.PhotoImage(rlname)

imglabel=Label(my_frame,image=nlname,bd=0, highlightthickness=0)
imglabel.place(x=25,y=45)

menu= Label(frame2,bg='dark slate blue', width=root.winfo_screenwidth(),height=3, bd=0,highlightthickness=0)
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

#Skin
MenuBttn3= Button(my_frame, text =" ABOUT ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2',command=abt)



#to change colour/font etc for drop down menu

MenuBttn3.place(x=550,y=56)




#Ingreadiants
MenuBttn4= Button(my_frame, text = " INGREDIENTS ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2',command=ing)


MenuBttn4.place(x=710,y=56)

#Reviews

MenuBttn5=Button(my_frame, text = "  CAREERS  ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2',command=careers)


MenuBttn5.place(x=900,y=56)

#MYCART

MenuBttn6=Button(my_frame, text = "  MY CART  ", font=('Times New roman',12),relief = RAISED,
                      bg='LAVENDER',fg='DARKSLATEBLUE',activeforeground='darkslateblue',
                      activebackground='lavender',bd=0,cursor='hand2', command=finalbill)


MenuBttn6.place(x=1155,y=56)

#----------------------------------------------






#Photoslider
pics_list=['showergel2.jpg','showergel1.jpg','showergel.jpg']

index=0


def previousImage():
    global index, img
    index-=1

    if index < 0:
        index= len(pics_list) - 1



    img=Image.open(pics_list[index])
    img=img.resize((430, 400))
    img= ImageTk.PhotoImage(img)
    label1= Label(my_frame, image=img, bg='black',bd=0,highlightthickness=0)
    label1.place(x=53,y=110)
    
def nextImage():
    global index, img

    index+=1
    if index > len(pics_list) - 1:
        index=0

    img=Image.open(pics_list[index])
    img=img.resize((430, 400))
    img= ImageTk.PhotoImage(img)
    label1= Label(my_frame, image=img, bg='black',bd=0,highlightthickness=0)
    label1.place(x=53,y=110)


image1=Image.open("next.jpg")
resize_image1=image1.resize((50, 50))
img1= ImageTk.PhotoImage(resize_image1)
lbl_next=tk.Button(my_frame, image=img1, bd=0, bg='white', activebackground='white', cursor='hand2', command=nextImage)


image2=Image.open("previous.jpg")
resize_image2=image2.resize((50, 50))
img2= ImageTk.PhotoImage(resize_image2)
lbl_previous=tk.Button(my_frame, image=img2, command=previousImage, bd=0, bg='white', activebackground='white', cursor='hand2')


lbl_picture=tk.Label()



lbl_previous.place(x=3,y=300)
lbl_next.place(x=483,y=300)

nextImage()

#Title

sghead=Image.open('sghead.png')
sgtk=ImageTk.PhotoImage(sghead)
sglab=Label(my_frame, image=sgtk, bd=0, highlightthickness=0)
sglab.place(x=535,y=120)


#select quantity

label5= Label(my_frame, text="Select Quantity:  ", font=('Georgia', 19), bg='white', fg='black')
label5.place(x=565,y=220)


values=['10oz                                                   ',
        '16oz                                                  ']
cval=tk.StringVar()
cval.set(values[0])

qty=OptionMenu(my_frame, cval, *values,command=click_bind)
qty.config(bg='white',fg='black', activeforeground='black', activebackground='white',
           bd=0, width=30, cursor='hand2')
qty['menu'].config(bg='white', activeforeground='black', activebackground='lavender',bd=0)
qty['highlightthickness']=0
qty.pack()
qty.place(x=565,y=290)

price_label=Label(my_frame, text='$23.00', font=('Microsoft Yahei UI Light', 22,'bold'), bg='white', fg='black')
price_label.place(x=870,y=280)


create_button= Button(my_frame, text='CREATE YOUR FORMULA', font=('Times new roman', 20), bg='black' , fg='white', activebackground='black',
                      activeforeground='white',width=26,cursor='hand2', command=bquiz)
create_button.place(x=565,y=370)




#scrolling text
def shift():
    x1,y1,x2,y2 = canvas1.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas1.winfo_width()
        y1 = canvas1.winfo_height()//2
        canvas1.coords("marquee",x1,y1)
    else:
        canvas1.move("marquee", -2, 0)
    canvas1.after(1000//fps,shift)

canvas1=Canvas(my_frame,bg='lavender',width=my_frame.winfo_screenwidth(),height=50,bd=0, highlightthickness=0)
canvas1.place(x=0,y=530)
text_var="100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested  - 100% Vegan  -  Paraben Free -  Cruelty Free  -  Dermatologist Tested - 100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested  - 100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested  - 100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested - "
text=canvas1.create_text(0,-2000,text=text_var,font=('Microsoft Yahei UI Light',15,'bold'),fill='darkslateblue',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas1.bbox("marquee")
fps=110   #Change the fps to make the animation faster/slower
shift()


#Key benefits
label2= Label(my_frame, text="Key Benefits  ", font=('Times New Roman', 24),bg='white', fg='Black')
label2.place(x=20,y=600)

insert_text= """
- Moisturizing effects with exfoliation
    
"""
label3= Label(my_frame, text=insert_text, font=('Georgia', 14), bg='white', fg='black')
label3.place(x=20,y=640, anchor='nw')

insert_text1= """
- Rehydrates Dry Skin
    
"""
label4= Label(my_frame, text=insert_text1, font=('Georgia', 14), bg='white', fg='black')
label4.place(x=20,y=700, anchor='nw')



#prod desc
label4= Label(my_frame, text="Key Ingrediants  ", font=('Times New Roman', 24),bg='white', fg='Black')
label4.place(x=670,y=600)


bwing=Image.open('bodying.png')
rbwing=bwing.resize((397,100))
tkbwing=ImageTk.PhotoImage(rbwing)
labeling= Label(my_frame, image=tkbwing, bg='white', fg='black')
labeling.place(x=645,y=650)



root.mainloop()
