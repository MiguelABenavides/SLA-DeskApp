import tkinter as tk
from tkinter import messagebox as VaquerosMessager

from createAccount import create_account_window # Imports the account creation window function
# Imports the database functions from your database.py file
from database import validate_user, add_user
from dashboardWindow import DashboardWindow

# Global variables for entry widgets. These need to be accessible across functions
# like on_login_attempt, so they are declared global here and assigned in create_main_window.
username_entry = None
password_entry = None

def on_login_attempt(login_window):
    """
    This function is called when the "Login" button is clicked.
    It retrieves the username and password from the entry fields,
    performs validation against the database, and handles the outcome.

    Args:
        login_window: The Tkinter window object of the login screen,
                      which will be destroyed on successful login.
    """
    global username_entry, password_entry # Declares intent to use the global entry widgets

    username = username_entry.get() # Retrieves the text from the username entry field
    password = password_entry.get() # Retrieves the text from the password entry field

    # Basic validation: Checks if either input field is empty
    if not username or not password:
        VaquerosMessager.showwarning("Login Failed", "Username and Password cannot be empty.")
        print("Login failed: Empty fields.")
        return # Stops the function execution if fields are empty

    # Calls the validate_user function from database.py
    if validate_user(username, password):
        VaquerosMessager.showinfo("Login Successful", "Welcome to The Vaquero Network!")
        print(f"Login successful for user: {username}")
        # Hide the root instead of destroying it, so we can open a Toplevel dashboard
        login_window.withdraw()
        dash = DashboardWindow(master=login_window)
        dash.focus_set()
        def on_dash_close():
            dash.destroy()
            login_window.deiconify()
        dash.protocol("WM_DELETE_WINDOW", on_dash_close)
    else:
        VaquerosMessager.showerror("Login Failed", "Invalid Username or Password.")
        print(f"Login failed: Invalid credentials for {username}.")


def create_main_window():
    """
    Creates and displays the initial Tkinter window for the login screen.
    """
    window = tk.Tk() # Creates the root Tkinter window
    window.title("The Vaquero Network - Login") # Sets the title of the login window
    window.geometry("400x350") # Sets the initial size of the window

    # Welcome message label
    welcome_label = tk.Label(
        window,
        text="Welcome to The Vaquero Network!",
        font=("Arial", 16, "bold"), # Sets font and makes it bold
        fg="#333333" # Sets text color to dark gray
    )
    welcome_label.pack(pady=30) # Packs the label with vertical padding

    # --- Username Input Field ---
    username_label = tk.Label(window, text="Username:", font=("Arial", 10))
    username_label.pack(pady=(10, 0)) # Packs label with padding (top, bottom)

    global username_entry # Declares username_entry as a global variable
    username_entry = tk.Entry(window, width=40, bd=2, relief="groove") # Creates the input field for username
    username_entry.pack(pady=(0, 10)) # Packs entry with padding

    # --- Password Input Field ---
    password_label = tk.Label(window, text="Password:", font=("Arial", 10))
    password_label.pack(pady=(10, 0))

    global password_entry # Declares password_entry as a global variable
    password_entry = tk.Entry(window, width=40, show="*", bd=2, relief="groove") # Creates password input, shows '*' for chars
    password_entry.pack(pady=(0, 20)) # Packs entry with padding

    # --- Login Button ---
    login_button = tk.Button(
        window,
        text="Login",
        # Uses a lambda function to pass the 'window' object to on_login_attempt when clicked
        command=lambda: on_login_attempt(window),
        bg="#4CAF50", # Sets background color (green)
        fg="white", # Sets foreground color (text color)
        font=("Arial", 12, "bold"),
        width=15,
        height=1,
        relief="raised", # Gives the button a raised 3D effect
        bd=3 # Sets the border thickness
    )
    login_button.pack(pady=10)

    # --- Create Account Button ---
    create_account_button = tk.Button(
        window,
        text="Create Account",
        command=lambda: create_account_window(), # Opens the account creation window
        bg="#2196F3", # Sets background color (blue)
        fg="white", # Sets foreground color (text color)
        font=("Arial", 12, "bold"),
        width=15,
        height=1,
        relief="raised", # Gives the button a raised 3D effect
        bd=3 # Sets the border thickness
    )
    create_account_button.pack(pady=10)

    return window # Returns the main window object
