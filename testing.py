from tkinter import *
import mysql.connector
from PIL import ImageTk, Image

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="faizkhan777",
    database="login"
)

mycursor = mydb.cursor()

root = Tk()
root.title("Login Page")
root.iconbitmap('ry.ico')
root.geometry('350x500')


img = ImageTk.PhotoImage(Image.open("background.jpg"))
label = Label(image=img)
label.pack()


lab = Label(root, text="WELCOME TO THE LOGIN PAGE").pack(pady=40)

def register():
    root.destroy()
    import testing2

def login():
    root.destroy()
    import testing4


register_button = Button(root, text="Register", command=register).place(x=150, y=200)
login_button = Button(root, text="Login", width=6, command=login).place(x=150, y=250)





root.mainloop()




