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


lab1 = Label(root, text="Enter your Username and Password").place(x=85, y=150)

lab2 = Label(root, text="Username: ").place(x=40, y=200)
lab3 = Label(root, text="Password: ").place(x=40, y=250)

e1 = Entry(root)
e1.place(x=115, y=200, width=200)
e2 = Entry(root)
e2.place(x=115, y=250, width=200)

def click():
    check = "SELECT * FROM login_details WHERE username = '" + e1.get() + "' and password = '" + e2.get() + "'"
    mycursor.execute(check)
    result = mycursor.fetchall()
    for x in result:
        x
        if e1.get() and e2.get() in x:
            root.destroy()
            import testing3
            # else:
            #     lab3 = Label(root, text="Wrong password").pack()
        elif e1.get() and e2.get() not in x:
            lab4 = Label(root, text="Username doesn't exist").grid()

login_button = Button(root, text="Login", command=click).place(x=270, y=290)



root.mainloop()