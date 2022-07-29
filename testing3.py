from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Login Page")
root.iconbitmap('ry.ico')
root.geometry('350x500')

img = ImageTk.PhotoImage(Image.open("background.jpg"))
label = Label(image=img)
label.pack()


lab = Label(root, text="LOGIN SUCCESSFUL").place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()