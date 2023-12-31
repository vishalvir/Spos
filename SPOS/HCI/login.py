import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Replace with your authentication logic
    if username == "your_username" and password == "your_password":
        messagebox.showinfo("Login Successful", "Welcome to Instagram!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")


root = tk.Tk()
root.title("Login")
root.geometry("400x400")


root.configure(bg="#f0f2f5")


frame = tk.Frame(root, bg="#ffffff")
frame.place(relx=0.5, rely=0.5, anchor="center")


logo_label = tk.Label(frame, text="Instagram", font=("Helvetica", 30, "bold"), bg="#ffffff", fg="#405DE6")
logo_label.pack(pady=10)

username_label = tk.Label(frame, text="Username", font=("Helvetica", 14), bg="#ffffff")
username_label.pack(pady=(0, 5))
username_entry = tk.Entry(frame, font=("Helvetica", 12))
username_entry.pack(pady=(0, 10))


password_label = tk.Label(frame, text="Password", font=("Helvetica", 14), bg="#ffffff")
password_label.pack()
password_entry = tk.Entry(frame, show="*", font=("Helvetica", 12))
password_entry.pack(pady=(0, 10))


login_button = tk.Button(frame, text="Login", command=login, font=("Helvetica", 14), bg="#405DE6", fg="white", relief="solid")
login_button.pack()


forgot_password_label = tk.Label(frame, text="Forgot password?", font=("Helvetica", 12, "underline"), bg="#ffffff", cursor="hand2")
forgot_password_label.pack(pady=10)


new_account_label = tk.Label(frame, text="Create new account", font=("Helvetica", 12, "underline"), bg="#ffffff", cursor="hand2")
new_account_label.pack()


forgot_password_label.bind("<Button-1>", lambda e: messagebox.showinfo("Forgot Password", "Redirect to password recovery page"))
new_account_label.bind("<Button-1>", lambda e: messagebox.showinfo("Create New Account", "Redirect to registration page"))

root.mainloop()
