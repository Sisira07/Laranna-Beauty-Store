import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
from ttkbootstrap.scrolled import ScrolledFrame
from mysql.connector import (connection)
from tkinter import messagebox

one=Tk()
one.grid()
one.title("Hair Quiz")
width=one.winfo_screenwidth()
height=one.winfo_screenheight()


#set screensize as fullscreen and not resizable
one.geometry("%dx%d"%(width,height))
one.resizable(True, False)



#scrollbar
window=ScrolledFrame(one, autohide=False)
window.pack(fill=BOTH , expand=YES)
#required to make the scrollbar work
w1=Frame(window, bg="lavender")
w1.pack(fill=BOTH , expand=True)


#increase the range value to increase the length
for i in range(35):
    my_label=Label(w1, text='', bg='pink')
    my_label.pack()



    


#placing background image,      if i put height as screen size (height) it doesn't come properly
bg=Image.open("bg8.png")
resize_bgImage=bg.resize((width, 700))
bgImage= ImageTk.PhotoImage(resize_bgImage)


bgLabel= Label(window, image=bgImage, autostyle=False)
bgLabel.place(x=0, y=0)
#idk why this is req
# Make sure the image doesn't get garbage collected
bgLabel.img = bgImage

#-----------------------------------------------------------------------------------------------------------
#database connection
cnx = connection.MySQLConnection(user='root', password='sisira@dl07', host='localhost', database='ingredients')
mycursor=cnx.cursor()
#---------------------functions to display the images for each product-------------------------------------------------------
clicked_buttons1=set()
def button_clicked1(button_num):
    clicked_buttons1.add(button_num)
    
def show_result_button1():
    if len(clicked_buttons1) == 0:
        messagebox.showinfo("Message", "Please select atleast one option")
    else:
        show_ingredients()
def shampoo_colours():
    global radio_button1, image_refs1, radio_var_s, shampoo_image
    k=1
    image_refs1 = {}                 #essential to display all the images otherwise only the last image will be displayed
    #In this code, I've made sure to store the references to the ImageTk.PhotoImage objects in the image_refs dictionary to prevent them from being destroyed by the garbage collector.
    radio_var_s = StringVar()
    shampoo_image={"blue":"blue_s.png", "pink":"pink_s.png", "green":"green_s.png", "orange":"orange_s.png", "white":"white_s.png" }
    for colour in shampoo_image:

        img = Image.open(shampoo_image[colour])
        img1 = img.resize((100, 200))  
        img2 = ImageTk.PhotoImage(img1)
        image_refs1[colour] = img2
        radio_button1=ttk.Radiobutton(frame_s, variable=radio_var_s, value=colour, image=img2, command=lambda: button_clicked1(k))
        radio_button1.image = img2
        radio_button1.pack(side="left", padx=20, pady=60)
        k+=1 
def conditioner_colours():
    global radio_button2, radio_var_c, image_refs2, conditioner_image
    k=1
    image_refs2 = {}                 #essential to display all the images otherwise only the last image will be displayed
    #In this code, I've made sure to store the references to the ImageTk.PhotoImage objects in the image_refs dictionary to prevent them from being destroyed by the garbage collector.
    radio_var_c = StringVar()
    conditioner_image={"blue":"c_blue.png", "green":"c_green.png", "white":"c_white.png", "pink":"c_pink.png", "orange":"c_orange.png"}
    for colour in conditioner_image:

        img = Image.open(conditioner_image[colour])
        img1 = img.resize((100, 200))  
        img2 = ImageTk.PhotoImage(img1)
        image_refs2[colour] = img2
        radio_button2=ttk.Radiobutton(frame_c, variable=radio_var_c, value=colour, image=img2, command=lambda: button_clicked1(k))
        radio_button2.image = img2
        radio_button2.pack(side="left", padx=20, pady=60)
        k+=1

def serum_colours():
    global radio_button3, radio_var_se
    k=1               #essential to display all the images otherwise only the last image will be displayed
    #In this code, I've made sure to store the references to the ImageTk.PhotoImage objects in the image_refs dictionary to prevent them from being destroyed by the garbage collector.
    radio_var_se = StringVar()
    #conditioner_image={"blue":"c_blue.png", "green":"c_green.png", "white":"c_white.png", "pink":"c_pink.png", "orange":"c_orange.png"}
    #for colour in conditioner_image:

    img = Image.open("hair_serum.jpg")
    img1 = img.resize((120, 220))  
    img3 = ImageTk.PhotoImage(img1)
    radio_button3=ttk.Radiobutton(frame_se, variable=radio_var_se, value="Hair Serum", image=img3, command=lambda: button_clicked1(k))
    radio_button3.image = img3
    radio_button3.pack(side="left", padx=200, pady=60)
    k+=1

def mask_colours():
    global radio_button4, radio_var_m, image_refs4, mask_image
    k=1
    image_refs4 = {}                 #essential to display all the images otherwise only the last image will be displayed
    #In this code, I've made sure to store the references to the ImageTk.PhotoImage objects in the image_refs dictionary to prevent them from being destroyed by the garbage collector.
    radio_var_m = StringVar()
    mask_image={"green":"m_green.png", "lavender":"m_lavender.png", "peach":"m_peach.png", "white":"m_white.png"}
    for colour in mask_image:

        img = Image.open(mask_image[colour])
        img1 = img.resize((170, 170))  
        img4 = ImageTk.PhotoImage(img1)
        image_refs4[colour] = img4
        radio_button4=ttk.Radiobutton(frame_m, variable=radio_var_m, value=colour, image=img4, command=lambda: button_clicked1(k))
        radio_button4.image = img4
        radio_button4.pack(side="left", padx=18, pady=60)
        k+=1

def primer_colours():
    global radio_button5, radio_var_p,frame_px
    k=1
    radio_var_p = StringVar()
    #mask_image={"green":"m_green.png", "lavender":"m_lavender.png", "peach":"m_peach.png", "white":"m_white.png"}
    #for colour in mask_image:

    img = Image.open("primer.jpg")
    img1 = img.resize((120, 220))  
    img5 = ImageTk.PhotoImage(img1)
    radio_button5=ttk.Radiobutton(frame_px, variable=radio_var_p, value="Primer", image=img5, command=lambda: button_clicked1(k))
    radio_button5.image = img5
    radio_button5.pack(side="left", padx=200, pady=60)
    k+=1
