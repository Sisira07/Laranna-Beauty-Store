import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from ttkbootstrap.scrolled import ScrolledFrame
from tkinter import messagebox


root=Tk()
root.title("   Laranna")

root.iconbitmap(r'C:\Users\user\OneDrive\Documents\Sisira\Senior high-\Grade 12\Computer Project\login\favicon.ico')

#get wigth & height of screen
width=root.winfo_screenwidth()
height=root.winfo_screenheight()

#set screensize as fullscreen and not resizable
root.geometry("%dx%d"%(width,height))
root.resizable(True, False)

#scrollbar
my_frame= ScrolledFrame(root, autohide=False)
my_frame.pack(fill=BOTH , expand=YES)
#required to make the scrollbar work
my_frame1=Frame(my_frame, bg="lavender")
my_frame1.pack(fill=BOTH , expand=True)


#increase the range value to increase the length
for i in range(88):
    my_label=Label(my_frame1, text='', bg='pink')
    my_label.pack()





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


#mycart button( menu bar)
def finalbill():
    messagebox.showinfo('Welcome','Your cart is empty!, Start shopping by using the menubar or homepage!')
    

#careers
def careers():
    root.destroy
    import careerspage


        

#frame
frame1=Frame(my_frame)
frame1.place(x=0, y=0)

#1st statement
heading = Label(frame1, text='                                                                                  SUBSCRIBE & GET 20% OFF YOUR FIRST LARGE SHAMPOO + CONDITIONER!'
                ,font=('Times New roman',12),anchor='w'
                , bg='lavender', fg='black', width=root.winfo_screenwidth(),height=2,autostyle=False)
heading.grid(row=0, column=0)

#menubar
frame2=Frame(my_frame, autostyle=False)
frame2.place(x=0,y=45)

lname=Image.open('logomenu.png')
rlname=lname.resize((139,53))
nlname=ImageTk.PhotoImage(rlname)

imglabel=Label(my_frame,image=nlname,bd=0, highlightthickness=0, autostyle=False)
imglabel.place(x=25,y=45)

menu= Label(frame2,bg='dark slate blue', width=root.winfo_screenwidth(),height=3,  autostyle=False)
menu.grid(row=0,column=0)



    
#Hair


