import tkinter as tk
from loginWindow import create_main_window
from database import init_db


def main():
    """
    The main function to run the application.
    It initializes the database and starts the Tkinter event loop.
    """
    # Initialize the SQLite database (creates file and tables if they don't exist)
    init_db()

    # Create the initial login window
    main_window = create_main_window()

    # Start the Tkinter event loop to display the window and handle interactions
    main_window.mainloop()


if __name__ == "__main__":
    main()