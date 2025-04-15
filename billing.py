from tkinter import *
from tkinter import messagebox
import PIL as p
import PIL.ImageTk as ptk
import os
from datetime import datetime

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
my_frame= ScrolledFrame(root, autohide=False)
my_frame.pack(fill=BOTH , expand=YES)
#required to make the scrollbar work
my_frame1=Frame(my_frame, bg="lavender")
my_frame1.pack(fill=BOTH , expand=True)


file=open('bill.txt','a+')




root.mainloop()
