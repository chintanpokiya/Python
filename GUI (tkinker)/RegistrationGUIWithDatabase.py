import tkinter as tk
from tkinter import messagebox
import mysql.connector

#function to check login credentials
def login():
    username = entry_username_login.get()
    password = entry_password_login.get()

    try:
        connection=mysql.connector.connect(
            host='localhost',
            database='test',
            user='root', #replace with your MYSQL username
            password=''  #replace with your MYSQL password
        )
        #Step 3
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users1 WHERE username=%s and password=%s",(username,password))
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

def register():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email =  entry_email.get()
    username = entry_user_name.get()
    password = entry_password.get()
    birthdate = entry_birthdate.get()
    gender = gender_var.get()
    phone = entry_phone.get()

    
    try:
        connection=mysql.connector.connect(
            host='localhost',
            database='test',
            user='root', #replace with your MYSQL username
            password=''  #replace with your MYSQL password
        )
        #Step 3
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users1 (first_name, last_name, email, username, password, birthdate, gender, phone) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(first_name, last_name, email, username, password, birthdate, gender, phone))
        connection.commit()
                
        messagebox.showinfo("Registration","Registration Successfully..!!")
        
    except mysql.connector.Error as err:
        messagebox.showerror("Error",f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def show_registration():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="First Name :").place(x=50, y=20)
    global entry_first_name
    entry_first_name = tk.Entry(root)
    entry_first_name.place(x=150, y=20)

    tk.Label(root, text="Last Name :").place(x=50, y=60)
    global entry_last_name
    entry_last_name = tk.Entry(root)
    entry_last_name.place(x=150, y=60)

    tk.Label(root, text="Email :").place(x=50, y=100)
    global entry_email
    entry_email = tk.Entry(root)
    entry_email.place(x=150, y=100)

    tk.Label(root, text="User Name :").place(x=50, y=140)
    global entry_user_name
    entry_user_name = tk.Entry(root)
    entry_user_name.place(x=150, y=140)

    tk.Label(root, text="Password :").place(x=50, y=180)
    global entry_password
    entry_password = tk.Entry(root, show='*')
    entry_password.place(x=150, y=180)

    tk.Label(root, text="BirthDate (YYYY-MM-DD) :").place(x=50, y=220)
    global entry_birthdate
    entry_birthdate = tk.Entry(root)
    entry_birthdate.place(x=200, y=220)

    tk.Label(root, text="Gender :").place(x=50, y=260)
    global gender_var
    gender_var = tk.StringVar(value='Male')
    tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").place(x=150, y=260)
    tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").place(x=200, y=260)
    tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").place(x=270, y=260)

    tk.Label(root, text="Phone :").place(x=50, y=300)
    global entry_phone
    entry_phone = tk.Entry(root)
    entry_phone.place(x=150, y=300)

    tk.Button(root, text='Register', command=register).place(x=60, y=340)    
    tk.Button(root, text='Back to Login', command=show_login).place(x=120, y=340)
        
def show_login():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Username :").place(x=50, y=40)
    global entry_username_login
    entry_username_login = tk.Entry(root)
    entry_username_login.place(x=120, y=40)

    tk.Label(root, text="Password :").place(x=50, y=80)
    global entry_password_login
    entry_password_login = tk.Entry(root, show='*')
    entry_password_login.place(x=120, y=80)

    tk.Button(root,text="Login",command=login).place(x=60, y=120)
    tk.Button(root,text="Register",command=show_registration).place(x=120, y=120)


#create and place labels and entries
root=tk.Tk()
root.title("User Registration and Login Page")
root.geometry("400x450")

show_login()

#run the application
root.mainloop()
