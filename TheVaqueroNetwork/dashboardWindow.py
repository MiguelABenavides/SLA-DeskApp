import tkinter as tk
from datetime import datetime
import calendar

# Welcome message displayed on the dashboard home screen
WELCOME_TEXT = (
    "Welcome to The Vaquero Network!\n\n"
    "This is your dashboard home.\n\n"
    "Use the navigation on the left to explore Activities, Calendar, Bulletin Board, and Emergency Contacts."
)

class DashboardWindow(tk.Toplevel):
    def __init__(self, master=None, username: str = "Guest"):
        super().__init__(master=master) # Initialize the Toplevel window
        self.title("The Vaquero Network - Dashboard") # Set window title
        self.geometry("1000x700") # Set initial window size
        self.username = username # Store the logged-in username for personalization

        # Configure grid layout for the main window (sidebar and content area)
        self.grid_rowconfigure(0, weight=1) # Make row 0 expandable vertically
        self.grid_columnconfigure(0, weight=0) # Sidebar column (column 0) does not expand horizontally
        self.grid_columnconfigure(1, weight=1) # Main content column (column 1) expands horizontally

        # Build UI sections for the dashboard
        self._build_sidebar()
        self._build_content()

        # Display the welcome text when the dashboard first opens
        self.show_welcome_text()

    def _build_sidebar(self):
        # Create and configure the sidebar frame, placed in grid column 0
        self.sidebar_frame = tk.Frame(self, bg="#1a344a", width=200, relief="raised", bd=2)
        self.sidebar_frame.grid(row=0, column=0, sticky="nswe") # Expand to fill grid cell
        self.sidebar_frame.pack_propagate(False) # Prevent frame from shrinking if content is small

        # Add navigation title label to the top of the sidebar
        tk.Label(
            self.sidebar_frame,
            text="Navigation",
            font=("Arial", 16, "bold"),
            bg="#1a344a", # Match sidebar background
            fg="white"
        ).pack(pady=20) # Add vertical padding

        # Define common style parameters for all sidebar navigation buttons
        button_style = {
            "font": ("Arial", 12, "bold"), # Font for button text
            "bg": "#4a6784", # Background color for buttons
            "fg": "white", # Foreground (text) color for buttons
            "width": 20, # Fixed width for buttons
            "pady": 8, # Vertical padding inside buttons
            "relief": "raised", # 3D effect for button appearance
            "bd": 3 # Border thickness for buttons
        }

        # Create and pack navigation buttons using the defined style
        tk.Button(self.sidebar_frame, text="Home", command=self.show_welcome_text, **button_style).pack(pady=10)
        tk.Button(self.sidebar_frame, text="Activities", command=self.show_activities_manager, **button_style).pack(pady=10)
        tk.Button(self.sidebar_frame, text="Calendar", command=self.show_event_calendar, **button_style).pack(pady=10)
        tk.Button(self.sidebar_frame, text="Bulletin Board", command=self.show_bulletin_board, **button_style).pack(pady=10)
        tk.Button(self.sidebar_frame, text="Emergency Contacts", command=self.show_emergency_contacts, **button_style).pack(pady=10)

    def _build_content(self):
        # Create and configure the main content frame, placed in grid column 1
        self.content_frame = tk.Frame(self, bg="#ffffff", relief="sunken", bd=2)
        self.content_frame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10) # Expand to fill grid cell with padding

    def _clear_content(self):
        # Destroy all widgets currently displayed within the content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_welcome_text(self, text: str | None = None):
        self._clear_content() # Clear existing content
        message = text if text is not None else WELCOME_TEXT # Use provided text or default welcome message
        tk.Label(self.content_frame, text="Dashboard Home", font=("Arial", 16, "bold"), fg="#333333").pack(pady=(20, 10))
        tk.Message(self.content_frame, text=message, font=("Arial", 12), width=700, justify="left").pack(padx=20, pady=(0, 20))

    def show_activities_manager(self):
        self._clear_content() # Clear existing content
        tk.Label(self.content_frame, text="Activities/Task Schedule Manager", font=("Arial", 16, "bold"), fg="#333333").pack(pady=20)
        tk.Label(self.content_frame, text="Here you can add, view, edit, and delete your tasks.", font=("Arial", 12)).pack(pady=10)

        # Placeholder buttons for future CRUD operations
        tk.Button(self.content_frame, text="Add New Task", font=("Arial", 12, "bold"), bg="#5cb85c", fg="white", width=15).pack(pady=5)
        tk.Button(self.content_frame, text="View All Tasks", font=("Arial", 12, "bold"), bg="#0275d8", fg="white", width=15).pack(pady=5)

    def show_event_calendar(self):
        self._clear_content() # Clear existing content
        tk.Label(self.content_frame, text="Event Calendar", font=("Arial", 16, "bold"), fg="#333333").pack(pady=20)

        # Get and format the current date for display
        today = datetime.now()
        current_date_text = today.strftime("Today is %A, %B %d, %Y")
        tk.Label(self.content_frame, text=current_date_text, font=("Arial", 14), fg="#555555").pack(pady=(10, 20))

        # Generate a text calendar for the current month and year
        cal = calendar.month(today.year, today.month)

        # Create a frame to act as a container for centering the calendar label
        calendar_container_frame = tk.Frame(self.content_frame, bg="#ffffff")
        calendar_container_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Display the text calendar in a label, configured for large, bold, centered text
        calendar_label = tk.Label(
            calendar_container_frame, # Pack into the container frame
            text=cal,
            font=("Courier New", 24, "bold"), # Larger, bold, monospaced font for alignment
            justify="center", # Center text lines horizontally
            anchor="center",  # Center content within the label's allocated space
            bg="#f0f0f0", # Light background for the calendar area
            relief="groove",
            padx=20, # Horizontal padding around calendar text
            pady=20  # Vertical padding around calendar text
        )
        calendar_label.pack(expand=True) # Allow label to expand and help with centering within container

    def show_bulletin_board(self):
        self._clear_content() # Clear existing content
        tk.Label(self.content_frame, text="Bulletin Board", font=("Arial", 16, "bold"), fg="#333333").pack(pady=20)
        tk.Label(self.content_frame, text="Browse and post announcements.", font=("Arial", 12)).pack(pady=10)

    def show_emergency_contacts(self):
        self._clear_content() # Clear existing content
        tk.Label(self.content_frame, text="Emergency Contacts & Quick Access", font=("Arial", 16, "bold"), fg="#333333").pack(pady=20)
        tk.Label(self.content_frame, text="Quick access to security, counseling, and health services.", font=("Arial", 12)).pack(pady=10)
