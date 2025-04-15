from tkinter import*
from PIL import Image

root=Tk()
root.geometry('800x550')
root.config(background='mistyrose')

gifImage='beautypic.gif'
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
    showanimation=root.after(50,lambda: animation(count))

gif_Label=Label(root,image='')
gif_Label.place(x=200, y=30, width=400,height=500)

animation(count)

root.mainloop()


    