#------------------===================changing the function of next button==================-------------------------------------------------------------------
def next_button_clicked1():
    global current_frame
    if current_frame==frame10 and selected_count>=1:
        next_product_frame()
        current_frame=frame6
    else:
        if len(clicked_buttons1) == 0:
            messagebox.showinfo("Message", "Please select atleast one option")
        elif len(clicked_buttons1) >= 1:
            next_product_frame()
        
        

index2=0
def next_product_frame():
    global product_frame_current, index2, index1,clicked_buttons1,current_frame
    index2+=1
    progress.pack_forget()
    current_frame=frame6
    current_frame.pack_forget()     #hide the current frame
    #product_frame_current=product_frame_list[0]
    product_frame_current.pack_forget()
    progress1.pack()
    clicked_buttons1.clear()
    product_frame_current=product_frame_list[(product_frame_list.index(product_frame_current)+1)% len(product_frame_list)]#move to next frame
    progress1["value"] = (index2 + 1) * 100 / len(product_frame_list)

    if product_frame_current==product_frame_list[len(product_frame_list)-1]:
        next1.place_forget()
        show_result.place(x=805, y=540)

    product_frame_current.pack()
     


#---------------------selected products--------------------------------------------------------------------------------------
def check_checkbox1(index9):                  
    check_vars9[index9].set(1)
    update_selected_count1()

def update_selected_count1():                                        #dealing with checkboxes----disabling after 5 selections
    global  selected_count1
    selected_count1 = sum(var9.get() for var9 in check_vars9)
    if selected_count1==0:
        messagebox.showinfo("Message", "Please select atleast 1 product")
    elif  selected_count1>=1:
        show_selected_product()
    

def show_selected_product():
    global frame_s, a, product_frame_list, product_frame_current, selected_products,selected_count1
    selected_options9 = [options_p[j] for j, var9 in enumerate(check_vars9) if var9.get() == 1]
    #---------#selected products---------
    selected_products=[f"{option9}" for option9 in selected_options9]
    #next1.config(command=next_product_frame)
    

    product_frame_list=[frame10]
    #for a in range(len(selected_products)):
    for product in selected_products:
        if product=="Shampoo":
            product_frame_list.append(frame_s)

        elif product=="Conditioner":
            product_frame_list.append(frame_c)

        elif product=="Hair Serum":
            product_frame_list.append(frame_se)

        elif product=="Hair Mask":
            product_frame_list.append(frame_m)

        elif product=="Styling Primer":
            product_frame_list.append(frame_px)

    product_frame_current=product_frame_list[0]
    next1.config(command=next_button_clicked1)
    show_result.config(command=show_result_button1)
#---------------------------selected goals-------------------------------------------------------------------------------
def check_checkbox(index):                  
    check_vars[index].set(1)
    update_selected_count()

def update_selected_count():                                        #dealing with checkboxes----disabling after 5 selections
    global  selected_count
    selected_count = sum(var.get() for var in check_vars)
    for index, checkbox in enumerate(checkboxes):
        if selected_count >=5:
            checkbox.config(state="disabled")
        else:
            checkbox.config(state="normal")

    if selected_count == 5:
        messagebox.showinfo("Message", "You have selected 5 goals!")
        nextFrame()
    elif selected_count==0:
        messagebox.showinfo("Message", "Please select atleast 1 goal")
    #elif selected_count>=1:
        #nextFrame()

#-----------------------------------------------------------------------------------------------------------
def show_selected_options():                        #displaying the selected goals in the ingredients page
    global selected_goals
    selected_options = [options[i] for i, var in enumerate(check_vars) if var.get() == 1]
    formatted_text = "\n\n".join([f"• {option}" for option in selected_options])

    #---------#selected goals---------
    selected_goals=[f"{option}" for option in selected_options]
    g_label.config(text=formatted_text)
#-----------------------------------------------------------------------------------------
def show_ingredients():                     
    global bgImage, final, g_label, in_frame2                   #removing the already placed things from the window
    progress.pack_forget()
    next1.place_forget()
    #back.place_forget()
    big_frame.pack_forget()
    current_frame.pack_forget()
    show_result.place_forget()

    #----------------R E S U L T    P A G E    I N G E D I E N T S ----------------------------------
    bg6=Image.open("bg6.png")
    resize_bgImage6=bg6.resize((width, 700))
    bgImage= ImageTk.PhotoImage(resize_bgImage6)
    bgLabel.config(image=bgImage)
    
    in_frame2=Frame(window, width=100, bg='#afecee', autostyle=False)
    in_frame2.pack(side="left", padx=10, pady=200)
    
    g_label=Label(window, bg="#d4fcff", height=0, width=0, justify="left", font=('Georgia', 20), autostyle=False)
    g_label.pack(side="right", padx=112)
    

    #next button
    final=Button(window, text="NEXT",font=('Georgia', 24), bd=0, fg="white", bg="black",
                 activebackground="black", activeforeground="black", command=finalpg, autostyle=False)
    final.place(x=1085, y=575)
    
    show_selected_options()
    
    for goal in selected_goals:                         #retriving the image paths from the database
        query= (
            "SELECT image1 FROM shampoo1 WHERE goal=%s")
        
        mycursor.execute(query, (goal,))
        #to get all the images .....it will be a tuple inside a list [(image1.png, image2.png,....etc)]
        image_path=mycursor.fetchall()
        #for accessing the tuple
        for i in image_path:
            #for accessing the image path one at a time and it will be placed side by side
            for k in i:
                img = Image.open(k)
                img = img.resize((165, 170))  
                img = ImageTk.PhotoImage(img)
                ing_label = Label(in_frame2, image=img)
                ing_label.image = img  # Keep a reference to avoid garbage collection
                ing_label.pack(side="left", padx=4)       

    cnx.close()


#---------------------------------------Add to cart------------------------------


def shamcart():
    file1=open('bill.txt','a+')
    mbox=messagebox.askyesno('Confirmation','Add to cart? (Once added cannot be removed)')
    if mbox:
        messagebox.showinfo('','Successfully added to cart!')
        if quantity_combo1.get()=='16oz':
            file1.write('Custom Shampoo (16 oz)  -  $27.00')
            file1.write('\n')
        elif quantity_combo1.get()=='8oz':
            file1.write('Custom Shampoo (8 oz)  -  $21.00')
            file1.write('\n')
            
def condcart():
    file1=open('bill.txt','a+')
    mbox2=messagebox.askyesno('Confirmation','Add to cart? (Once added cannot be removed)')
    if mbox2:
        messagebox.showinfo('','Successfully added to cart!')
        if quantity_combo2.get()=='16oz':
            file1.write('Custom Conditioner (16 oz)  -  $27.00')
            file1.write('\n')
        elif quantity_combo2.get()=='8oz':
            file1.write('Custom Conditioner (8 oz)  -  $21.00')
            file1.write('\n')

