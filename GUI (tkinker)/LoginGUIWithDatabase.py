import tkinter as tk
from tkinter import messagebox
import mysql.connector

#function to check login credentials
def login():
    username = entry_username.get()
    password = entry_password.get()

    try:
        connection=mysql.connector.connect(
            host='localhost',
            database='test',
            user='root', #replace with your MYSQL username
            password=''  #replace with your MYSQL password
        )
        #Step 3
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE uname=%s and password=%s",(username,password))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Login","Login Successfully..!!")
        else:
            messagebox.showerror("Login","Invalid username or password..!!")

    except mysql.connector.Error as err:
        messagebox.showerror("Error",f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
        
        

#create and place labels and entries
root=tk.Tk()
root.title("Login Page")

label_username = tk.Label(root,text="Username :- ")
label_username.pack(pady=5)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root,text="Password :- ")
label_password.pack(pady=5)

entry_password = tk.Entry(root)
entry_password.pack(pady=5)

#Create and place the login button
login_button = tk.Button(root,text="Login",command=login)
login_button.pack(pady=20)

#run the application
root.mainloop()
