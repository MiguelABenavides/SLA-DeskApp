import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta  # Import timedelta for date calculations
import calendar


class CalendarPanel(ttk.Frame):
    def __init__(self, parent, username):
        """
        Initializes the CalendarPanel with a modern, grid-based calendar.
        """
        super().__init__(parent, padding="10 10 10 10")
        self.username = username
        self.pack(fill="both", expand=True)

        self.current_date = datetime.now()  # Store current date for navigation
        self._setup_styles()  # Setup custom styles for calendar elements

        # --- Panel Title ---
        tk.Label(self, text="Event Calendar", font=("Inter", 16, "bold"), fg="#0056b3", bg="white").pack(pady=20)

        # --- Month Navigation and Display ---
        nav_frame = ttk.Frame(self, style='Calendar.TFrame')  # Use a themed frame
        nav_frame.pack(pady=(10, 5))

        ttk.Button(nav_frame, text="<", command=self._prev_month, style='Calendar.Nav.TButton').pack(side="left",
                                                                                                     padx=5)
        self.month_year_label = ttk.Label(nav_frame, text="", font=("Inter", 16, "bold"), style='Calendar.TLabel')
        self.month_year_label.pack(side="left", padx=10)
        ttk.Button(nav_frame, text=">", command=self._next_month, style='Calendar.Nav.TButton').pack(side="left",
                                                                                                     padx=5)

        # --- Calendar Grid Frame ---
        self.calendar_frame = ttk.Frame(self, style='Calendar.TFrame')
        self.calendar_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self._display_calendar()  # Initial display of the calendar

    def _setup_styles(self):
        """
        Configures custom ttk styles for calendar elements.
        """
        style = ttk.Style(self)
        style.configure('Calendar.TFrame', background='white')
        style.configure('Calendar.TLabel', background='white', foreground='#333333', font=('Inter', 12))
        style.configure('Calendar.Weekday.TLabel', background='#f0f0f0', foreground='#0056b3',
                        font=('Inter', 12, 'bold'), borderwidth=1,
                        relief='solid')  # UTRGV Blue for weekdays, added border
        style.configure('Calendar.Day.TLabel', background='white', foreground='#333333', font=('Inter', 12),
                        borderwidth=1, relief='solid')  # Added border
        style.configure('Calendar.Today.TLabel', background='#F26722', foreground='white', font=('Inter', 12, 'bold'),
                        borderwidth=1, relief='solid')  # UTRGV Orange for today, added border
        style.configure('Calendar.OtherMonth.TLabel', background='white', foreground='#aaaaaa',
                        font=('Inter', 12, 'italic'), borderwidth=1,
                        relief='solid')  # Faded for other months, added border
        style.configure('Calendar.Nav.TButton',
                        font=('Inter', 10),  # Reduced font size from bold 10 to regular 10
                        foreground='white',
                        background='#0056b3',  # UTRGV Blue
                        padding=[5, 2],  # Reduced vertical padding to 5, horizontal to 2
                        relief='flat',
                        borderwidth=0
                        )
        style.map('Calendar.Nav.TButton',
                  background=[('active', '#003d80')],
                  foreground=[('active', 'white')]
                  )

    def _clear_calendar_grid(self):
        """
        Clears all widgets from the calendar grid frame.
        """
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

    def _display_calendar(self):
        """
        Generates and displays the calendar grid for the current month.
        """
        self._clear_calendar_grid()

        # Update month/year label
        self.month_year_label.config(text=self.current_date.strftime("%B %Y"))

        # Get calendar data for the current month
        cal_data = calendar.Calendar(firstweekday=calendar.MONDAY).monthdayscalendar(self.current_date.year,
                                                                                     self.current_date.month)

        # Weekday headers
        weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for col, day_name in enumerate(weekdays):
            ttk.Label(self.calendar_frame, text=day_name, style='Calendar.Weekday.TLabel', anchor="center").grid(row=0,
                                                                                                                 column=col,
                                                                                                                 padx=2,
                                                                                                                 pady=2,
                                                                                                                 sticky="nsew")
            self.calendar_frame.grid_columnconfigure(col, weight=1)  # Make columns expand

        # Days of the month
        row_offset = 1
        for week_index, week in enumerate(cal_data):
            for day_index, day in enumerate(week):
                day_label_text = str(day) if day != 0 else ""

                style_name = 'Calendar.Day.TLabel'
                if day == 0:  # Days from previous/next month
                    style_name = 'Calendar.OtherMonth.TLabel'
                elif day == self.current_date.day and self.current_date.month == datetime.now().month and self.current_date.year == datetime.now().year:
                    style_name = 'Calendar.Today.TLabel'  # Highlight today's date

                day_label = ttk.Label(self.calendar_frame, text=day_label_text, style=style_name, anchor="center")
                day_label.grid(row=row_offset + week_index, column=day_index, padx=2, pady=2, sticky="nsew")
                self.calendar_frame.grid_rowconfigure(row_offset + week_index, weight=1)  # Make rows expand

    def _prev_month(self):
        """
        Navigates to the previous month.
        """
        self.current_date = self.current_date.replace(day=1)  # Set to 1st to avoid month-end issues
        self.current_date -= timedelta(days=1)  # Go back to last day of previous month
        self.current_date = self.current_date.replace(day=1)  # Set to 1st of previous month
        self._display_calendar()

    def _next_month(self):
        """
        Navigates to the next month.
        """
        self.current_date = self.current_date.replace(day=1)  # Set to 1st to avoid month-end issues
        if self.current_date.month == 12:
            self.current_date = self.current_date.replace(year=self.current_date.year + 1, month=1)
        else:
            self.current_date = self.current_date.replace(month=self.current_date.month + 1)
        self._display_calendar()