def secart():
    file1=open('bill.txt','a+')
    mbox3=messagebox.askyesno('Confirmation','Add to cart? (Once added cannot be removed)')
    if mbox3:
        messagebox.showinfo('','Successfully added to cart!')
        if quantity_combo3.get()=='5oz':
            file1.write('Hair Serum (5 oz)  -  $31.00')
            file1.write('\n')
        elif quantity_combo3.get()=='3oz':
            file1.write('Hair Serum (3 oz)  -  $29.00')
            file1.write('\n')

def mcart():
    file1=open('bill.txt','a+')
    mbox4=messagebox.askyesno('Confirmation','Add to cart? (Once added cannot be removed)')
    if mbox4:
        messagebox.showinfo('','Successfully added to cart!')
        if quantity_combo4.get()=='5oz':
            file1.write('Hair Mask (5 oz)  -  $20.00')
            file1.write('\n')
        elif quantity_combo4.get()=='7oz':
            file1.write('Hair Mask (7 oz)  -  $24.00')
            file1.write('\n')

def spcart():
    file1=open('bill.txt','a+')
    mbox5=messagebox.askyesno('Confirmation','Add to cart? (Once added cannot be removed)')
    if mbox5:
        messagebox.showinfo('','Successfully added to cart!')
        if quantity_combo5.get()=='4oz':
            file1.write('Styling Primer (4 oz)  -  $24.00')
            file1.write('\n')
        elif quantity_combo5.get()=='6oz':
            file1.write('Styling Primer (6 oz)  -  $29.00')
            file1.write('\n')

#mycart button( menu bar)
def finalbill():
    mboxm=messagebox.askyesno('Checkout','Do you want to proceed to checkout?')
    if mboxm:
        import mycart





    
#-----------------------------------------------------------------------------------------
#click_bind                             to change the price when quantity is changed
def click_bind1(e):
    if quantity_combo1.get()=='16oz':
        price_label1.config(text='$27.00')
    elif quantity_combo1.get()=='8oz':
        price_label1.config(text='$21.00')

def click_bind2(e):
    if quantity_combo2.get()=='16oz':
        price_label2.config(text='$27.00')
    elif quantity_combo2.get()=='8oz':
        price_label2.config(text='$21.00')

def click_bind3(e):
    if quantity_combo3.get()=='5oz':
        price_label3.config(text='$31.00')
    elif quantity_combo3.get()=='3oz':
        price_label3.config(text='$29.00')

def click_bind4(e):
    if quantity_combo4.get()=='5oz':
        price_label4.config(text='$20.00')
    elif quantity_combo4.get()=='7oz':
        price_label4.config(text='$24.00')

def click_bind5(e):
    if quantity_combo5.get()=='4oz':
        price_label5.config(text='$24.00')
    elif quantity_combo5.get()=='6oz':
        price_label5.config(text='$29.00')
#----------------------------------------------------------------------------------------
def next_product():
    global final_frame_current, index1, final_frame_list
    final_frame_current.pack_forget()
    final_frame_current=final_frame_list[(final_frame_list.index(final_frame_current)+1)% len(final_frame_list)]#move to next frame

    if final_frame_current==final_frame_list[len(final_frame_list)-1]:
        next3.place_forget()
    final_frame_current.pack()
