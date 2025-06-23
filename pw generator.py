import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            result_label.config(text="Length should be at least 4")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_display.delete(0, tk.END)
        password_display.insert(0, password)
    except ValueError:
        result_label.config(text="Please enter a valid number")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.config(bg="#f0f0f0")

tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

tk.Label(root, text="Enter password length:", font=("Arial", 12), bg="#f0f0f0").pack()
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)

tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password, bg="#4CAF50", fg="white").pack(pady=10)

password_display = tk.Entry(root, font=("Arial", 14), justify="center", width=30)
password_display.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 10), fg="red", bg="#f0f0f0")
result_label.pack()

root.mainloop()
