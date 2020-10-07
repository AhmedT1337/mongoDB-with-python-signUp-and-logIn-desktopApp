import hashlib
import pymongo
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# The mongoDB Stuff
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["myDataBase"]
mycol = mydb["users"]

# Hashing Stuff
h = hashlib.new("sha512")

# Ui Stuff
root = Tk()
root.title("Sign Up")

# user name
ttk.Label(root, width = 50, text = "User Name :").pack(padx = 5, pady = 5)
user_name = ttk.Entry(root, width = 50)
user_name.pack(padx = 10, pady = 10)

# phone or Email
ttk.Label(root, width = 50, text = "Phone or Email :").pack(padx = 5, pady = 5)
phone_or_email = ttk.Entry(root, width = 50)
phone_or_email.pack(padx = 10, pady = 10)

# password
ttk.Label(root, width = 50, text = "Password :").pack(padx = 5, pady = 5)
password = ttk.Entry(root, show = "*", width = 50)
password.pack(padx = 10, pady = 10)

# buttons
button = ttk.Button(root, width = 30, text = "Sign up")
button.pack(padx = 10, pady = 10)
# button to show the logins
show = ttk.Button(root, width = 30, text = "Show The DataBase")
show.pack(padx = 10, pady = 10)


# The real work begins here
def login():
    # Password Hashing For Security
    global password, user_name, phone_or_email
    # hashing The Password
    password_get_encoded = str(password.get()).encode("utf-8")
    h.update(password_get_encoded)
    password_get = h.hexdigest()
    # The rest Of entries getting
    user_name_get = str(user_name.get())
    phone_or_email_get = str(phone_or_email.get())

    # Data Handling and Inserting
    data = {"name" : user_name_get, "phone_or_email" : phone_or_email_get, "password" : password_get}
    mycol.insert_one(data)
    messagebox.showinfo(message = "Inserted")
    w = open("data.txt", "a")
    for i in mycol.find() :
        w.write(str(i))
    user_name.delete(0, END)
    phone_or_email.delete(0, END)
    password.delete(0, END)


button.config(command = login)

root.mainloop()