#----------------------------------------------------------------------------------------
def finalpg():
    global bgImage, bgLabel, final_big, final_s, label_s2, quantity_combo1, quantity_combo2, price_label1,price_label2,style, final_c, label_c2, selected_products, final_frame_list, final_frame_current, next3
    in_frame2.pack_forget()
    g_label.pack_forget()
    final.place_forget()

    bg7=Image.open("bg100.png")
    resize_bgImage7=bg7.resize((width, 700))
    bgImage= ImageTk.PhotoImage(resize_bgImage7)
    bgLabel.config(image=bgImage)
    
    
    #-------------------------------F I N A L     P A G E------------------------------------------
    final_big=Frame(window, width=1000, height=500, bg="#eae9f1", autostyle=False)
    next3=Button(window, text="NEXT",font=('Georgia', 25), bd=0, width=17, fg="white", bg="black",
                 activebackground="black", activeforeground="black", command=next_product, autostyle=False)
    next3.place(x=864, y=613)

    #final_s
    final_s=Frame(final_big, width=1000, height=500, bg="#eae9f1", autostyle=False)
    #final_s.pack()

    bg20=Image.open("trial_s1.png")
    resize_bgImage20=bg20.resize((1000, 500))
    s_bgImage= ImageTk.PhotoImage(resize_bgImage20)
    #label_s1
    label_s1=Label(final_s, image=s_bgImage, bg="#eae9f1", autostyle=False)
    label_s1.image=s_bgImage
    label_s1.place(x=0, y=0)
    label_s2=Label(final_s,width=200, height=300, autostyle=False)
    label_s2.place(x=60, y=195)

    #1 add to basket button
    add_to_basket=Button(final_s, text="ADD TO BASKET",font=('Georgia', 25), bd=0,
                         width=14, fg="white", bg="black", activebackground="black", activeforeground="black", command=shamcart, autostyle=False)
    add_to_basket.place(x=579, y=430)
    
    #price label
    price_label1=Label(final_s, text='$21.00', font=('Microsoft Yahei UI Light', 21,'bold'), bg='#caebda', fg='black', autostyle=False)
    price_label1.place(x=905, y=62)

    

    #option menu 
    quantity=["8oz", "16oz"]

    quantity_combo1=tk.StringVar()
    quantity_combo1.set(quantity[0])


    qty=OptionMenu(final_s, quantity_combo1, *quantity,command=click_bind1, autostyle=False)
    qty.config(bg='#caebda',fg='black', activeforeground='black', activebackground='#caebda',
           bd=0, width=45, cursor='hand2')
    qty['menu'].config(bg='#caebda', activeforeground='black', activebackground='SkyBlue1', bd=0)
    qty['highlightthickness']=0
    qty.pack()
    qty.place(x=580, y=62)


    style.configure("TButton", padding=2, relief="flat", background="#f1c0ff", foreground="black", font=('Georgia', 25), bd=0, width=15)
    frag=["Aquatic", "Floral", "Fruity", "Fragrance free"]
    for i in range(len(frag)):
        frag_button=ttk.Button(final_s, text=frag[i])
        frag_button.place(x=580, y=180 + i*65, width=260, height=40)
    shampoo_final()
    #---------------------------final_c--------------------------------------------------------------------------------------------------------------------
    #final_c
    final_c=Frame(final_big, width=1000, height=500, bg="#eae9f1", autostyle=False)
    #final_c.pack()

    bg19=Image.open("trial_c.png")
    resize_bgImage19=bg19.resize((1000, 500))
    c_bgImage= ImageTk.PhotoImage(resize_bgImage19)
    #label_c1
    label_c1=Label(final_c, image=c_bgImage, bg="#eae9f1", autostyle=False)
    label_c1.image=c_bgImage
    label_c1.place(x=0, y=0)
    label_c2=Label(final_c,width=200, height=300, autostyle=False)
    label_c2.place(x=60, y=195)

    #2 add to basket button
    add_to_basket2=Button(final_c, text="ADD TO BASKET",font=('Georgia', 25), bd=0, width=13, fg="white",
                          bg="black", activebackground="black", activeforeground="black", command=condcart, autostyle=False)
    add_to_basket2.place(x=618, y=423)
    
    #price label
    price_label2=Label(final_c, text='$21.00', font=('Microsoft Yahei UI Light', 20,'bold'), bg='#caebda', fg='black', autostyle=False)
    price_label2.place(x=910, y=50)

    

    #option menu 
    quantity2=["8oz", "16oz"]

    quantity_combo2=tk.StringVar()
    quantity_combo2.set(quantity2[0])


    qty2=OptionMenu(final_c, quantity_combo2, *quantity2,command=click_bind2, autostyle=False)
    qty2.config(bg='#caebda',fg='black', activeforeground='black', activebackground='#caebda',
           bd=0, width=45, cursor='hand2')
    qty2['menu'].config(bg='#caebda', activeforeground='black', activebackground='SkyBlue1', bd=0)
    qty2['highlightthickness']=0
    qty2.pack()
    qty2.place(x=580, y=62)

    style.configure("TButton", padding=2, relief="flat", background="#f1c0ff", foreground="black", font=('Georgia', 25), bd=0, width=15)
    frag=["Aquatic", "Floral", "Fruity", "Fragrance free"]
    for i in range(len(frag)):
        frag_button=ttk.Button(final_c, text=frag[i])
        frag_button.place(x=610, y=170 + i*65, width=260, height=40)
    conditioner_final()


    #-----------------------------final_se------------------------------------------------------------------------------------------------------------------
    global final_se, se_bgImage, label_se2, price_label3, quantity_combo3
    #final_se
    final_se=Frame(final_big, width=1000, height=500, bg="#eae9f1", autostyle=False)
    #final_se.pack()

    bg18=Image.open("trial_se.png")
    resize_bgImage18=bg18.resize((1000, 500))
    se_bgImage= ImageTk.PhotoImage(resize_bgImage18)
    #label_se1
    label_se1=Label(final_se, image=se_bgImage, bg="#eae9f1", autostyle=False)
    label_se1.image=c_bgImage
    label_se1.place(x=0, y=0)
    label_se2=Label(final_se,width=200, height=300, autostyle=False)
    label_se2.place(x=60, y=195)

    #3 add to basket button
    add_to_basket3=Button(final_se, text="ADD TO BASKET",font=('Georgia', 25), bd=0, width=13,
                          fg="white", bg="black", activebackground="black", activeforeground="black", command=secart, autostyle=False)
    add_to_basket3.place(x=610, y=423)
    
    #price label
    price_label3=Label(final_se, text='$29.00', font=('Microsoft Yahei UI Light', 20,'bold'), bg='#caebda', fg='black', autostyle=False)
    price_label3.place(x=910, y=53)

    style = ttk.Style()
    style.configure("TCombobox", padding=5, relief="flat", background="#caebda", foreground="black", autostyle=False)
    style.map("TCombobox", fieldbackground=[("readonly", "#caebda")])

    #option menu 
    quantity3=["3oz", "5oz"]

    quantity_combo3=tk.StringVar()
    quantity_combo3.set(quantity[0])


    qty3=OptionMenu(final_se, quantity_combo3, *quantity3,command=click_bind3, autostyle=False)
    qty3.config(bg='#caebda',fg='black', activeforeground='black', activebackground='#caebda',
           bd=0, width=45, cursor='hand2')
    qty3['menu'].config(bg='#caebda', activeforeground='black', activebackground='SkyBlue1', bd=0)
    qty3['highlightthickness']=0
    qty3.pack()
    qty3.place(x=580, y=62)

    style.configure("TButton", padding=2, relief="flat", background="#f1c0ff", foreground="black", font=('Georgia', 25), bd=0, width=15, autostyle=False)
    frag=["Aquatic", "Floral", "Fruity", "Fragrance free"]
    for i in range(len(frag)):
        frag_button=ttk.Button(final_se, text=frag[i])
        frag_button.place(x=610, y=172 + i*65, width=260, height=40)
    serum_final()

     #-----------------------------final_m------------------------------------------------------------------------------------------------------------------
    global final_m, m_bgImage, label_m2, price_label4, quantity_combo4
    #final_m
    final_m=Frame(final_big, width=1000, height=500, bg="#eae9f1", autostyle=False)
    #final_se.pack()

    bg17=Image.open("trial_m.png")
    resize_bgImage17=bg17.resize((1000, 500))
    m_bgImage= ImageTk.PhotoImage(resize_bgImage17)
    #label_m1
    label_m1=Label(final_m, image=m_bgImage, bg="#eae9f1", autostyle=False)
    label_m1.image=m_bgImage
    label_m1.place(x=0, y=0)
    label_m2=Label(final_m,width=200, height=300, bg="#eae9f1", autostyle=False)
    label_m2.place(x=60, y=195)

    #4 add to basket button
    add_to_basket4=Button(final_m, text="ADD TO BASKET",font=('Georgia', 25), bd=0, width=13,
                          fg="white", bg="black", activebackground="black", activeforeground="black", command=mcart, autostyle=False)
    add_to_basket4.place(x=604, y=425)
    
    #price label
    price_label4=Label(final_m, text='$20.00', font=('Microsoft Yahei UI Light', 20,'bold'), bg='#caebda', fg='black', autostyle=False)
    price_label4.place(x=910, y=56)



    #option menu 
    quantity4=["5oz", "7oz"]

    quantity_combo4=tk.StringVar()
    quantity_combo4.set(quantity4[0])


    qty4=OptionMenu(final_m, quantity_combo4, *quantity4,command=click_bind4, autostyle=False)
    qty4.config(bg='#caebda',fg='black', activeforeground='black', activebackground='#caebda',
           bd=0, width=45, cursor='hand2')
    qty4['menu'].config(bg='#caebda', activeforeground='black', activebackground='SkyBlue1', bd=0)
    qty4['highlightthickness']=0
    qty4.pack()
    qty4.place(x=580, y=62)

    style.configure("TButton", padding=2, relief="flat", background="#f1c0ff", foreground="black", font=('Georgia', 25), bd=0, width=15)
    frag=["Aquatic", "Floral", "Fruity", "Fragrance free"]
    for i in range(len(frag)):
        frag_button=ttk.Button(final_m, text=frag[i])
        frag_button.place(x=602, y=175 + i*65, width=260, height=40)
    mask_final()

    #-----------------------------final_px------------------------------------------------------------------------------------------------------------------
    global final_p, p_bgImage, label_p2, price_label5, quantity_combo5
    #final_m
    final_p=Frame(final_big, width=1000, height=500, bg="#eae9f1", autostyle=False)
    #final_se.pack()

    bg16=Image.open("trial_p.png")
    resize_bgImage16=bg16.resize((1000, 500))
    p_bgImage= ImageTk.PhotoImage(resize_bgImage16)
    #label_p1
    label_p1=Label(final_p, image=p_bgImage, bg="#eae9f1", autostyle=False)
    label_p1.image=p_bgImage
    label_p1.place(x=0, y=0)
    label_p2=Label(final_p,width=200, height=300, bg="#eae9f1", autostyle=False)
    label_p2.place(x=60, y=195)

    #5 add to basket button
    add_to_basket5=Button(final_p, text="ADD TO BASKET",font=('Georgia', 25), bd=0, width=13, fg="white",
                         bg="black", activebackground="black", activeforeground="black", command=spcart, autostyle=False)
    add_to_basket5.place(x=604, y=425)
    
    #price label
    price_label5=Label(final_p, text='$24.00', font=('Microsoft Yahei UI Light', 20,'bold'), bg='#caebda', fg='black', autostyle=False)
    price_label5.place(x=907, y=55)



    #option menu 
    quantity5=["4oz", "6oz"]

    quantity_combo5=tk.StringVar()
    quantity_combo5.set(quantity5[0])


    qty5=OptionMenu(final_p, quantity_combo5, *quantity5,command=click_bind5, autostyle=False)
    qty5.config(bg='#caebda',fg='black', activeforeground='black', activebackground='#caebda',
           bd=0, width=45, cursor='hand2')
    qty5['menu'].config(bg='#caebda', activeforeground='black', activebackground='SkyBlue1', bd=0)
    qty5['highlightthickness']=0
    qty5.pack()
    qty5.place(x=580, y=62)

    style.configure("TButton", padding=2, relief="flat", background="#f1c0ff", foreground="black", font=('Georgia', 25), bd=0, width=15)
    frag=["Aquatic", "Floral", "Fruity", "Fragrance free"]
    for i in range(len(frag)):
        frag_button=ttk.Button(final_p, text=frag[i])
        frag_button.place(x=602, y=173 + i*65, width=260, height=40)
    primer_final()
    
    if len(selected_products)==1:
        next3.place_forget()
    final_frame_list=[]
    for k in selected_products:
        if k=="Shampoo":
            final_frame_list.append(final_s)

        elif k=="Conditioner":
            final_frame_list.append(final_c)

        elif k=="Hair Serum":
            final_frame_list.append(final_se)

        elif k=="Hair Mask":
            final_frame_list.append(final_m)

        elif k=="Styling Primer":
            final_frame_list.append(final_p)
    final_big.pack(pady=100)
    final_frame_current=final_frame_list[0]
    final_frame_current.pack()
    
    
    
