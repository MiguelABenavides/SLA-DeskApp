import tkinter as tk
from tkinter import ttk
from datetime import datetime
import calendar

class CalendarPanel(ttk.Frame):
    def __init__(self, parent, username):
        """
        Initializes the CalendarPanel.
        This panel displays the current date and a text-based calendar for the current month.
        """
        super().__init__(parent, padding="10 10 10 10")
        self.username = username
        self.pack(fill="both", expand=True)

        # Panel title
        tk.Label(self, text="Event Calendar", font=("Inter", 16, "bold"), fg="#333333", bg="white").pack(pady=20)

        # Get and format the current date for display
        today = datetime.now()
        current_date_text = today.strftime("Today is %A, %B %d, %Y")
        tk.Label(self, text=current_date_text, font=("Inter", 14), fg="#555555", bg="white").pack(pady=(10, 20))

        # Generate a text calendar for the current month and year
        cal = calendar.month(today.year, today.month)

        # Frame to act as a container for centering the calendar label
        calendar_container_frame = tk.Frame(self, bg="white")
        calendar_container_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Label to display the text calendar
        tk.Label(
            calendar_container_frame,
            text=cal,
            font=("Courier New", 28, "bold"),
            justify="center",
            bg="#f0f0f0",
            relief="groove",
            padx=20,
            pady=20
        ).pack(side="top", anchor="center", pady=15)
