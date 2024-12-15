from tkinter import *
from PIL import Image, ImageTk


window = Tk()
window.title('image')
window.geometry('400x400')


limage = Image.open("img.png")


image_l = ImageTk.PhotoImage(limage)


label = Label(window, image=image_l, height=200, width=300)
button = Button(text = "Click Here", bg="#BC544B")
textbox = Text()
textbox.insert(END, "This is how you do it!")

label.pack()
button.pack()
textbox.pack()