def shampoo_final():
    global label_s2, img_s1, final_s, label, s_bgImage
    shampoo_value= radio_var_s.get()                     #to get colour from the image selected to display on the final page
    for choice in shampoo_image:
        if choice==shampoo_value:
            img = Image.open(shampoo_image[choice])
            img1 = img.resize((200, 300))  
            img_s1 = ImageTk.PhotoImage(img1)
            label_s2.config(image=img_s1)
            label_s2.image=img_s1

def conditioner_final():
    global label_c2, img_c1
    conditioner_value= radio_var_c.get()                     #to get colour from the image selected to display on the final page
    for choice in conditioner_image:
        if choice==conditioner_value:
            img = Image.open(conditioner_image[choice])
            img1 = img.resize((200, 300))  
            img_c1 = ImageTk.PhotoImage(img1)
            label_c2.config(image=img_c1)
            label_c2.image=img_c1

def serum_final():
    global label_se2, img_se1
    serum_value= radio_var_se.get()                     #to get colour from the image selected to display on the final page
    #for choice in conditioner_image:
        #if choice==conditioner_value:
    img = Image.open("hair_serum.jpg")
    img1 = img.resize((200, 300))  
    img_se1 = ImageTk.PhotoImage(img1)
    label_se2.config(image=img_se1)
    label_se2.image=img_se1

def mask_final():
    global label_m4, img_m4
    mask_value= radio_var_m.get()                     #to get colour from the image selected to display on the final page
    for choice in mask_image:
        if choice==mask_value:
            img = Image.open(mask_image[choice])
            img1 = img.resize((210, 210))  
            img_m1 = ImageTk.PhotoImage(img1)
            label_m2.config(image=img_m1)
            label_m2.image=img_m1

def primer_final():
    global label_p2, img_p1
    primer_value= radio_var_p.get()                     #to get colour from the image selected to display on the final page
    #for choice in conditioner_image:
        #if choice==conditioner_value:
    img = Image.open("primer.jpg")
    img1 = img.resize((200, 300))  
    img_p1 = ImageTk.PhotoImage(img1)
    label_p2.config(image=img_p1)
    label_p2.image=img_p1
#--------------------------------------------------------------------------------- 

