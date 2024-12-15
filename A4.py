from tkinter import *


root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')


lbl1 = Label(text = "Full Name", bg="#3895D3", fg='white')
lbl2 = Label(text = "Email Id", bg="#3895D3", fg='white')
lbl3 = Label(text = "Enter Password", bg="#3895D3", fg='white')


name_entry = Entry()
email_entry = Entry()
pass_entry = Entry(show="*")


def display():
	name = name_entry.get()
	greet = "Hey "+name
	message =  "\nCongratulations for your new account!"
	textbox.insert(END, greet)
	textbox.insert(END, message)


textbox = Text(bg="#BEBEBE", fg="black")


btn = Button(text = "Create Account", command=display)


lbl1.pack()
name_entry.pack()
lbl2.pack()
email_entry.pack()
lbl3.pack()
pass_entry.pack()
btn.pack()
textbox.pack()