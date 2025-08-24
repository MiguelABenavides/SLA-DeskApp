import tkinter as tk
from tkinter import ttk  # NEW: Import ttk for themed widgets
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
    window.geometry("400x380")  # Slightly increased height for better spacing
    window.resizable(False, False)  # Prevent resizing for a fixed, clean look

    # NEW: Configure ttk styles
    style = ttk.Style()
    style.theme_use('clam')

    # Configure global fonts and colors for ttk widgets
    style.configure('.', font=('Inter', 10))
    style.configure('TLabel', font=('Inter', 12), foreground='#333333', background='white')
    style.configure('TEntry', font=('Inter', 12), fieldbackground='#f0f0f0', foreground='#333333', borderwidth=1, relief='flat')

    # Configure default TButton style (for Login button - UTRGV Orange)
    style.configure('TButton',
                    font=('Inter', 12, 'bold'),
                    foreground='white',
                    background='#F26722',  # UTRGV Orange
                    padding=10,
                    relief='flat',
                    borderwidth=0
                    )
    style.map('TButton',
              background=[('active', '#d95d1e')],  # Darken on hover
              foreground=[('active', 'white')]
              )

    # Specific style for the Create Account button (UTRGV Blue)
    style.configure('Blue.TButton', background='#0056b3')  # UTRGV Blue
    style.map('Blue.TButton',
              background=[('active', '#003d80')],  # Darken on hover
              foreground=[('active', 'white')]
              )


    # Welcome message label (still using tk.Label as it's not a themed widget type that needs ttk.Style)
    tk.Label(
        window,
        text="Welcome to The Vaquero Network!",
        font=("Inter", 18, "bold"),
        fg="#0056b3",  # UTRGV Blue for heading
        bg="white"
    ).pack(pady=(30, 20))

    # --- Username Input Field ---
    ttk.Label(window, text="Username:").pack(pady=(5, 0))
    global username_entry
    username_entry = ttk.Entry(window, width=40)
    username_entry.pack(pady=(0, 10))

    # --- Password Input Field ---
    ttk.Label(window, text="Password:").pack(pady=(5, 0))
    global password_entry
    password_entry = ttk.Entry(window, width=40, show="*")
    password_entry.pack(pady=(0, 20))

    # --- Login Button ---
    ttk.Button(
        window,
        text="Login",
        command=lambda: on_login_attempt(window),
        style='TButton'
    ).pack(pady=5)

    # --- Create Account Button ---
    ttk.Button(
        window,
        text="Create Account",
        command=lambda: create_account_window(),
        style='Blue.TButton'
    ).pack(pady=5)

    # Set window background explicitly for consistency
    window.configure(bg='white')

    return window