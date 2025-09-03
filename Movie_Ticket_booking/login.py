from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from main import ticket_book

def admin_login():

    window = Tk()
    window.title("Login form")
    window.geometry('800x550')
    window.configure(bg='#333333')

    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "admin123"

    # Variables for the login fields
    username = StringVar()
    password = StringVar()

    bg_image = Image.open("C:\\Users\\CHINTAN\\OneDrive\\Desktop\\Movie_Ticket_booking\\ticket.jpg")
    bg_image = bg_image.resize((800, 550), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = Canvas(window, width=800, height=550)
    canvas.pack(fill="both", expand=True)
    bg_image_id = canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    def on_resize(event):
        new_width = event.width
        new_height = event.height
        resized_bg_image = bg_image.resize((new_width, new_height), Image.LANCZOS)
        new_bg_photo = ImageTk.PhotoImage(resized_bg_image)
        canvas.itemconfig(bg_image_id, image=new_bg_photo)
        canvas.image = new_bg_photo  
        canvas.config(width=new_width, height=new_height)

    canvas.bind("<Configure>", on_resize)

    def login():
        if username_entry.get() == ADMIN_USERNAME and password_entry.get() == ADMIN_PASSWORD:
            messagebox.showinfo(title="Login Success", message="You successfully logged in.")
            window.destroy()
            ticket_book()
        else:
            messagebox.showerror(title="Error", message="Invalid login.")

    frame = Frame(window, bg='#333333')

    login_label = Label(frame, text="Login", bg='#333333', fg="lightblue", font=("Arial", 30))
    username_label =Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    username_entry =Entry(frame, font=("Arial", 16))
    password_label =Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    password_entry =Entry(frame, show="*", font=("Arial", 16))
    login_button = Button(frame, text="Login", bg="lightblue", fg="#FFFFFF", font=("Arial", 16), command=login)

    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)

    frame.place(relx=0.4, rely=0.5, anchor='center') 

    window.mainloop()


if __name__ == "__main__":
    admin_login()