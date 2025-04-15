import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from ttkbootstrap.scrolled import ScrolledFrame
import os
import product_data

root=Tk()
root.title("   Laranna")

#root.iconbitmap(r'C:\Users\user\OneDrive\Documents\Sisira\Senior high-\Grade 12\Computer Project\login\favicon.ico')

#get wigth & height of screen
width=root.winfo_screenwidth()
height=root.winfo_screenheight()

#set screensize as fullscreen and not resizable
root.geometry("%dx%d"%(width,height))
root.resizable(True, False)

bg=Image.open("bg(cart).png")
resize_bgImage=bg.resize((width, 700))
bgImage= ImageTk.PhotoImage(resize_bgImage)
bgLabel= Label(root, image=bgImage)
bgLabel.place(x=0, y=0)
bgLabel.image=bgImage


#label1=Label(root,bg='#F6E9DA',width=40)
#headlabel=Label(root,text='BILL', font=('Georgia', 25), bg='#F6E9DA', width=40)
#headlabel.pack()
label2=Label(root,text="Here are your customized products: ", bg='#F6E9DA', font=('Georgia', 17))
label2.place(x=30, y=170)

frame= Frame(root,bg='#F6E9DA')
frame.place(x=500, y=170)
file1 = open('bill.txt', 'r')  # Open the file in read mode
text1 = file1.readlines()
x = len(text1)
for i in range(x):
    billlabel = Label(frame, text=text1[i], font=('Georgia', 14), bg='#F6E9DA')
    billlabel.pack(side="top", padx=4, pady=0)  # Adjust the pady value to your preference
file1.close()
os.remove('bill.txt')
c=product_data.count_p()

label3=Label(root, text=c ,bg='#F1C0FF', font=('Georgia', 27))
label3.place(x=470, y=529)
label4=Label(root, text='$' ,bg='#F1C0FF', font=('Georgia', 27))
label4.place(x=430, y=529)

product_data.delete_product()

root.mainloop()
