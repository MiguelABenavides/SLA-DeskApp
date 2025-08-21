import tkinter as tk

# Default text to show when the dashboard opens
WELCOME_TEXT = (
    "Welcome to The Vaquero Network!\n\n"
    "This is your dashboard home.\n\n"
    "Use the navigation on the left to explore Activities, Calendar, Bulletin Board, and Emergency Contacts."
)

current_dashboard_content = None

def clear_dashboard_content(parent_frame):
    """
    Clears all widgets from the current content frame in the dashboard.
    """
    for widget in parent_frame.winfo_children():
        widget.destroy()

def show_welcome_text(parent_frame, text: str | None = None):
    """
    Displays a welcome/custom text area in the dashboard content area.
    """
    clear_dashboard_content(parent_frame)
    message = text if text is not None else WELCOME_TEXT
    tk.Label(parent_frame, text="Dashboard", font=("Arial", 16, "bold"), fg="#333333").pack(pady=(20, 10))
    tk.Message(parent_frame, text=message, font=("Arial", 12), width=700, justify="left").pack(padx=20, pady=(0, 20))


def show_activities_manager(parent_frame):
    """
    Displays the Activities/Task Schedule Manager UI in the dashboard content area.
    """
    clear_dashboard_content(parent_frame) # Clear previous content

    # Add specific UI elements for the Activities Manager here
    tk.Label(parent_frame, text="Activities/Task Schedule Manager", font=("Arial", 16, "bold"), fg="#333333").pack(pady=20)
    tk.Label(parent_frame, text="Here you can add, view, edit, and delete your tasks.", font=("Arial", 12)).pack(pady=10)

    # Placeholder buttons for CRUD operations (we'll implement these next)
    add_task_button = tk.Button(parent_frame, text="Add New Task", font=("Arial", 12, "bold"), bg="#5cb85c", fg="white", width=15)
    add_task_button.pack(pady=5)
    view_tasks_button = tk.Button(parent_frame, text="View All Tasks", font=("Arial", 12, "bold"), bg="#0275d8", fg="white", width=15)
    view_tasks_button.pack(pady=5)

def show_event_calendar(parent_frame):
    """
    Displays the Event Calendar UI in the dashboard content area.
    """
    clear_dashboard_content(parent_frame)
    tk.Label(parent_frame, text="Event Calendar", font=("Arial", 16, "bold"), fg="#333333").pack(pady=20)
    tk.Label(parent_frame, text="View and manage upcoming events.", font=("Arial", 12)).pack(pady=10)

def show_bulletin_board(parent_frame):
    """
    Displays the Bulletin Board UI in the dashboard content area.
    """
    clear_dashboard_content(parent_frame)
    tk.Label(parent_frame, text="Bulletin Board", font=("Arial", 16, "bold"), fg="#333333").pack(pady=20)
    tk.Label(parent_frame, text="Browse and post announcements.", font=("Arial", 12)).pack(pady=10)

def show_emergency_contacts(parent_frame):
    """
    Displays the Emergency Contacts UI in the dashboard content area.
    """
    clear_dashboard_content(parent_frame)
    tk.Label(parent_frame, text="Emergency Contacts & Quick Access", font=("Arial", 16, "bold"), fg="#333333").pack(pady=20)
    tk.Label(parent_frame, text="Quick access to security, counseling, and health services.", font=("Arial", 12)).pack(pady=10)

def create_dashboard_window():
    """
    Creates and displays the main dashboard window of the application.
    This window will appear after a successful login.
    """
    dashboard_window = tk.Toplevel() # Toplevel creates a new, independent top-level window
    dashboard_window.title("The Vaquero Network - Dashboard")
    dashboard_window.geometry("1000x700") # Increased size for dashboard

    # Configure grid for main layout (sidebar and content area)
    dashboard_window.grid_rowconfigure(0, weight=1)
    dashboard_window.grid_columnconfigure(0, weight=0)
    dashboard_window.grid_columnconfigure(1, weight=1)

    #Sidebar Frame
    sidebar_frame = tk.Frame(dashboard_window, bg="#e0e0e0", width=200, relief="raised", bd=2)
    sidebar_frame.grid(row=0, column=0, sticky="nswe")
    sidebar_frame.pack_propagate(False) # Prevent frame from shrinking to content

    tk.Label(sidebar_frame, text="Navigation", font=("Arial", 14, "bold"), bg="#e0e0e0", fg="#333333").pack(pady=20)

    # Main Content Frame (declared before sidebar buttons so it exists when they call it)
    dashboard_content_frame = tk.Frame(dashboard_window, bg="#ffffff", relief="sunken", bd=2)
    dashboard_content_frame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)


    # Dashboard navigation buttons
    # Note: We pass dashboard_content_frame to these functions
    home_button = tk.Button(sidebar_frame, text="Home", command=lambda: show_welcome_text(dashboard_content_frame), width=20, pady=5)
    home_button.pack(pady=5)

    activities_button = tk.Button(sidebar_frame, text="Activities", command=lambda: show_activities_manager(dashboard_content_frame), width=20, pady=5)
    activities_button.pack(pady=5)

    calendar_button = tk.Button(sidebar_frame, text="Calendar", command=lambda: show_event_calendar(dashboard_content_frame), width=20, pady=5)
    calendar_button.pack(pady=5)

    bulletin_button = tk.Button(sidebar_frame, text="Bulletin Board", command=lambda: show_bulletin_board(dashboard_content_frame), width=20, pady=5)
    bulletin_button.pack(pady=5)

    emergency_button = tk.Button(sidebar_frame, text="Emergency Contacts", command=lambda: show_emergency_contacts(dashboard_content_frame), width=20, pady=5)
    emergency_button.pack(pady=5)

    # Display welcome text when dashboard opens
    show_welcome_text(dashboard_content_frame)
