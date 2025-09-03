from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("Ticket.db") 

def ticket_book():
    root = Tk()
    root.title("Document Management System")
    root.geometry("1200x800")  # Adjusted size for better viewing
    root.config(bg="black")
    
    name = StringVar()
    email = StringVar()
    contact = StringVar()
    movie_name = StringVar()
    movie_prize = StringVar()
    movie_type = StringVar()

    entries_frame = Frame(root, bg="lightblue")
    entries_frame.pack(side=TOP, fill=X, padx=20, pady=10)  # Added padding around the frame
    title = Label(entries_frame, text="Document Management System", font=("Calibri", 18, "bold"), bg="lightblue", fg="black")
    title.grid(row=0, columnspan=4, padx=10, pady=10, sticky="w")

    # Entry labels and fields with reduced padding
    lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="lightblue", fg="black")
    lblName.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=25)
    txtName.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    lblemail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="lightblue", fg="black")
    lblemail.grid(row=1, column=2, padx=5, pady=5, sticky="w")
    txtemail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=25)
    txtemail.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    lblContact = Label(entries_frame, text="Contact", font=("Calibri", 16), bg="lightblue", fg="black")
    lblContact.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=25)
    txtContact.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    lblmovie_name = Label(entries_frame, text="Movie Name", font=("Calibri", 16), bg="lightblue", fg="black")
    lblmovie_name.grid(row=2, column=2, padx=5, pady=5, sticky="w")
    txtmovie_name = Entry(entries_frame, textvariable=movie_name, font=("Calibri", 16), width=25)
    txtmovie_name.grid(row=2, column=3, padx=5, pady=5, sticky="w")

    lblmovie_prize = Label(entries_frame, text="Movie Prize", font=("Calibri", 16), bg="lightblue", fg="black")
    lblmovie_prize.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    txtmovie_prize = Entry(entries_frame, textvariable=movie_prize, font=("Calibri", 16), width=25)
    txtmovie_prize.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    lblmovie_type = Label(entries_frame, text="Moive Type", font=("Calibri", 16), bg="lightblue", fg="black")
    lblmovie_type.grid(row=3, column=2, padx=5, pady=5, sticky="w")
    txtmovie_type = Entry(entries_frame, textvariable=movie_type, font=("Calibri", 16), width=25)
    txtmovie_type.grid(row=3, column=3, padx=5, pady=5, sticky="w")

    # Functions for handling data
    def getData(event):
        selected_row = tv.focus()
        data = tv.item(selected_row)
        global row
        row = data["values"]
        name.set(row[1])
        email.set(row[2])
        contact.set(row[3])
        movie_name.set(row[4])
        movie_prize.set(row[5])
        movie_type.set(row[6])

    def displayAll():
        tv.delete(*tv.get_children())
        for row in db.fetch():
            tv.insert("", END, values=row)

    def add_document():
        if txtName.get() == "" or txtemail.get() == "" or txtContact.get() == "" or txtmovie_name.get() == "" or txtmovie_prize.get() == "" or txtmovie_type.get() == "":
            messagebox.showerror("Error", "Please fill in all details")
            return
        db.insert(txtName.get(), txtemail.get(), txtContact.get(), txtmovie_name.get(), txtmovie_prize.get(), txtmovie_type.get())
        messagebox.showinfo("Success", "Record added successfully")
        clearAll()
        displayAll()

    def update_document():
        if txtName.get() == "" or txtemail.get() == "" or txtContact.get() == "" or txtmovie_name.get() == "" or txtmovie_prize.get() == "" or txtmovie_type.get() == "":
            messagebox.showerror("Error", "Please fill in all details")
            return
        db.update(row[0], txtName.get(), txtemail.get(), txtContact.get(), txtmovie_name.get(), txtmovie_prize.get(), txtmovie_type.get())
        messagebox.showinfo("Success", "Record updated successfully")
        clearAll()
        displayAll()

    def delete_document():
        db.remove(row[0])
        messagebox.showinfo("Success", "Record deleted successfully")
        clearAll()
        displayAll()

    def clearAll():
        name.set("")
        email.set("")
        contact.set("")
        movie_name.set("")
        movie_prize.set("")
        movie_type.set("")

    # Buttons frame
    btn_frame = Frame(entries_frame, bg="lightblue")
    btn_frame.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="w")

    btnAdd = Button(btn_frame, command=add_document, text="Add", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#16a085", bd=0)
    btnAdd.grid(row=0, column=0)

    btnUpdate = Button(btn_frame, command=update_document, text="Update", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#2980b9", bd=0)
    btnUpdate.grid(row=0, column=1, padx=10)

    btnDelete = Button(btn_frame, command=delete_document, text="Delete", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#c0392b", bd=0)
    btnDelete.grid(row=0, column=2, padx=10)

    btnClear = Button(btn_frame, command=clearAll, text="Clear", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#f39c12", bd=0)
    btnClear.grid(row=0, column=3, padx=10)

    # Table View
    tree_frame = Frame(root, bg="lightblue")
    tree_frame.place(x=0, y=400, width=1200, height=380)  # Adjusted height

    # Scrollbars
    vsb = Scrollbar(tree_frame, orient="vertical")
    vsb.pack(side='right', fill='y')

    hsb = Scrollbar(tree_frame, orient="horizontal")
    hsb.pack(side='bottom', fill='x')

    style = ttk.Style()
    style.configure("mystyle.Treeview", font=("Calibri", 14), rowheight=35)
    style.configure("mystyle.Treeview.Heading", font=("Calibri", 15, "bold"))

    tv = ttk.Treeview(tree_frame, columns=("1", "2", "3", "4", "5", "6", "7"), style="mystyle.Treeview", yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    vsb.config(command=tv.yview)
    hsb.config(command=tv.xview)

    # Configuring headings and column widths
    tv.heading("1", text="ID")
    tv.column("1", width=50)
    tv.heading("2", text="Name")
    tv.column("2", width=150)
    tv.heading("3", text="Email")
    tv.column("3", width=200)
    tv.heading("4", text="Contact")
    tv.column("4", width=150)
    tv.heading("5", text="Movie Name")
    tv.column("5", width=150)
    tv.heading("6", text="Movie prize")
    tv.column("6", width=100)
    tv.heading("7", text="Movie Type")
    tv.column("7", width=100)
    tv['show'] = 'headings'
    
    tv.bind("<ButtonRelease-1>", getData)
    tv.pack(fill=BOTH, expand=True)

    displayAll()
    root.mainloop()

# Call the function to start the application
ticket_book()
