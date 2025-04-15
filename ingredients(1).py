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
resize_bgImage=bg.resize((width, 600))
bgImage=ImageTk.PhotoImage(resize_bgImage)
bgLabel=Label(root, image=bgImage)
bgLabel.image=resize_bgImage
bgLabel.place(x=0, y=0)

stik1=Image.open("acacia extract.png")
rstik1=stik1.resize((200,203))
bg.paste(rstik1,(10,100))


hp3 = ImageTk.PhotoImage(bg)

panel3=Label(root, image=hp3)
panel3.grid(row=0, column=2, sticky=E)


#FFF6FC

root.mainloop()
