import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task can't be empty!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# GUI window
root = tk.Tk()
root.title("To-Do List")

# Entry and Buttons
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", width=20, command=add_task)
add_btn.pack(pady=5)

del_btn = tk.Button(root, text="Delete Task", width=20, command=delete_task)
del_btn.pack(pady=5)

# Listbox to show tasks
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

root.mainloop()
