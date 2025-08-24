import tkinter as tk
from tkinter import ttk  # NEW: Import ttk for themed widgets
from tkinter import messagebox as VaquerosMessager  # Using VaquerosMessager for consistency

from database import add_user  # Imports the function to add a new user to the database

def create_account_window():
    """
    Creates and displays the account creation window of the application.
    This window allows users to input a new username and password to register.
    """
    account_window = tk.Toplevel()  # Creates a new top-level window for account creation
    account_window.title("Create Account")  # Sets the title of the window
    account_window.geometry("400x400")  # Sets the initial size of the window
    account_window.resizable(False, False)  # Prevent resizing for a fixed, clean look

    style = ttk.Style(account_window)  # Pass the Toplevel window to the style
    style.theme_use('clam')

    # Configure global fonts and colors for ttk widgets within this window
    style.configure('.', font=('Inter', 10))
    style.configure('TLabel', font=('Inter', 12), foreground='#333333', background='white')
    style.configure('TEntry', font=('Inter', 12), fieldbackground='#f0f0f0', foreground='#333333', borderwidth=1, relief='flat')

    # Configure button style for Create Account button
    style.configure('Purple.TButton',
                    font=('Inter', 12, 'bold'),
                    foreground='white',
                    background='#6202C2',  # Purple background
                    padding=10,
                    relief='flat',
                    borderwidth=0
                    )
    style.map('Purple.TButton',
              background=[('active', '#4a0196')],  # Darken on hover
              foreground=[('active', 'white')]
              )

    # Add a main title label for the account creation form
    tk.Label(
        account_window,
        text="Create a New Account",
        font=("Inter", 18, "bold"),
        fg="#1a344a",  # Darker navy for heading
        bg="white"
    ).pack(pady=(30, 20))

    # --- Username Input Field ---
    ttk.Label(account_window, text="Username:").pack(pady=(5, 0))
    username_entry = ttk.Entry(account_window, width=30)
    username_entry.pack(pady=(0, 10))

    # --- Password Input Field ---
    ttk.Label(account_window, text="Password:").pack(pady=(5, 0))
    password_entry = ttk.Entry(account_window, show="*", width=30)
    password_entry.pack(pady=(0, 20))

    # --- Create Account Button ---
    ttk.Button(
        account_window,
        text="Create Account",
        command=lambda: create_account(username_entry.get(), password_entry.get(), account_window),
        # Pass window to close
        style='Purple.TButton'
    ).pack(pady=10)

    account_window.configure(bg='white')

def create_account(username, password, account_window_to_destroy):
    """
    Handles the account creation logic.
    Validates input and attempts to add the new user to the database.

    Args:
        username (str): The username to be created.
        password (str): The password for the new user.
        account_window_to_destroy: The Tkinter window object to destroy on success.
    """

    # Check if both username and password fields are not empty
    if not username or not password:
        VaquerosMessager.showwarning("Input Error", "Please enter both username and password.")
        return  # Stop if input is incomplete

    # Attempt to add the new user to the database
    if add_user(username, password):
        VaquerosMessager.showinfo("Success",
                                  "Account created successfully! You can now log in.")
        account_window_to_destroy.destroy()  # Close the account creation window on success
    else:
        # Show error if account creation fails (e.g., username already exists)
        VaquerosMessager.showerror("Error", "Failed to create account. Username might already exist.")