def menubar():

    #menubar
    frame2=Frame(window, autostyle=False)
    frame2.place(x=0,y=45)
    menu= Label(frame2,bg='dark slate blue', width=window.winfo_screenwidth(),height=3, autostyle=False)
    menu.grid(row=0,column=0)

    #Hair
    MenuBttn = Menubutton(window, text = "          HAIR          ", font=('Times New roman',12),relief = RAISED,
                          bg='dark slate blue',fg='white',activeforeground='lavender',
                          activebackground='darkslateblue',bd=0,cursor='hand2', autostyle=False)

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
    MenuBttn2 = Menubutton(window, text = "          BODY         ", font=('Times New roman',12),relief = RAISED,
                          bg='dark slate blue',fg='white',activebackground='darkslateblue',
                          activeforeground='lavender',bd=0,cursor='hand2', autostyle=False)

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
    MenuBttn3= Menubutton(window, text =" SKINCARE ", font=('Times New roman',12),relief = RAISED,
                          bg='dark slate blue',fg='white',activebackground='darkslateblue',
                          activeforeground='lavender',bd=0,cursor='hand2', autostyle=False)

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
    MenuBttn4= Menubutton(window, text = " INGREDIENTS ", font=('Times New roman',12),relief = RAISED,
                          bg='dark slate blue',fg='white',activebackground='darkslateblue',
                          activeforeground='lavender',bd=0,cursor='hand2', autostyle=False)


    MenuBttn4.place(x=710,y=56)

    #Reviews

    MenuBttn5= Menubutton(window, text = "  CAREERS  ", font=('Times New roman',12),relief = RAISED,
                          bg='dark slate blue',fg='white',activebackground='darkslateblue',
                          activeforeground='lavender',bd=0,cursor='hand2', autostyle=False)


    MenuBttn5.place(x=900,y=56)

    #MYCART

    MenuBttn6=Button(window, text = "  MY CART  ", font=('Times New roman',12),relief = RAISED,
                          bg='LAVENDER',fg='DARKSLATEBLUE',activeforeground='darkslateblue',
                          activebackground='lavender',bd=0,cursor='hand2', command=finalbill, autostyle=False)
    MenuBttn6.place(x=1160,y=56)
menubar()
#----------------------------------------------------------------------------------------------------------------------
#big frame
big_frame=Frame(window, width=1000, height=560, bg="#e3e3ef", autostyle=False)
big_frame.pack(pady=150)

#progress bar2
s1 = ttk.Style()
s1.theme_use('clam')
s1.configure("blue.Horizontal.TProgressbar", troughcolor ='#be96d6', background='#671399', bd=0)

progress1 = ttk.Progressbar(big_frame, orient="horizontal", style="blue.Horizontal.TProgressbar", length=600, mode="determinate")
#progress1.pack()


#frame_s
frame_s=Frame(big_frame, width=1000, height=50, bg="#e3e3ef", autostyle=False)
#frame_c.pack_forget()
#product_frame_current.pack_forget()
#label1
label_s1=Label(frame_s, text=("Choose colour for your Shampoo"), font=('Georgia', 24), bg="#e3e3ef", autostyle=False)
label_s1.config(anchor=CENTER)
label_s1.place(x=15, y=13)
shampoo_colours()

#frame_c
frame_c=Frame(big_frame, width=1000, height=50, bg="#e3e3ef", autostyle=False)
#label1
label_c1=Label(frame_c, text=("Choose colour for your Conditioner"), font=('Georgia', 24), bg="#e3e3ef", autostyle=False)
label_c1.config(anchor=CENTER)
label_c1.place(x=15, y=13)
conditioner_colours()

#frame_se
frame_se=Frame(big_frame, width=1000, height=50, bg="#e3e3ef", autostyle=False)
label_se1=Label(frame_se, text=("Select your Hair Serum: "), font=('Georgia', 24), bg="#e3e3ef", autostyle=False)
#label_se1.config(anchor=CENTER)
label_se1.place(x=0, y=13)
serum_colours()

#frame_m
frame_m=Frame(big_frame, width=1000, height=50, bg="#e3e3ef", autostyle=False)
#label1
label_m1=Label(frame_m, text=("Choose colour for your Hair Mask"), font=('Georgia', 24), bg="#e3e3ef", autostyle=False)
label_m1.config(anchor=CENTER)
label_m1.place(x=15, y=13)
mask_colours()

#frame_p
frame_px=Frame(big_frame, width=1000, height=50, bg="#e3e3ef", autostyle=False)
#label1
label_p1=Label(frame_px, text=("Select your Styling Primer: "), font=('Georgia', 24), bg="#e3e3ef",autostyle=False)
#label_p1.config(anchor=CENTER)
label_p1.place(x=0, y=13)
primer_colours()

product_frame_list=[]
#product_frame_current=product_frame_list[0]

clicked_buttons = set()
def button_clicked(button_num):
    clicked_buttons.add(button_num)
def show_result_button():
    if len(clicked_buttons) == 0:
        messagebox.showinfo("Message", "Please select atleast one option")
    else:
         show_ingredients()


def next_button_clicked():
    if current_frame==frame4:
        update_selected_count()
        if  selected_count>=1:
            nextFrame()
    elif current_frame==frame10:
        update_selected_count1()
    elif len(clicked_buttons) == 0:
        messagebox.showinfo("Message", "Please select atleast one option")
    else:
        nextFrame()

index1=0
def nextFrame():                            #functionality for next button in the quiz frames
    global current_frame, index1, bgImage
    index1+=1
    current_frame.pack_forget()     #hide the current frame
    current_frame=frame_list[(frame_list.index(current_frame)+1)% len(frame_list)]#move to next frame
    progress["value"] = (index1 + 1) * 100 / len(frame_list)
    clicked_buttons.clear()
    if current_frame==frame1:
        bg=Image.open("bg8.png")
        resize_bgImage=bg.resize((width, 700))
        bgImage= ImageTk.PhotoImage(resize_bgImage)
        bgLabel.config(image=bgImage)
        #back.place_forget()
    elif current_frame==frame6:
        next1.place_forget()
        show_result.place(x=805, y=540)
    else:
        bg=Image.open("bg8.png")
        resize_bgImage=bg.resize((width, 700))
        bgImage= ImageTk.PhotoImage(resize_bgImage)
        bgLabel.config(image=bgImage)
        #back.place(x=230, y=549)
    current_frame.pack()

