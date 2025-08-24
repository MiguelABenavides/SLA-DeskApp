import tkinter as tk
from tkinter import ttk

# Import panel classes for modular dashboard sections
from activity import ActivitiesPanel
from calendar_panel import CalendarPanel
from bulletin_board import BulletinBoardPanel
from emergency_contact import EmergencyContactsPanel

# Welcome message displayed on the dashboard home screen
WELCOME_TEXT = (
    "Welcome to The Vaquero Network!\n\n"
    "This is your dashboard home.\n\n"
    "Use the navigation on the left to explore Activities, Calendar, Bulletin Board, and Emergency Contacts."
)


class DashboardWindow(tk.Toplevel):
    def __init__(self, master=None, username: str = "Guest"):
        super().__init__(master=master)
        self.title("The Vaquero Network - Dashboard")
        self.geometry("1000x700")
        self.username = username

        # Configure ttk styles for the dashboard
        style = ttk.Style(self)
        style.theme_use('clam')

        # Configure global fonts and colors for ttk widgets within this dashboard
        style.configure('.', font=('Inter', 10))
        style.configure('TLabel', font=('Inter', 12), foreground='#333333', background='white')
        style.configure('TEntry', font=('Inter', 12), fieldbackground='#f0f0f0', foreground='#333333', borderwidth=1,
                        relief='flat')

        # Configure sidebar button styles (UTRGV Blue)
        style.configure('Sidebar.TButton',
                        font=('Inter', 12, 'bold'),
                        foreground='white',
                        background='#0056b3',
                        padding=10,
                        relief='flat',
                        borderwidth=0
                        )
        style.map('Sidebar.TButton',
                  background=[('active', '#003d80')],
                  foreground=[('active', 'white')]
                  )

        # Configure content area button styles (UTRGV Orange for primary actions)
        style.configure('Content.TButton',
                        font=('Inter', 12, 'bold'),
                        foreground='white',
                        background='#F26722',
                        padding=10,
                        relief='flat',
                        borderwidth=0
                        )
        style.map('Content.TButton',
                  background=[('active', '#d95d1e')],
                  foreground=[('active', 'white')]
                  )

        # Configure style for the Emergency Contact Add button (keeping red for emergency)
        style.configure('Emergency.TButton',
                        font=('Inter', 12, 'bold'),
                        foreground='white',
                        background='#e74c3c',
                        padding=10,
                        relief='flat',
                        borderwidth=0
                        )
        style.map('Emergency.TButton',
                  background=[('active', '#c0392b')],  # Darken on hover
                  foreground=[('active', 'white')]
                  )

        # Configure style for Bulletin Board Post button (UTRGV Blue)
        style.configure('Post.TButton',
                        font=('Inter', 12, 'bold'),
                        foreground='white',
                        background='#0056b3',  # UTRGV Blue
                        padding=10,
                        relief='flat',
                        borderwidth=0
                        )
        style.map('Post.TButton',
                  background=[('active', '#003d80')],  # Darker UTRGV Blue on hover
                  foreground=[('active', 'white')]
                  )

        # Configure grid layout for the main window (sidebar and content area)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # Build UI sections for the dashboard
        self._build_sidebar()
        self._build_content()

        # Display the welcome text when the dashboard first opens
        self.show_welcome_text()

        # Set window background explicitly for consistency
        self.configure(bg='white')

    def _build_sidebar(self):
        self.sidebar_frame = tk.Frame(self, bg="#003366", width=200, relief="raised", bd=2)
        self.sidebar_frame.grid(row=0, column=0, sticky="nswe")
        self.sidebar_frame.pack_propagate(False)

        tk.Label(
            self.sidebar_frame,
            text="Navigation",
            font=("Inter", 16, "bold"),
            bg="#003366",
            fg="white"
        ).pack(pady=20)

        ttk.Button(self.sidebar_frame, text="Home", command=self.show_welcome_text, style='Sidebar.TButton').pack(pady=10)
        ttk.Button(self.sidebar_frame, text="Activities", command=self.show_activities_manager, style='Sidebar.TButton').pack(pady=10)
        ttk.Button(self.sidebar_frame, text="Calendar", command=self.show_event_calendar, style='Sidebar.TButton').pack(pady=10)
        ttk.Button(self.sidebar_frame, text="Bulletin Board", command=self.show_bulletin_board, style='Sidebar.TButton').pack(pady=10)
        ttk.Button(self.sidebar_frame, text="Emergency Contacts", command=self.show_emergency_contacts, style='Sidebar.TButton').pack(pady=10)

    def _build_content(self):
        self.content_frame = tk.Frame(self, bg="#ffffff", relief="sunken", bd=2)
        self.content_frame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
        self.content_frame.configure(bg='white')

    def _clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_welcome_text(self, text: str | None = None):
        self._clear_content()
        message = text if text is not None else WELCOME_TEXT
        tk.Label(self.content_frame, text="Dashboard Home", font=("Inter", 18, "bold"), fg="#0056b3", bg="white").pack(
            pady=(20, 10))
        tk.Message(self.content_frame, text=message, font=("Inter", 12), width=700, justify="left", bg="white",
                   fg="#555555").pack(padx=20, pady=(0, 20))

    def show_activities_manager(self):
        self._clear_content()
        ActivitiesPanel(self.content_frame, self.username)

    def show_event_calendar(self):
        self._clear_content()
        CalendarPanel(self.content_frame, self.username)

    def show_bulletin_board(self):
        self._clear_content()
        BulletinBoardPanel(self.content_frame, self.username)

    def show_emergency_contacts(self):
        self._clear_content()
        EmergencyContactsPanel(self.content_frame, self.username)