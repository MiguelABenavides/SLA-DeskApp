import tkinter as tk

from database import add_user

def create_account_window():
    """
    Creates and displays the account creation window of the application.
    """
    account_window = tk.Toplevel()
    account_window.title("Create Account")
    account_window.geometry("400x400")

    # Account creation form
    tk.Label(account_window, text="Create a New Account", font=("Arial", 16)).pack(pady=10)

    tk.Label(account_window, text="Username:", font=("Arial", 12)).pack(pady=5)
    username_entry = tk.Entry(account_window, width=30)
    username_entry.pack(pady=5)

    tk.Label(account_window, text="Password:", font=("Arial", 12)).pack(pady=5)
    password_entry = tk.Entry(account_window, show="*", width=30)
    password_entry.pack(pady=5)

    tk.Button(account_window, text="Create Account", command=lambda: create_account(username_entry.get(), password_entry.get()),
            bg="#6202C2", # Sets background color (purple)
            fg="white", # Sets foreground color (text color)
            font=("Arial", 12, "bold"),
            width=15,
            height=1,
            relief="raised", # Gives the button a raised 3D effect
            bd=3 # Sets the border thickness
            ).pack(pady=20)

def create_account(username, password):
    """
    Handles the account creation logic.
    """
    if not username or not password:
        tk.messagebox.showwarning("Input Error", "Please enter both username and password.")
        return
    
    if add_user(username, password):
        tk.messagebox.showinfo("Success", "Account created successfully!")

    else:
        tk.messagebox.showerror("Error", "Failed to create account. Username might already exist.")