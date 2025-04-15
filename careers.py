import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
from email_validator import validate_email, EmailNotValidError

root=Tk()
root.title("   Careers")

root.iconbitmap(r'C:/Users/user/OneDrive/Documents/Sisira/Senior high-/Grade 12/Computer Project/final/favicon.ico')

width=root.winfo_screenwidth()
height=root.winfo_screenheight()

#set screensize as fullscreen and not resizable
root.geometry("%dx%d"%(width,height))
root.resizable(True, False)

bg=Image.open("bg(career).png")
resize_bgImage=bg.resize((width, 650))
bgImage= ImageTk.PhotoImage(resize_bgImage)
bgLabel= Label(root, image=bgImage)
bgLabel.image=bgImage
bgLabel.place(x=0, y=0)

def back():
    root.destroy()
    import careersroles
    
def validate_email_format(email):
    try:
        valid = validate_email(email)
        email_address = valid.email
        return email_address
    except EmailNotValidError:
        return None


def submit():
    global email
    email = email_entry.get()
    validated_email = validate_email_format(email)
   
    if fname_entry.get()=='' or lname_entry.get()=='' or str(date.get())=='' or str(email_entry.get())=='' or str(phone_entry.get())=='' or str(job_combo1.get())=='':
        messagebox.showerror("Error",'All field Are Required')
    elif len(str(phone_entry.get()))!=11:
        messagebox.showerror("Error",'Enter valid phone number!')
    elif validated_email==None:
        messagebox.showerror("Error",'Invalid email format')
        
    else:
        fname =str(fname_entry.get())
        lname = str(lname_entry.get())
        dob = str(date.get())
        email = str(email_entry.get())
        phone = str(phone_entry.get())
        experience = str(experience_entry.get())
        job = str(job_combo1.get())
        s=' '
        skills = str(skill_text.get("1.0", "end-1c"))
        t=str(fname+s+lname+s+dob+s+email+s+phone+s+experience+s+job+s+skills+'\n')
        myfile=open('Record.txt', 'a')
        myfile.write(t)
        myfile.close()
        messagebox.showinfo("Submitted",'Application submitted successfully!')
    

font1= ('Times New roman', 23, 'bold')
font2=('Times New roman', 21)
font3=('Times New roman', 14, 'bold')


fname_label = Label(root, text="First Name:", font=font1, bg='#FFF7EF')
fname_label.place(x=600, y=126)
fname_entry = Entry(root, font=font2, width=20, bd=1)
fname_entry.place(x=960, y=126)

lname_label = Label(root, text="Last Name:", font=font1, bg='#FFF7EF')
lname_label.place(x=600, y=184)
lname_entry = Entry(root, font=font2, width=20, bd=1)
lname_entry.place(x=960, y=184)


dob_label = Label(root, text="Date of Birth:", font=font1, bg='#FFF7EF')
dob_label.place(x=600, y=242)
date= DateEntry(root, font=font3, width=27, bd=0, bg='#FFF7EF' )
date.place(x=960, y=242)

email_label = Label(root, text="Email:", font=font1, bg='#FFF7EF')
email_label.place(x=600, y=300)
email_entry = Entry(root, font=font2, width=20, bd=1)
email_entry.place(x=960, y=303)

phone_label = Label(root, text="Phone Number:", font=font1, bg='#FFF7EF')
phone_label.place(x=600, y=358)
phone_entry = Entry(root, font=font2, width=20, bd=1)
phone_entry.place(x=960, y=360)

experience_label = Label(root, text="Experience:", font=font1, bg='#FFF7EF')
experience_label.place(x=600, y=414)
experience_entry = Entry(root, font=font2, width=20, bd=1)
experience_entry.place(x=960, y=417)

job_label= tk.Label(root, text="Job Title: ",font=font1, bg='#FFF7EF')
job_label.place(x=600, y=473)
job=["Equipment Cleaning Technician", "Brand Designer", "Social Content Producer","Retention Manager" ]
job_combo1=ttk.Combobox(root, values=job,font=font2, width=19)
job_combo1.place(x=960, y=476)

skill_label = Label(root, text="Skills:",font=font1, bg='#FFF7EF')
skill_label.place(x=600, y=530)
skill_text = Text(root, height=2, width=29, font=font3)
skill_text.place(x=960, y=530)

submit_button=Button(root,cursor='hand2', command=submit, text="SUBMIT", font=('Times', 20, 'bold'), bg='#8BB4AC', bd=0, width=22, activebackground='#8BB4AC')
submit_button.place(x=920, y=594)

back=Button(root,cursor='hand2', command=back, text="BACK", font=('Times', 20, 'bold'), bg='#8BB4AC', bd=0, width=28, activebackground='#8BB4AC')
back.place(x=10, y=595)
       

root.mainloop()
