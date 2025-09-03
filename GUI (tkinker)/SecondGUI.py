import tkinter as tk

#create the main window
root = tk.Tk()
root.title("My Second GUI Application")
root.geometry("300x200")

#create entry widgets for two numbers
entry1 = tk.Entry(root,width=10,font=('Arial',18))
entry1.pack(pady=10)

entry2 = tk.Entry(root,width=10,font=('Arial',18))
entry2.pack(pady=10)


#Function to add numbers
def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result :- {result}")
    except ValueError :
        result_label.config(text="Error : Invalid input")

#create a button to perform addition
add_button = tk.Button(root,text="Add",command=add_numbers,font=('Arial',18))
add_button.pack(pady=20)

#create a label to display the result
result_label = tk.Label(root,text="Result :- ",font=('Arial',18))
result_label.pack(pady=10)

#Run the application
root.mainloop()
