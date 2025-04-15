import tkinter as tk
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

#scrollbar

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



for i in range(48):
    my_label=tk.Label(my_frame, text="", bg='white')
    my_label.pack()


#functions
def hairframe():
    root.destroy()
    import mphairf	

def bodyframe():
    root.destroy()
    import mpbodyf

def skinframe():
    root.destroy()
    import mpskinf

#title
mpf1= Frame(my_frame)
mpf1.place(x=0,y=0)
mpbg1 = Image.open('mpbg1.png')
mphead1 = Image.open('mphead1.png')

rmphead1=mphead1.resize((809,150))

mpbg1.paste(rmphead1, (250,30))
 # Convert the Image object into a TkPhoto object
mpimgtk = ImageTk.PhotoImage(mpbg1)

mp1lab = Label(mpf1, image=mpimgtk, bd=0,highlightthickness=0)
mp1lab.grid(row=0,column=2)



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

canvas1=Canvas(my_frame,bg='black',width=my_frame.winfo_screenwidth(),height=50, bd=0,highlightthickness=0)
canvas1.place(x=0,y=200)
text_var="100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested  - 100% Vegan  -  Paraben Free -  Cruelty Free  -  Dermatologist Tested - 100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested  - 100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested  - 100% Vegan  -  Paraben Free  -  Cruelty Free  -  Dermatologist Tested - "
text=canvas1.create_text(0,-2000,text=text_var,font=('Microsoft Yahei UI Light',15,'bold'),fill='azure',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas1.bbox("marquee")
fps=110   #Change the fps to make the animation faster/slower
shift()



#HAIR

mpf2= Frame(my_frame)
mpf2.place(x=0,y=250)
mpbg2 = Image.open('mpbg2.png')
mptxt2 = Image.open('mptxthair.png')

rmptxt2=mptxt2.resize((800,268))

mpbg2.paste(rmptxt2, (370,100))

Hairpic=Image.open("mphair.png")
rhairpic=Hairpic.resize((350,406))
mpbg2.paste(rhairpic,(0,0))

Hairhd=Image.open("mphairhd.png")
rhairhd=Hairhd.resize((300,126))
mpbg2.paste(rhairhd,(435,40))

 # Convert the Image object into a TkPhoto object
mpimg2tk = ImageTk.PhotoImage(mpbg2)

mp2lab = Label(mpf2, image=mpimg2tk, bd=0,highlightthickness=0)
mp2lab.grid(row=0,column=1,sticky=E)




button1=Button(my_frame,text='  Shop Haircare  ', font=('Georgia', 16), bg='black', fg='mediumpurple3',bd=0,activeforeground='mediumpurple2'
           ,activebackground='black',cursor='hand2', command=hairframe)
button1.place(x=500,y=570)

#BODY

mpf3= Frame(my_frame)
mpf3.place(x=0,y=656)
mpbg3 = Image.open('mpbg3.png')
mptxt3 = Image.open('mpbodytxt.png')

rmptxt3=mptxt3.resize((800,268))

mpbg3.paste(rmptxt3, (0,80))

bodypic=Image.open("mpbody.png")
rbodypic=bodypic.resize((531,370))
mpbg3.paste(rbodypic,(815,0))

bodyhd=Image.open("mpbodyhd.png")
rbodyhd=bodyhd.resize((300,127))
mpbg3.paste(rbodyhd,(83,30))

 # Convert the Image object into a TkPhoto object
mpimg3tk = ImageTk.PhotoImage(mpbg3)

mp3lab = Label(mpf3, image=mpimg3tk, bd=0,highlightthickness=0)
mp3lab.grid(row=0,column=1,sticky=E)


button2=Button(my_frame,text='  Shop Bodycare  ', font=('Georgia', 16), bg='black', fg='mediumpurple3',bd=0,activeforeground='mediumpurple2'
           ,activebackground='black',cursor='hand2', command=bodyframe)
button2.place(x=132,y=950)


#SKIN
mpf4= Frame(my_frame)
mpf4.place(x=0,y=1020)
mpbg4 = Image.open('mpbg4.png')
mptxt4 = Image.open('mpskintxt.png')

rmptxt4=mptxt4.resize((800,204))

mpbg4.paste(rmptxt4, (410,120))

skinpic=Image.open("mpskin.png")
rskinpic=skinpic.resize((409,370))
mpbg4.paste(rskinpic,(0,0))

skinhd=Image.open("mpskinhd.png")
rskinhd=skinhd.resize((300,142))
mpbg4.paste(rskinhd,(445,30))

 # Convert the Image object into a TkPhoto object
mpimg4tk = ImageTk.PhotoImage(mpbg4)

mp4lab = Label(mpf4, image=mpimg4tk, bd=0,highlightthickness=0)
mp4lab.grid(row=0,column=1,sticky=E)




button3=Button(my_frame,text='  Shop Skincare  ', font=('Georgia', 16), bg='black', fg='mediumpurple3',bd=0,activeforeground='mediumpurple2'
           ,activebackground='black',cursor='hand2', command=skinframe)
button3.place(x=500,y=1325)





root.mainloop()
