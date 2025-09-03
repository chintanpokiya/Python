import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

connection = None

def setup_database():
    global connection
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='items_db'
            )
        cursor=connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS items(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name varchar(255) NOT NULL UNIQUE
            )

        ''')
        connection.commit()

    except Error as e:
        print(f"(Error : {e})")
    finally:
        if connection:
            cursor.close()


def insert_item(item_name):
    global connection
    try:
        cursor=connection.cursor()
        cursor.execute("INSERT INTO items (name) values(%s)",(item_name,))
        connection.commit()
    except mysql.connector.IntegrityError as e:
        messagebox.showerror("Error : ",str(e))
    finally:
        cursor.close()

def fetch_items():
    global connection
    items = []
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * from items")
        items=cursor.fetchall()
    except Error as e:
        messagebox,showerror("Error",str(e))
    finally:
        cursor.close()
    return items

def delete_items(item_id):
    global connection
    try:
        cursor=connection.cursor()
        cursor.execute("DELETE FROME items WHERE id LIKE %s",(item_id,))
        connection.commit()
    except Error as e:
        messagebox.showerror("Error",str(e))
        
    finally:
        cursor.close()

class ItemApp:
    def __init__(self,root):
        
        self.root=root
        self.root.title("Item List")

        self.label=tk.Label(root,text="Enter Item Name : ")
        self.label.pack()

        self.entry=tk.Entry(root)
        self.entry.pack()

        self.add_button=tk.Button(root,text="Add Item",command=self.add_item)
        self.add_button.pack()

        self.display_button=tk.Button(root,text="Display Item",command=self.display_items)
        self.display_button.pack()
            
        self.delete_button=tk.Button(root,text="delete Item",command=self.delete_items)
        self.delete_button.pack()

        self.text=tk.Text(root,height=10,width=30)
        self.text.pack()

    def add_item(self):
        item_name = self.entry.get()
        if item_name:
            insert_item(item_name)
            messagebox.showinfo("Success","Item Added !!")
            self.entry.delete(0,tk.END)
            self.display_items()
        else:
            messagebox.showerror("Warning","Please Enter an item name")

    def display_items(self):
        self.text.delete(1.0,tk.END)
        items=fetch_items()
        for item in items:
            self.text.insert(tk.END,f"{item[0]}:{item[1]}\n")

    def delete_items(self):
        try:
            select_text=self.text.get("sel.first","sel.last")
            item_id=int(select_text.split(":")[0])
            delete_items(item_id)
            messagebox.showinfo("Success","item deleted !!")
            self.display_items()
        except ValueError:
            messagebox.showerror("Warning","Please Select item to delete")
            
        

if __name__ == "__main__":
    setup_database()
    root=tk.Tk()
    app=ItemApp(root)
    root.mainloop()
                
        