#display the new frame
'''
def backFrame():                    #functionality for back button in the quiz frames
    global current_frame, index1, bgImage
    index1-=1
    current_frame.pack_forget()
    current_frame=frame_list[(frame_list.index(current_frame)-1) % len(frame_list)]
    if current_frame==frame1:
        bg=Image.open("bg8.png")
        resize_bgImage=bg.resize((width, 700))
        bgImage= ImageTk.PhotoImage(resize_bgImage)
        bgLabel.config(image=bgImage)
        back.place_forget()
    elif current_frame==frame6:
        next1.place_forget()
        show_result.place(x=860, y=550)
    else:
        bg=Image.open("bg.png")
        resize_bgImage=bg.resize((width, 700))
        bgImage= ImageTk.PhotoImage(resize_bgImage)
        bgLabel.config(image=bgImage)
        back.place(x=230, y=549)
        next1.place(x=860, y=550)
        show_result.place_forget()
        
   
    current_frame.pack()
    progress["value"] = (index1 - 1) * 100 / len(frame_list)
'''
#-------------------------------------------------------------------------------    
#progress bar
s = ttk.Style()
s.theme_use('clam')
s.configure("blue.Horizontal.TProgressbar", troughcolor ='#be96d6', background='#671399', bd=0)

progress = ttk.Progressbar(big_frame, orient="horizontal", style="blue.Horizontal.TProgressbar", length=600, mode="determinate")
progress.pack()

#-------------------------------------------------------------------------------
#styling
style = ttk.Style()
style.configure("TButton", padding=10, relief="flat", background="#d7d4f4", foreground="black", font=('Kristen ITC', 18), bd=0, width=15, autostyle=False)

#frame1
frame1=Frame(big_frame, width=1000, height=50, bg="#e3e3ef", autostyle=False)
#label1
label1=Label(frame1, text="What is your natural hair type?", font=('Georgia', 24), bg="#e3e3ef", autostyle=False)
label1.config(anchor=CENTER)
label1.grid(row=0, column=0, padx=100, pady=15)

#button1
button1=ttk.Button(frame1, text="Straight", cursor='hand2',command=lambda: button_clicked(1))
button1.grid(row=6, column=0, sticky="w", padx=50, pady=15)

#button2
button2=ttk.Button(frame1, text="Wavy", cursor='hand2',command=lambda: button_clicked(2))
button2.grid(row=6, column=0, sticky="e", padx=50, pady=15)

#button3
button3=ttk.Button(frame1, text="Curly",command=lambda: button_clicked(2))
button3.grid(row=7, column=0, sticky="w", padx=50, pady=15)

#button4
button4=ttk.Button(frame1, text="Coily",command=lambda: button_clicked(4))
button4.grid(row=7, column=0, sticky="e", padx=50, pady=15)

#------------------------------------------------------------------------------------------------------------------------
#styling
style.configure("TButton", padding=10, relief="flat", background="#d7d4f4", foreground="black", font=('Kristen ITC', 18), bd=0, width=15, autostyle=False)

#frame2
frame2=Frame(big_frame, width=1000, height=600, bg="#e3e3ef", autostyle=False)

#label1
label1=Label(frame2, text=" What is troubling you about your hair?", font=('Georgia', 24), bg="#e3e3ef", autostyle=False)
label1.config(anchor=CENTER)
label1.grid(row=4, column=0, padx=100, pady=15)

#button1
button1=ttk.Button(frame2, text="Scalp issues", command=lambda: button_clicked(1))
button1.grid(row=6, column=0, sticky="w", padx=60, pady=15)

#button2
button2=ttk.Button(frame2, text="Fizz",command=lambda: button_clicked(2))
button2.grid(row=6, column=0, sticky="e", padx=60, pady=15)

#button3
button3=ttk.Button(frame2, text="Dryness",command=lambda: button_clicked(3))
button3.grid(row=7, column=0, sticky="w", padx=60, pady=15)

#button4
button4=ttk.Button(frame2, text="Lack of volume",command=lambda: button_clicked(4))
button4.grid(row=7, column=0, sticky="e", padx=60, pady=15)

#frame3
frame3=Frame(big_frame, width=1000, height=600, bg="#e3e3ef", autostyle=False)
#styling
style.configure("TButton", padding=10, relief="flat", background="#d7d4f4", foreground="black", font=('Kristen ITC', 15), bd=0, width=19)

#label1
label1=Label(frame3, text="How often do you wash your hair?", font=('Georgia', 24), bg="#e3e3ef", autostyle=False)
label1.config(anchor=CENTER)
label1.grid(row=4, column=0, padx=100, pady=15)

#button1
button1=ttk.Button(frame3, text="Daily", command=lambda: button_clicked(1))
button1.grid(row=6, column=0, sticky="w", padx=10, pady=15)

#button2
button2=ttk.Button(frame3, text="Every other day", command=lambda: button_clicked(2))
button2.grid(row=6, column=0, sticky="e", padx=10, pady=15)

#button3
button3=ttk.Button(frame3, text="Once or twice a week", command=lambda: button_clicked(3))
button3.grid(row=7, column=0, sticky="w", padx=10, pady=15)

#button4
button4=ttk.Button(frame3, text="Less than once a week", command=lambda: button_clicked(4))
button4.grid(row=7, column=0, sticky="e", padx=10, pady=15)

#frame4
frame4=Frame(big_frame, width=1000, height=600, bg="#e3e3ef", autostyle=False)

#label1
label1=Label(frame4, text="Select your #hairgoals   (any 5)", font=('Georgia', 24), bg="#e3e3ef", autostyle=False)
label1.config(anchor=CENTER)
label1.pack()

#checkbuttons
frame0=Frame(frame4, bg="#e3e3ef", autostyle=False)
frame0.pack(side="left", padx=9)
check_vars = []
checkboxes=[]
options=["Anti Frizz", "Deep Condition", "Fix split ends", "Hydrate", "Shine","Volumize","Strengthen", "Colour Protection", "Soothe scalp","Straighten"]
options1 = ["Anti Frizz", "Deep Condition", "Fix split ends", "Hydrate", "Shine",]
options2=["Volumize","Strengthen", "Colour Protection", "Soothe scalp","Straighten"]
for index, option in enumerate(options1):
    var = IntVar()
    check_vars.append(var)
    check = Checkbutton(
        frame0,
        text=option,
        variable=var,
        font=("Kristen ITC", 15),
        fg="darkblue",  # Text color
        selectcolor="lightgreen",  # Background color when selected
        activebackground="lightblue",  # Background color when hovering
        padx=10,  # Horizontal padding
        pady=5,   # Vertical padding
        relief="flat",  # No button border
        anchor="w",  # Text alignment (west)
        command=lambda option=options.index(option): check_checkbox(option)   #functio to keep track of no of check boxes selected
    )
    check.pack(fill="x", pady=4, padx=9)
    checkboxes.append(check)
    
frame9=Frame(frame4, bg="#e3e3ef")
frame9.pack(side="left", padx=9)

