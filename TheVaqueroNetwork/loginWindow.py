import tkinter as tk
from tkinter import messagebox as VaquerosMessager

from createAccount import create_account_window
from database import validate_user, add_user
from dashboardWindow import DashboardWindow

# Global variables for entry widgets. These are used to access the input fields
username_entry = None
password_entry = None


def on_login_attempt(login_window):
    """
    This function is called when the "Login" button is clicked.
    It retrieves user credentials, validates them against the database,
    and handles success (opening dashboard) or failure (showing error/offering account creation).

    Args:
        login_window: The Tkinter window object of the login screen,
                      which will be managed upon successful login.
    """
    global username_entry, password_entry

    username = username_entry.get()  # Retrieve text from the username input field
    password = password_entry.get()  # Retrieve text from the password input field

    # Basic validation: Check if either input field is empty
    if not username or not password:
        VaquerosMessager.showwarning("Login Failed", "Username and Password cannot be empty.")
        print("Login failed: Empty fields.")
        return  # Stop function execution if fields are empty

    # Call the validate_user function from database.py to check credentials
    if validate_user(username, password):
        VaquerosMessager.showinfo("Login Successful", "Welcome to The Vaquero Network!")
        print(f"Login successful for user: {username}")
        login_window.withdraw()  # Hide the current login window

        # Create an instance of the DashboardWindow class, passing the login window as master
        dash = DashboardWindow(master=login_window, username=username)
        dash.focus_set()  # Set focus to the newly opened dashboard window

        # Define a function to handle the dashboard window being closed by the user
        def on_dash_close():
            dash.destroy()  # Destroy the dashboard window
            login_window.deiconify()  # Reveal the login window again

        # Set the protocol for the dashboard window's close button (e.g., 'X' button)
        dash.protocol("WM_DELETE_WINDOW", on_dash_close)
    else:
        # If login fails, offer to create an account
        if VaquerosMessager.askyesno("User Not Found", "User not found. Would you like to create an account?"):
            # Attempt to add the new user to the database
            if add_user(username, password):
                VaquerosMessager.showinfo("Account Created", "Account created successfully! You can now log in.")
                username_entry.delete(0, tk.END)  # Clear username field after successful registration
                password_entry.delete(0, tk.END)  # Clear password field after successful registration
            else:
                VaquerosMessager.showerror("Error", "Could not create account. Username might already exist.")
        else:
            VaquerosMessager.showerror("Login Failed", "Invalid Username or Password.")  # Show error for invalid credentials
            print(f"Login failed: Invalid credentials for {username}.")


def create_main_window():
    """
    Creates and displays the initial Tkinter window for the login screen.
    This is the first window users will see.
    """

    window = tk.Tk()  # Creates the root Tkinter window instance
    window.title("The Vaquero Network - Login")  # Sets the title of the login window
    window.geometry("400x350")  # Sets the initial size of the window

    # Welcome message label for the login screen
    welcome_label = tk.Label(
        window,
        text="Welcome to The Vaquero Network!",
        font=("Arial", 16, "bold"),  # Sets font and makes it bold
        fg="#333333"  # Sets text color to dark gray
    )
    welcome_label.pack(pady=30)

    # --- Username Input Field ---
    username_label = tk.Label(window, text="Username:", font=("Arial", 10))
    username_label.pack(pady=(10, 0))

    global username_entry
    username_entry = tk.Entry(window, width=40, bd=2, relief="groove")  # Creates the input field for username
    username_entry.pack(pady=(0, 10))

    # --- Password Input Field ---
    password_label = tk.Label(window, text="Password:", font=("Arial", 10))
    password_label.pack(pady=(10, 0))

    global password_entry
    password_entry = tk.Entry(window, width=40, show="*", bd=2, relief="groove")  # Creates password input, hides characters
    password_entry.pack(pady=(0, 20))

    # --- Login Button ---
    login_button = tk.Button(
        window,
        text="Login",
        # Uses a lambda function to pass the 'window' object to on_login_attempt when clicked
        command=lambda: on_login_attempt(window),
        bg="#4CAF50",  # Sets background color (green)
        fg="white",  # Sets foreground color (text color)
        font=("Arial", 12, "bold"),
        width=15,
        height=1,
        relief="raised",  # Gives the button a raised 3D effect
        bd=3  # Sets the border thickness
    )
    login_button.pack(pady=10)  # Packs the login button

    # --- Create Account Button ---
    create_account_button = tk.Button(
        window,
        text="Create Account",
        command=lambda: create_account_window(),  # Opens the account creation window when clicked
        bg="#2196F3",  # Sets background color (blue)
        fg="white",  # Sets foreground color (text color)
        font=("Arial", 12, "bold"),
        width=15,
        height=1,
        relief="raised",  # Gives the button a raised 3D effect
        bd=3  # Sets the border thickness
    )
    create_account_button.pack(pady=10)  # Packs the create account button

    return window  # Returns the main window object for further management in SLAMain.py
