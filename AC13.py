from tkinter import *
import random
import time

Top = Tk()
Top.title('Restaurant Management System')
Top.geometry("700x400")

localtime=time.asctime(time.localtime(time.time()))

lblinfo = Label(Top, font=( 'aria' ,15, 'bold' ),text="Codingal Delicacies Billing System",fg="#003166",bd=10)

lblinfo.place(x=150, y=0)

lbl_info = Label(Top, font=( 'aria' ,10, ),text=localtime,fg="#003166")

lbl_info.place(x=250, y=40)

lbl_order = Label(Top, text="Order Number")
val_order = Entry(Top)
def insert():
	val_order.delete(0,END)
	val_order.insert(END, str(random.randint(0, 1000)))
btn_order = Button(text="New Order", bg="#8cd3ff", width=6, command=insert)
btn_order.place(x=100, y=65)
lbl_order.place(x=200, y=70)
val_order.place(x=310, y=70)


f1 = Frame(Top,width = 350,height=200,relief=SUNKEN)
f1.place(x=0, y=200)

f2 = Frame(Top ,width = 350,height=200,relief=SUNKEN)
f2.pack(side=RIGHT)