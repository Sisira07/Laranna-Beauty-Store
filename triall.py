from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame




root=Tk()
root.title("Home Page")

root.iconbitmap(r'C:\Users\user\OneDrive\Documents\Sisira\Senior high-\Grade 12\Computer Project\login\favicon.ico')

#get wigth & height of screen
width=root.winfo_screenwidth()
height=root.winfo_screenheight()

#set screensize as fullscreen and not resizable
root.geometry("%dx%d"%(width,height))
root.resizable(True, False)

#scrllbar
my_frame= ScrolledFrame(root, autohide=False)
my_frame.pack(fill=BOTH, expand=YES)
#required to make the scrollbar work
my_frame1=Frame(my_frame)
my_frame1.grid(row=200, column=0)
for i in range(200):
    my_label=Label(my_frame1, text='')
    my_label.pack()



#frame
frame1=Frame(my_frame)
frame1.place(x=0, y=0)

#1st statement
heading = Label(frame1, text='                                                                                  SUBSCRIBE & GET 20% OFF YOUR FIRST LARGE SHAMPOO + CONDITIONER!'
                ,font=('Times New roman',12),anchor='w', bg='lavender', fg='black', width=root.winfo_screenwidth(), height=2)
heading.grid(row=0, column=0)

#menubar
frame2=Frame(my_frame)
frame2.place(x=0,y=45)
menu= Label(frame2, bg='dark slate blue', width=root.winfo_screenwidth(),height=3)
menu.grid(row=0,column=0)

#Hair
MenuBttn = Menubutton(my_frame, text = "          HAIR          ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activeforeground='lavender',
                      activebackground='darkslateblue',bd=0,cursor='hand2')

Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()

Menu1 = Menu(MenuBttn, tearoff = 0)

Menu1.add_radiobutton(label = "Shampoo", variable = Var1, value = 1)
Menu1.add_radiobutton(label = "Conditioner", variable = Var1, value = 2)
Menu1.add_radiobutton(label = "Hair Serum", variable = Var1, value = 3)
Menu1.add_radiobutton(label = "Hair Mask", variable = Var1, value = 4)
Menu1.add_radiobutton(label = "Styling Primer", variable = Var1, value = 5)

MenuBttn["menu"] = Menu1
#to change colour/font etc for drop down menu
Menu1.config(bg='lavender')

MenuBttn.place(x=240,y=56)

#Body
MenuBttn2 = Menubutton(my_frame, text = "          BODY         ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2')

Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()

Menu2 = Menu(MenuBttn2, tearoff = 0)

Menu2.add_radiobutton(label = "Body Wash", variable = Var1, value = 1)
Menu2.add_radiobutton(label = "Shower gel", variable = Var1, value = 2)
Menu2.add_radiobutton(label = "Body Lotion", variable = Var1, value = 3)
Menu2.add_radiobutton(label = "Body Scrub", variable = Var1, value = 4)
Menu2.add_radiobutton(label = "Soaps", variable = Var1, value = 5)

MenuBttn2["menu"] = Menu2

#to change colour/font etc for drop down menu
Menu2.config(bg='lavender')


MenuBttn2.place(x=370,y=56)

#Skin
MenuBttn3= Menubutton(my_frame, text =" SKINCARE ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2')

Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()

Menu3 = Menu(MenuBttn3, tearoff = 0)

Menu3.add_radiobutton(label = "Serum", variable = Var1, value = 1)
Menu3.add_radiobutton(label = "Moisturizer", variable = Var1, value = 2)
Menu3.add_radiobutton(label = "Cleanser", variable = Var1, value = 3)
Menu3.add_radiobutton(label = "Face Wash", variable = Var1, value = 4)

MenuBttn3["menu"] = Menu3

#to change colour/font etc for drop down menu
Menu3.config(bg='lavender')

MenuBttn3.place(x=540,y=56)

#Ingreadiants
MenuBttn4= Menubutton(my_frame, text = " INGREDIENTS ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2')


MenuBttn4.place(x=710,y=56)

#Reviews

MenuBttn5= Menubutton(my_frame, text = "  REVIEWS  ", font=('Times New roman',12),relief = RAISED,
                      bg='dark slate blue',fg='white',activebackground='darkslateblue',
                      activeforeground='lavender',bd=0,cursor='hand2')


MenuBttn5.place(x=900,y=56)

#MYCART

MenuBttn6= Menubutton(my_frame, text = "  MY CART  ", font=('Times New roman',12),relief = RAISED,
                      bg='LAVENDER',fg='DARKSLATEBLUE',activeforeground='darkslateblue',
                      activebackground='lavender',bd=0,cursor='hand2')


MenuBttn6.place(x=1170,y=56)




#1
frame3= Frame(my_frame)
frame3.place(x=0,y=95)
imagebg = Image.open('hpbg.jpg')
imagetxt = Image.open('hp1.png')

imagebg.paste(imagetxt, (110,50), imagetxt)
# Convert the Image object into a TkPhoto object
tkimage = ImageTk.PhotoImage(imagebg)

panel1 = Label(frame3, image=tkimage)
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
    showanimation=root.after(250,lambda: animation(count))

gif_Label=Label(my_frame,image='')
gif_Label.place(x=825, y=95)

animation(count)

#button
cnf=Button(my_frame,text='  Create your Formula Here ', font=('Microsoft Yahei UI Light',18,'bold'),bg='black',fg='lemonchiffon',bd=0,activeforeground='lemonchiffon'
           ,activebackground='black',cursor='hand2')
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

canvas=Canvas(my_frame,bg='lavender',width=root.winfo_screenwidth(),height=50)
canvas.place(x=0,y=500)
text_var="100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested  - 100% Vegan  -  Paraben Free -  Cruelty Free  -  Dermatologist Tested - 100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested  - 100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested  - 100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested - "
text=canvas.create_text(0,-2000,text=text_var,font=('Microsoft Yahei UI Light',15,'bold'),fill='darkslateblue',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
fps=110   #Change the fps to make the animation faster/slower
shift()



#2
frame4=Frame(my_frame)
frame4.place(x=0,y=549)
hpbg2=Image.open('hpbg2.jpg')
hp2=ImageTk.PhotoImage(hpbg2)

panel2=Label(frame4, image=hp2)
panel2.grid(row=0,column=0)




root.mainloop()

