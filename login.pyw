import hashlib
import pymongo
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# The mongoDB Stuff
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["myDataBase"]
mycol = mydb["users"]

# hashing stuff
h = hashlib.new("sha512")

# Ui Stuff
root = Tk()
root.title("Login")

# Email or Phone
ttk.Label(root, width = 50, text = "Email Or Phone :").pack(padx = 5, pady = 5)
phone_or_email_entry = ttk.Entry(root, width = 50)
phone_or_email_entry.pack(padx = 10, pady = 10)

# password
ttk.Label(root, width = 50, text = "Password :").pack(padx = 5, pady = 5)
password = ttk.Entry(root, show = "*", width = 50)
password.pack(padx = 10, pady = 10)

# button
button = ttk.Button(root, width = 30, text = "Login")
button.pack(padx = 10, pady = 10)


def login() :
    global phone_or_email_entry, password
    # Getting The Values Of The Entries
    password_get = str(password.get()).encode("utf-8")
    phone_or_email = str(phone_or_email_entry.get())
    # Hashing The Password
    h.update(password_get)
    password_get = h.hexdigest()
    # Comparing Data To Login
    data = {"name" : phone_or_email, "password" : password_get}
    mydoc = mycol.find_one(data)
    try :
        if mydoc['phone_or_email'] == phone_or_email and mydoc['password'] == password_get :
            messagebox.showinfo(message="You Are Able To Log In")
    except :
        messagebox.showinfo(message="You Are Not Able To Log In")
    # Clearing The Entries
    phone_or_email_entry.delete(0, END)
    password.delete(0, END)
    exit()


button.config(command = login)
root.mainloop()