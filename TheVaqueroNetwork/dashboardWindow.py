import tkinter as tk

# Default text to show when the dashboard opens
WELCOME_TEXT = (
    "Welcome to The Vaquero Network!\n\n"
    "This is your dashboard home.\n\n"
    "Use the navigation on the left to explore Activities, Calendar, Bulletin Board, and Emergency Contacts."
)

class DashboardWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("The Vaquero Network - Dashboard")
        self.geometry("1000x700")

        # Configure grid for main layout (sidebar and content area)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # Build UI sections
        self._build_sidebar()
        self._build_content()

        # Initially show welcome text
        self.show_welcome_text()

    # ----- Layout helpers -----
    def _build_sidebar(self):
        self.sidebar_frame = tk.Frame(self, bg="#e0e0e0", width=200, relief="raised", bd=2)
        self.sidebar_frame.grid(row=0, column=0, sticky="nswe")
        self.sidebar_frame.pack_propagate(False)

        tk.Label(
            self.sidebar_frame,
            text="Navigation",
            font=("Arial", 14, "bold"),
            bg="#e0e0e0",
            fg="#333333"
        ).pack(pady=20)

        # Navigation buttons
        tk.Button(self.sidebar_frame, text="Home", width=20, pady=5, command=self.show_welcome_text).pack(pady=5)
        tk.Button(self.sidebar_frame, text="Activities", width=20, pady=5, command=self.show_activities_manager).pack(pady=5)
        tk.Button(self.sidebar_frame, text="Calendar", width=20, pady=5, command=self.show_event_calendar).pack(pady=5)
        tk.Button(self.sidebar_frame, text="Bulletin Board", width=20, pady=5, command=self.show_bulletin_board).pack(pady=5)
        tk.Button(self.sidebar_frame, text="Emergency Contacts", width=20, pady=5, command=self.show_emergency_contacts).pack(pady=5)

    def _build_content(self):
        self.content_frame = tk.Frame(self, bg="#ffffff", relief="sunken", bd=2)
        self.content_frame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

    # ----- Utilities -----
    def _clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    # ----- View methods -----
    def show_welcome_text(self, text: str | None = None):
        self._clear_content()
        message = text if text is not None else WELCOME_TEXT
        tk.Label(self.content_frame, text="Dashboard", font=("Arial", 16, "bold"), fg="#333333").pack(pady=(20, 10))
        tk.Message(self.content_frame, text=message, font=("Arial", 12), width=700, justify="left").pack(padx=20, pady=(0, 20))

    def show_activities_manager(self):
        self._clear_content()
        tk.Label(self.content_frame, text="Activities/Task Schedule Manager", font=("Arial", 16, "bold"), fg="#333333").pack(pady=20)
        tk.Label(self.content_frame, text="Here you can add, view, edit, and delete your tasks.", font=("Arial", 12)).pack(pady=10)

        tk.Button(self.content_frame, text="Add New Task", font=("Arial", 12, "bold"), bg="#5cb85c", fg="white", width=15).pack(pady=5)
        tk.Button(self.content_frame, text="View All Tasks", font=("Arial", 12, "bold"), bg="#0275d8", fg="white", width=15).pack(pady=5)

    def show_event_calendar(self):
        self._clear_content()
        tk.Label(self.content_frame, text="Event Calendar", font=("Arial", 16, "bold"), fg="#333333").pack(pady=20)
        tk.Label(self.content_frame, text="View and manage upcoming events.", font=("Arial", 12)).pack(pady=10)

    def show_bulletin_board(self):
        self._clear_content()
        tk.Label(self.content_frame, text="Bulletin Board", font=("Arial", 16, "bold"), fg="#333333").pack(pady=20)
        tk.Label(self.content_frame, text="Browse and post announcements.", font=("Arial", 12)).pack(pady=10)

    def show_emergency_contacts(self):
        self._clear_content()
        tk.Label(self.content_frame, text="Emergency Contacts & Quick Access", font=("Arial", 16, "bold"), fg="#333333").pack(pady=20)
        tk.Label(self.content_frame, text="Quick access to security, counseling, and health services.", font=("Arial", 12)).pack(pady=10)
