from tkinter import *
import tkinter
from tkinter import ttk
import final_backend_done
from PIL import ImageTk, Image     #pillow module

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e7.delete(0,END)
    e7.insert(END,selected_tuple[1])
    e8.delete(0,END)
    e8.insert(END,selected_tuple[2])
    e9.delete(0,END)
    e9.insert(END,selected_tuple[3])

def get_selected_row_1(event):
    global selected_tuple_1
    index_1=list2.curselection()[0]
    selected_tuple_1=list2.get(index_1)
    e1.delete(0,END)
    e1.insert(END,selected_tuple_1[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple_1[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple_1[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple_1[4])
    e5.delete(0,END)
    e5.insert(END,selected_tuple_1[5])
    e6.delete(0,END)
    e6.insert(END,selected_tuple_1[6])

def selected_1():
    id_no=list3.get(0)
    s_name=studentname_text.get()
    r_no=rollno_text.get()
    e_mail=email_text.get()
    add_no=addmissionno_text.get()
    branch=branch_text.get()
    ph_no=phonenumber_text.get()
    b_code=bookcode_text.get()
    b_name=bookname_text.get()
    a_name=author_text.get()
    s_date=t_date_text.get()
    s_month=t_month_text.get()
    s_year=t_year_text.get()
    final_backend_done.save_details(id_no,s_name,r_no,e_mail,add_no,branch,ph_no,b_code,b_name,a_name,s_date,s_month,s_year)
    info_box()

def view_command_3():
    list3.delete(0,END)
    for row in final_backend_done.view_3():
        list3.insert(END,row)

def send_email():
    final_backend_done.send_mail(t_date_text.get(),t_month_text.get(),t_year_text.get())
    view_command_3()
    info_box()


def view_command():
    list1.delete(0,END)
    for rows in final_backend_done.view():
        list1.insert(END,rows)

def search_command():
    list1.delete(0,END)
    for rows in final_backend_done.search(bookcode_text.get(),bookname_text.get(),author_text.get()):
          list1.insert(END,rows)

def insert_command():
    final_backend_done.insert(bookcode_text.get(),bookname_text.get(),author_text.get())
    list1.delete(0,END)
    list1.insert(END,(bookcode_text.get(),bookname_text.get(),author_text.get()))
    view_command()
    info_box()

def enter_command():
    final_backend_done.save_date(t_date_text.get(),t_month_text.get(),t_year_text.get())
    info_box()

def delete_command():
    final_backend_done.delete(selected_tuple[0])
    view_command()
    info_box()

def update_command():
    final_backend_done.update(selected_tuple[0],bookcode_text.get(),bookname_text.get(),author_text.get())
    info_box()

def find_command():
    list2.delete(0,END)
    for row in final_backend_done.find(studentname_text.get(),rollno_text.get(),email_text.get(),addmissionno_text.get(),branch_text.get(),phonenumber_text.get()):
          list2.insert(END,row)
 

def add_command():
    final_backend_done.add(studentname_text.get(),rollno_text.get(),email_text.get(),addmissionno_text.get(),branch_text.get(),phonenumber_text.get())
    list2.delete(0,END)
    list2.insert(END,(studentname_text.get(),rollno_text.get(),email_text.get(),addmissionno_text.get(),branch_text.get(),phonenumber_text.get()))
    info_box()

def view_command_1():
    list2.delete(0,END)
    for row in final_backend_done.view_1():
        list2.insert(END,row)

def view_details_command():
    list3.delete(0,END)
    for row in final_backend_done.view_3():
        list3.insert(END,row)
    info_box()

def erase_command():
    final_backend_done.erase(selected_tuple_1[0])
    view_command_1()
    info_box()

def update_s_command():
    final_backend_done.update_s(selected_tuple_1[0],studentname_text.get(),rollno_text.get(),email_text.get(),addmissionno_text.get(),branch_text.get(),phonenumber_text.get())
    info_box()

def scan_command():
    global addmission_number
    addmission_number=final_backend_done.scan()
    list2.delete(0,END)
    for row in final_backend_done.find(studentname_text.get(),rollno_text.get(),email_text.get(),addmission_number,branch_text.get(),phonenumber_text.get()):
          list2.insert(END,row)

window=Tk()  #Tk() is a class and window is the object

window.wm_title("Library Reminder ver_0.5")
window.iconbitmap('icon.ico')
window.geometry("1600x720")
font=('Arial Bold',8)

img=Image.open("logo.png")
img=img.resize((660,100))

my= ImageTk.PhotoImage(img)
label=Label(window,image=my)
label.place(x=10,y=0)


img_1=Image.open("owl.png")
img_1=img_1.resize((250,180))

my_1= ImageTk.PhotoImage(img_1)
label_1=Label(window,image=my_1)
label_1.place(x=450,y=510)

img_3=Image.open("library_image.png")
img_3=img_3.resize((450,100))

my_3= ImageTk.PhotoImage(img_3)
label_3=Label(window,image=my_3)
label_3.place(x=720,y=0)

img_2=Image.open("pic.png")
img_2=img_2.resize((250,180))

my_2= ImageTk.PhotoImage(img_2)
label_2=Label(window,image=my_2)
label_2.place(x=740,y=510)

Dataframe=Frame(window,bd=15,relief=RIDGE,bg="orange")
Dataframe.place(x=0,y=100,width=735,height=120)

Dataframe_1=Frame(window,bd=10,relief=RIDGE)
Dataframe_1.place(x=740,y=110,width=385,height=80)


l1=Label(window,text="Student Name",font=font)
l1.place(x=40,y=120)

l2=Label(window,text="Roll Number",font=font)
l2.place(x=280,y=120)

l3=Label(window,text="Email",font=font)
l3.place(x=490,y=120)

l4=Label(window,text="Addmission Number",font=font)
l4.place(x=25,y=150)

l5=Label(window,text="Branch",font=font)
l5.place(x=290,y=150)

l6=Label(window,text="Phone number",font=font)
l6.place(x=490,y=150)

l7=Label(window,text="Book code",font=font)
l7.place(x=40,y=180)


l8=Label(window,text="Book name",font=font)
l8.place(x=280,y=180)

l9=Label(window,text="Author",font=font)
l9.place(x=490,y=180)

l10=Label(window,text="BOOKS DETAILS",font=font)
l10.place(x=30,y=275)

l11=Label(window,text="STUDENTS DETAILS",font=font)
l11.place(x=30,y=490)

l12=Label(window,text="Date of Issue of the Book ",font=font)
l12.place(x=30,y=235)


l13=Label(window,text="DD",font=font)
l13.place(x=180,y=255)
t_date_text=StringVar()
t_date=ttk.Combobox(window,textvariable=t_date_text,state="readonly",font=("arial",10),width=2)
t_date["values"]=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
t_date.current(0)
t_date.place(x=180,y=235)


l14=Label(window,text="MM",font=font)
l14.place(x=230,y=255)
t_month_text=StringVar()
t_month=ttk.Combobox(window,textvariable=t_month_text,state="readonly",font=("arial",10),width=2)
t_month["values"]=(1,2,3,4,5,6,7,8,9,10,11,12)
t_month.current(0)
t_month.place(x=230,y=235)

l15=Label(window,text="YYYY",font=font)
l15.place(x=280,y=255)
t_year_text=StringVar()
t_year=ttk.Combobox(window,textvariable=t_year_text,state="readonly",font=("arial",10),width=5)
t_year["values"]=(2021,2022,2023,2024,2025,2026,2027,2028,2029,2030)
t_year.current(0)
t_year.place(x=280,y=235)

l16=Label(window,text="Information box",font=font)
l16.place(x=750,y=120)
Info=Text(window,height=2,width=45)
Info.place(x=750,y=140)

l17=Label(window,text="Current Issued Books Details",font=font)
l17.place(x=750,y=230)

def info_box():
    message=final_backend_done.Info_func()
    Info.delete(1.0,END)
    Info.insert(tkinter.END,message)


'''l12=Label(window,text="Developers  :  Gundaram Raju Rohith  ,  Satya Susheela  ,  Arshia Parveen ,  Arunanjan Bandari ,  Jayesh Dhoot")
l12.place(x=0,y=640)

l13=Label(window,text="Department  of  Computer Science  ;  Section :  2")
l13.place(x=0,y=660)

'''

studentname_text=StringVar()
e1=Entry(window,textvariable=studentname_text)
e1.place(x=150,y=120)

rollno_text=StringVar()
e2=Entry(window,textvariable=rollno_text)
e2.place(x=360,y=120)

email_text=StringVar()
e3=Entry(window,textvariable=email_text)
e3.place(x=590,y=120)

addmissionno_text=StringVar()
e4=Entry(window,textvariable=addmissionno_text)
e4.place(x=150,y=150)

branch_text=StringVar()
e5=Entry(window,textvariable=branch_text)
e5.place(x=360,y=150)

phonenumber_text=StringVar()
e6=Entry(window,textvariable=phonenumber_text)
e6.place(x=590,y=150)


bookcode_text=StringVar()
e7=Entry(window,textvariable=bookcode_text)
e7.place(x=150,y=180)

bookname_text=StringVar()
e8=Entry(window,textvariable=bookname_text)
e8.place(x=360,y=180)

author_text=StringVar()
e9=Entry(window,textvariable=author_text)
e9.place(x=590,y=180)


list1=Listbox(window,height=11,width=65)
list1.place(x=20,y=300)

sb1=Scrollbar(window)
sb1.place(x=420,y=350)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>',get_selected_row)

list2=Listbox(window,height=11,width=65)
list2.place(x=20,y=510)
sb2=Scrollbar(window)
sb2.place(x=420,y=590)
list2.configure(yscrollcommand=sb2.set)
sb2.configure(command=list2.yview)
list2.bind('<<ListboxSelect>>',get_selected_row_1)

list3=Listbox(window,height=11,width=125)
list3.place(x=740,y=250)
sb3=Scrollbar(window)
sb3.place(x=1270,y=330)
list3.configure(yscrollcommand=sb3.set)
sb3.configure(command=list3.yview)

Buttonframe=Frame(window,bd=15,relief=RIDGE)
Buttonframe.place(x=445,y=225,width=265,height=290)



b2=Button(window,text="View all Books", width=15,command=view_command,font=font)
b2.place(x=460,y=280)

b3=Button(window,text="Search  Book", width=15,command=search_command,font=font)
b3.place(x=460,y=320)

b4=Button(window,text="Add Book", width=15,command=insert_command,font=font)
b4.place(x=460,y=360)

b5=Button(window,text="Update  Book", width=15,command=update_command,font=font)
b5.place(x=460,y=400)

b6=Button(window,text="Delete  Book", width=15,command=delete_command,font=font)
b6.place(x=460,y=440)
 
b11=Button(window,text="All students",width=15,command=view_command_1,font=font)
b11.place(x=580,y=280)

b9=Button(window,text="Find Student",width=15,command=find_command,font=font)
b9.place(x=580,y=320)

b10=Button(window,text="Add Student",width=15,command=add_command,font=font)
b10.place(x=580,y=360)

b8=Button(window,text="Save  Details",width=15,font=font,command=selected_1)
b8.place(x=460,y=480)

b10=Button(window,text="Send Emails",width=15,command=send_email,font=font)
b10.place(x=580,y=480)

b9=Button(window,text="Delete Student",width=15,command=erase_command,font=font)
b9.place(x=580,y=440)


b10=Button(window,text="Update Student",width=15,command=update_s_command,font=font)
b10.place(x=580,y=400)

b11=Button(window,text="Scan",width=32,font=font,command=scan_command)
b11.place(x=460,y=240)

b12=Button(window,text="Enter",width=5,font=font,command=enter_command)
b12.place(x=340,y=234)

b13=Button(window,text="View",width=15,font=font,command=view_details_command)
b13.place(x=920,y=220)

tkinter.mainloop()
window.mainloop()
