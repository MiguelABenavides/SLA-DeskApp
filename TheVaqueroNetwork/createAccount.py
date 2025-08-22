import tkinter as tk
from tkinter import messagebox  # Using standard messagebox import for this file

from database import add_user  # Imports the function to add a new user to the database


def create_account_window():
    """
    Creates and displays the account creation window of the application.
    This window allows users to input a new username and password to register.
    """
    account_window = tk.Toplevel()  # Creates a new top-level window for account creation
    account_window.title("Create Account")  # Sets the title of the window
    account_window.geometry("400x400")  # Sets the initial size of the window

    # Add a main title label for the account creation form
    tk.Label(account_window, text="Create a New Account", font=("Arial", 16)).pack(pady=10)

    # --- Username Input Field ---
    tk.Label(account_window, text="Username:", font=("Arial", 12)).pack(pady=5)
    username_entry = tk.Entry(account_window, width=30)  # Creates an input field for the username
    username_entry.pack(pady=5)

    # --- Password Input Field ---
    tk.Label(account_window, text="Password:", font=("Arial", 12)).pack(pady=5)
    password_entry = tk.Entry(account_window, show="*", width=30)  # Creates a password input field, hiding characters
    password_entry.pack(pady=5)

    # --- Create Account Button ---
    tk.Button(account_window, text="Create Account",
              # Calls the create_account function with the entered username and password
              command=lambda: create_account(username_entry.get(), password_entry.get()),
              bg="#6202C2",  # Sets background color (purple)
              fg="white",  # Sets foreground color (text color)
              font=("Arial", 12, "bold"),
              width=15,
              height=1,
              relief="raised",  # Gives the button a raised 3D effect
              bd=3  # Sets the border thickness
              ).pack(pady=20)  # Packs the button with vertical padding


def create_account(username, password):
    """
    Handles the account creation logic.
    Validates input and attempts to add the new user to the database.

    Args:
        username (str): The username to be created.
        password (str): The password for the new user.
    """
    # Check if both username and password fields are not empty
    if not username or not password:
        messagebox.showwarning("Input Error", "Please enter both username and password.")
        return  # Stop if input is incomplete

    # Attempt to add the new user to the database
    if add_user(username, password):
        messagebox.showinfo("Success", "Account created successfully!")  # Show success message
    else:
        # Show error if account creation fails (e.g., username already exists)
        messagebox.showerror("Error", "Failed to create account. Username might already exist.")