for option in options2:
    var = IntVar()
    check_vars.append(var)
    check = Checkbutton(
        frame9,
        text=option,
        variable=var,
        font=("Kristen ITC", 15),
        fg="darkblue",  # Text color
        selectcolor="lightgreen",  # Background color when selected
        activebackground="lightblue",  # Background color when hovering
        padx=10,  # Horizontal padding
        pady=5,   # Vertical padding
        relief="flat",  # No button border
        anchor="w",  # Text alignment (west)
        command=lambda option=options.index(option): check_checkbox(option)
    )
    check.pack(fill="x", pady=4, padx=9)
    checkboxes.append(check)

#frame5
frame5=Frame(big_frame, width=1000, height=600, bg="#e3e3ef", autostyle=False)

#label1
label1=Label(frame5, text="Which colour best describes your hair?", font=('Georgia', 24), bg="#e3e3ef", autostyle=False)
label1.config(anchor=CENTER)
label1.grid(row=4, column=0, padx=100, pady=15)

#button1
button1=ttk.Button(frame5, text="Black", command=lambda: button_clicked(1))
button1.grid(row=6, column=0, sticky="w", padx=60, pady=15)

#button2
button2=ttk.Button(frame5, text="Blonde", command=lambda: button_clicked(2))
button2.grid(row=6, column=0, sticky="e", padx=60, pady=15)

#button3
button3=ttk.Button(frame5, text="Brunette", command=lambda: button_clicked(3))
button3.grid(row=7, column=0, sticky="w", padx=60, pady=15)

#button4
button4=ttk.Button(frame5, text="Red", command=lambda: button_clicked(4))
button4.grid(row=7, column=0, sticky="e", padx=60, pady=15)

#button5
button5=ttk.Button(frame5, text="Gray or Silver", command=lambda: button_clicked(5))
button5.grid(row=8, column=0, sticky="w", padx=60, pady=15)

#button6
button6=ttk.Button(frame5, text="Fashion colour(eg: pink)", command=lambda: button_clicked(6))
button6.grid(row=8, column=0, sticky="e", padx=60, pady=15)

#frame10
frame10=Frame(big_frame, width=800, height=300, bg="#e3e3ef", autostyle=False)

label1=Label(frame10, text="Select your desired hair products:", font=('Georgia', 24), bg="#e3e3ef", autostyle=False)
label1.config(anchor=CENTER)
label1.pack()


frame_p=Frame(frame10, bg="#e3e3ef", autostyle=False)
frame_p.pack(side="left", padx=9)
check_vars9 = []
checkboxes9=[]
options_p=["Shampoo", "Conditioner", "Hair Serum", "Hair Mask", "Styling Primer"]
for index9, option9 in enumerate(options_p):
    var9 = IntVar()
    check_vars9.append(var9)
    check9 = Checkbutton(
        frame_p,
        text=option9,
        variable=var9,
        font=("Kristen ITC", 15),
        fg="darkblue",  # Text color
        selectcolor="lightgreen",  # Background color when selected
        activebackground="lightblue",  # Background color when hovering
        padx=10,  # Horizontal padding
        pady=5,   # Vertical padding
        relief="flat",  # No button border
        anchor="w",  # Text alignment (west)
        command=lambda option9=options_p.index(option9): check_checkbox1(option9)   #functio to keep track of no of check boxes selected
    )
    check9.pack(fill="x", pady=4, padx=9)
    checkboxes9.append(check9)
    


#frame6
frame6=Frame(big_frame, width=800, height=300, bg="#e3e3ef", autostyle=False)

#label1
label1=Label(frame6, text=" Choose your formula colour....", font=('Georgia', 24), bg="#e3e3ef", autostyle=False)
label1.config(anchor=CENTER)
label1.place(x=200, y=10)
radio_var = StringVar()
#button1
image1=Image.open("blue_s.png")
resize_image1=image1.resize((100, 200))
blue= ImageTk.PhotoImage(resize_image1)

radio_button1 =ttk.Radiobutton(frame6, variable=radio_var, value="blue", image=blue, command=lambda: button_clicked(1))
radio_button1.place(x=10, y=80)

#button2
image2=Image.open("pink_s.png")
resize_image2=image2.resize((100, 200))
pink= ImageTk.PhotoImage(resize_image2)

radio_button2 = ttk.Radiobutton(frame6, variable=radio_var, value="pink", image=pink, compound=LEFT, command=lambda: button_clicked(2))
radio_button2.place(x=180, y=80)

#button3
image3=Image.open("green_s.png")
resize_image3=image3.resize((100, 200))
green= ImageTk.PhotoImage(resize_image3)

radio_button3= ttk.Radiobutton(frame6, variable=radio_var, value="green", image=green, compound=LEFT, command=lambda: button_clicked(3))
radio_button3.place(x=350, y=80)

#button4
image4=Image.open("orange_s.png")
resize_image4=image4.resize((100, 200))
orange= ImageTk.PhotoImage(resize_image4)

radio_button4= ttk.Radiobutton(frame6, variable=radio_var, value="orange", image=orange, compound=LEFT, command=lambda: button_clicked(4))
radio_button4.place(x=520, y=80)

#button5
image5=Image.open("white_s.png")
resize_image5=image5.resize((100, 200))
white= ImageTk.PhotoImage(resize_image5)

radio_button5= ttk.Radiobutton(frame6, variable=radio_var, value="white", image=white, compound=LEFT, command=lambda: button_clicked(5))
radio_button5.place(x=690, y=80)

#show results
show_result=Button(window, text="SHOW RESULTS", cursor='hand2', bg="black", bd=0, width=13
             ,  activebackground='black', activeforeground='black',fg="white", font=('Georgia', 23), command=show_result_button, autostyle=False)
show_result.place(x=805, y=540)

#--------------------------------------------------------------------------------
#frame_list
frame_list=[frame1, frame2, frame3, frame4, frame5,frame10]
#frame_list=[frame4, frame10]
current_frame=frame_list[0]
current_frame.pack()

#back
#back=Button(window, text="BACK", font=('Georgia', 25), width=15, cursor='hand2', bg="black", fg='white', bd=0
#             ,  activebackground='black', activeforeground='black', command=backFrame)
#back.place(x=230, y=549)

#next
next1=Button(window, text="NEXT", font=('Georgia', 25), width=13, cursor='hand2', bg="black", fg='white', bd=0
             ,  activebackground='black', activeforeground='black', command=next_button_clicked, autostyle=False)
next1.place(x=800, y=540)
one.mainloop()
