from loginWindow import create_main_window
from database import init_db

def main():
    """
    The main function to run the application.
    It initializes the database and starts the Tkinter event loop.
    """
    # Initializes the SQLite database to ensure it exists before the application tries to interact with it.
    init_db()
    
    # Creates the initial login window. The window object is returned.
    main_window = create_main_window()
    
    # Starts the Tkinter event loop. This line must be at the end.
    main_window.mainloop()

if __name__ == "__main__":
    main()