MenuBttn = Menubutton(my_frame, text = "          HAIR          ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activeforeground='lavender',
                      activebackground='darkslateblue',bd=0,cursor='hand2',autostyle=False)



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
                      activeforeground='lavender',bd=0,cursor='hand2', autostyle=False)

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
MenuBttn3= Menubutton(my_frame, text =" SKINCARE ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2', autostyle=False)

Var21 = StringVar()
Var22 = StringVar()
Var23 = StringVar()

Menu3 = Menu(MenuBttn3, tearoff = 0)

Menu3.add_radiobutton(label = "Serum", variable = Var21, value ='options1', command=skinb)
Menu3.add_radiobutton(label = "Moisturizer", variable = Var21, value ='options2', command=skinb)
Menu3.add_radiobutton(label = "Cleanser", variable = Var21, value ='options3', command=skinb)
Menu3.add_radiobutton(label = "Face Wash", variable = Var21, value ='options4', command=skinb)

MenuBttn3["menu"] = Menu3

#to change colour/font etc for drop down menu
Menu3.config(bg='lavender')

MenuBttn3.place(x=540,y=56)



#Ingreadiants
MenuBttn4= Button(my_frame, text = " INGREDIENTS ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2', autostyle=False)


MenuBttn4.place(x=710,y=56)

#Reviews

MenuBttn5=Button(my_frame, text = "  CAREERS  ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2', command=careers, autostyle=False)


MenuBttn5.place(x=900,y=56)

#MYCART

MenuBttn6=Button(my_frame, text = "  MY CART  ", font=('Times New roman',12),relief = RAISED,
                      bg='LAVENDER',fg='DARKSLATEBLUE',activeforeground='darkslateblue',
                      activebackground='lavender',bd=0,cursor='hand2', command=finalbill, autostyle=False)


MenuBttn6.place(x=1155,y=56)


#linking pages to the menubuttons







#1
frame3= Frame(my_frame, autostyle=False)
frame3.place(x=0,y=95)
imagebg = Image.open('hpbg.jpg')
imagetxt = Image.open('hp1.png')

imagebg.paste(imagetxt, (110,50), imagetxt)
# Convert the Image object into a TkPhoto object
tkimage = ImageTk.PhotoImage(imagebg)

panel1 = Label(frame3, image=tkimage, autostyle=False)
panel1.grid(row=0, column=2, sticky=E)

#gif
gifImage='b1.gif'
openImage=Image.open(gifImage)
frames=openImage.n_frames


imageObject=[PhotoImage(file=gifImage, format=f'gif -index {i}') for i in range(frames)]
count=0
showanimation=None


def animation(count):
    global showanimation
    newImage=imageObject[count]

    gif_Label.configure(image=newImage)
    count+=1
    if count==frames:
        count=0
    showanimation=my_frame.after(250,lambda: animation(count))

gif_Label=Label(my_frame,image='', autostyle=False)
gif_Label.place(x=825, y=95)

animation(count)

#button
cnf=Button(my_frame,text='  CREATE YOUR FORMULA ', font=('Georgia', 17),bg='black',fg='lemonchiffon',bd=0,activeforeground='lemonchiffon'
           ,activebackground='black',cursor='hand2', command=menupg, autostyle=False)
cnf.place(x=200,y=390)

#scrolling text
def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)

canvas=Canvas(my_frame,bg='lavender',width=root.winfo_screenwidth(),height=50, autostyle=False)
canvas.place(x=0,y=500)
text_var="100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested  - 100% Vegan  -  Paraben Free -  Cruelty Free  -  Dermatologist Tested - 100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested  - 100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested  - 100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested - "
text=canvas.create_text(0,-2000,text=text_var,font=('Microsoft Yahei UI Light',15,'bold'),fill='darkslateblue',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
fps=110   #Change the fps to make the animation faster/slower
shift()



#2

frame4= Frame(my_frame, autostyle=False)
frame4.place(x=0,y=549)
hpbg2 = Image.open('hpbg2.jpg')
hpbg3 = Image.open('hpbg3.png')

bgimg=hpbg2.copy()

bgimg.paste(hpbg3, (540,30), hpbg3)
# Convert the Image object into a TkPhoto object
hp2 = ImageTk.PhotoImage(bgimg)

panel2 = Label(frame4, image=hp2, autostyle=False)
panel2.grid(row=0, column=2, sticky=E)




#gif
gifImage1='hp2.gif'
openImage1=Image.open(gifImage1)
frames1=openImage1.n_frames


imageObject1=[PhotoImage(file=gifImage1, format=f'gif -index {i}') for i in range(frames1)]
count1=0
showanimation1=None


def animation1(count1):
    global showanimation1
    newImage1=imageObject1[count1]

    gif_Label1.configure(image=newImage1)
    count1+=1
    if count1==frames1:
        count1=0
    showanimation1=my_frame.after(250,lambda: animation1(count1))

gif_Label1=Label(my_frame,image='', autostyle=False)
gif_Label1.place(x=0, y=549)

animation1(count1)


#scrolling text
def shift1():
    x1,y1,x2,y2 = canvas1.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas1.winfo_width()
        y1 = canvas1.winfo_height()//2
        canvas1.coords("marquee",x1,y1)
    else:
        canvas1.move("marquee", -2, 0)
    canvas1.after(1000//fps1,shift1)

canvas1=Canvas(my_frame,bg='darkslateblue',width=root.winfo_screenwidth(),height=50, autostyle=False)
canvas1.place(x=0,y=1000)
text_var1="100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested  - 100% Vegan  -  Paraben Free -  Cruelty Free  -  Dermatologist Tested - 100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested  - 100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested  - 100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested - "
text1=canvas1.create_text(0,-2000,text=text_var,font=('Microsoft Yahei UI Light',15,'bold'),fill='lavender',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas1.bbox("marquee")
fps1=110   #Change the fps to make the animation faster/slower
shift1()


#3

frame5= Frame(my_frame, autostyle=False)
frame5.place(x=0,y=1050)
hpbg5=Image.open('hpbg.jpg')
hptxt4=Image.open('hptxt4.png')
bgimg1=hpbg5.copy()

bgimg1.paste(hptxt4, (315,25), hptxt4)

#stickers
stik1=Image.open("stik1.png")
rstik1=stik1.resize((90,92))
bgimg1.paste(rstik1,(100,50))

stik2=Image.open("stik2.png")
rstik2=stik2.resize((110,92))
bgimg1.paste(rstik2,(230,200))


stik3=Image.open("stik3.png")
rstik3=stik3.resize((110,108))
bgimg1.paste(rstik3,(870,170))

stik4=Image.open("stik4.png")
rstik4=stik4.resize((110,91))
bgimg1.paste(rstik4,(1000,290))

stik5=Image.open("stik5.png")
rstik5=stik5.resize((120,129))
bgimg1.paste(rstik5,(1100,80))

stik6=Image.open("stik6.png")
rstik6=stik6.resize((110,97))
bgimg1.paste(rstik6,(50,300))


# Convert the Image object into a TkPhoto object
hp3 = ImageTk.PhotoImage(bgimg1)

panel3 = Label(frame5, image=hp3, autostyle=False)
panel3.grid(row=0, column=2, sticky=E)


#Photoslider
pics_list=['hpic1.png', "hpic2.png","hpic3.png", "hpic4.png"]

index=0

def previousImage():
    global index, img
    index-=1

    if index < 0:
        index= len(pics_list) - 1



    img=Image.open(pics_list[index])
    img=ImageTk.PhotoImage(img)
    label1= Label(my_frame, image=img, bg='black',autostyle=False)
    label1.place(x=490,y=1200)
    
def nextImage():
    global index, img

    index+=1
    if index > len(pics_list) - 1:
        index=0

    img=Image.open(pics_list[index])
    img=ImageTk.PhotoImage(img)
    label1= Label(my_frame, image=img, bg='black', autostyle=False)
    label1.place(x=490,y=1200)


image1=Image.open("next.png")
resize_image1=image1.resize((50, 50))
img1=ImageTk.PhotoImage(resize_image1)
lbl_next=tk.Button(my_frame, image=img1, bd=0, bg='lemonchiffon', activebackground='lemonchiffon', cursor='hand2', command=nextImage, autostyle=False)


image2=Image.open("previous.png")
resize_image2=image2.resize((50, 50))
img2=ImageTk.PhotoImage(resize_image2)
lbl_previous=tk.Button(my_frame, image=img2, command=previousImage, bd=0, bg='lemonchiffon', activebackground='lemonchiffon', cursor='hand2',autostyle=False)


lbl_picture=tk.Label()



lbl_previous.place(x=435,y=1270)
lbl_next.place(x=790,y=1270)

nextImage()



#4
frame6= Frame(my_frame,autostyle=False)
frame6.place(x=0,y=1500)

hpbg6 = Image.open('hpbg6.jpg')
hp6txt = Image.open('hp6txt.jpg')

bgimg6=hpbg6.copy()

bgimg6.paste(hp6txt, (360,40))
# Convert the Image object into a TkPhoto object
hp6 = ImageTk.PhotoImage(bgimg6)

panel6 = Label(frame6, image=hp6, autostyle=False)
panel6.grid(row=0, column=2, sticky=E)

sn=Button(frame6,text='        SHOP NOW       ', font=('Georgia', 17),bg='mistyrose',fg='black',bd=0,activeforeground='black'
           ,activebackground='mistyrose',cursor='hand2', command=menupg, autostyle=False)
sn.place(x=530,y=240)


root.mainloop()
