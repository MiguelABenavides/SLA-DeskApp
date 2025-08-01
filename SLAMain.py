
# import function that creates the main window from our logic file.
from SLALogic import create_main_window

def main():

    # call the function from logic to get the main window.
    main_window = create_main_window()

    # start the Tkinter event loop ; this makes the window appear and
    # listens for user interactions.
    main_window.mainloop()

if __name__ == "__main__":
    main()
