import tkinter as tk

#create the main window
root = tk.Tk()
root.title("My First GUI Application")
root.geometry("300x200")

#create a label
label = tk.Label(root,text="Hello, World!")
label.pack(pady=10)    

#define button click function
def on_button_click():
    label.config(text="Button Clicked!!")

#create a button
button = tk.Button(root,text="Click Me",command=on_button_click)
button.pack(pady=10)

#run the application
root.mainloop()
