import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as VaquerosMessager
from database import add_task, get_tasks  # Import database functions for tasks


class ActivitiesPanel(ttk.Frame):
    def __init__(self, parent, username):
        """
        Initializes the ActivitiesPanel.
        This panel allows users to add and view their tasks.
        """
        super().__init__(parent, padding="10 10 10 10")
        self.username = username
        self.pack(fill="both", expand=True)

        # Panel title and description
        tk.Label(self, text="Activities/Task Schedule Manager", font=("Inter", 16, "bold"), fg="#333333", bg="white").pack(pady=20)
        tk.Label(self, text="Here you can add, view, edit, and delete your tasks.", font=("Inter", 12), bg="white", fg="#555555").pack(pady=10)

        # Frame for task input fields
        task_input_frame = ttk.Frame(self, padding="10 10 10 10")
        task_input_frame.pack(pady=20, padx=20, fill="x")

        # Task title input field
        ttk.Label(task_input_frame, text="Task Title:").pack(pady=(5, 0), anchor="w")
        self.task_title_entry = ttk.Entry(task_input_frame, width=60)
        self.task_title_entry.pack(pady=(0, 10), fill="x")

        # Task description input field
        ttk.Label(task_input_frame, text="Description (Optional):").pack(pady=(5, 0), anchor="w")
        self.task_description_entry = ttk.Entry(task_input_frame, width=60)
        self.task_description_entry.pack(pady=(0, 10), fill="x")

        # Task due date input field
        ttk.Label(task_input_frame, text="Due Date (YYYY-MM-DD, Optional):").pack(pady=(5, 0), anchor="w")
        self.task_due_date_entry = ttk.Entry(task_input_frame, width=60)
        self.task_due_date_entry.pack(pady=(0, 10), fill="x")

        # Button to add a new task
        ttk.Button(
            task_input_frame,
            text="Add Task",
            command=self._add_task,
            style='Content.TButton'
        ).pack(pady=10)

        # Label for the tasks list
        tk.Label(self, text="Your Tasks:", font=("Inter", 14, "bold"), fg="#333333", bg="white").pack(pady=(20, 10),anchor="w", padx=20)

        # Text widget to display tasks, with scrollbar
        self.tasks_text_widget = tk.Text(
            self,
            font=("Inter", 12),
            bg="#f8f8f8",
            fg="#333333",
            relief="flat",
            borderwidth=1,
            height=15,
            wrap="word"
        )
        self.tasks_text_widget.pack(fill="both", expand=True, padx=20, pady=10)

        # Scrollbar for the tasks text widget
        scrollbar = ttk.Scrollbar(self.tasks_text_widget, command=self.tasks_text_widget.yview)
        self.tasks_text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Load and display tasks when the panel is initialized
        self._display_tasks()

    def _add_task(self):
        """
        Handles adding a new task.
        Saves the task to the database and refreshes the displayed list.
        """
        title = self.task_title_entry.get().strip()
        description = self.task_description_entry.get().strip()
        due_date = self.task_due_date_entry.get().strip()

        if title:
            # Call the database function to add the task
            task_id = add_task(self.username, title, description if description else None,
                               due_date if due_date else None)
            if task_id:
                VaquerosMessager.showinfo("Task Added", f"Task '{title}' added successfully!")
                self.task_title_entry.delete(0, tk.END)  # Clear input fields
                self.task_description_entry.delete(0, tk.END)
                self.task_due_date_entry.delete(0, tk.END)
                self._display_tasks()  # Refresh the displayed list of tasks
            else:
                VaquerosMessager.showerror("Error", "Failed to add task to database.")
        else:
            VaquerosMessager.showwarning("Input Error", "Please enter a title for the task.")

    def _display_tasks(self):
        """
        Retrieves tasks from the database for the current user and displays them in the UI.
        """
        self.tasks_text_widget.config(state="normal")  # Enable editing to clear/insert
        self.tasks_text_widget.delete(1.0, tk.END)  # Clear existing content

        tasks = get_tasks(self.username)  # Fetch tasks for the current user

        if tasks:
            for task_id, title, description, due_date, status in tasks:
                self.tasks_text_widget.insert(tk.END, f"Title: {title}\n")
                if description:
                    self.tasks_text_widget.insert(tk.END, f"Description: {description}\n")
                if due_date:
                    self.tasks_text_widget.insert(tk.END, f"Due Date: {due_date}\n")
                self.tasks_text_widget.insert(tk.END, f"Status: {status}\n")
                self.tasks_text_widget.insert(tk.END, "-" * 50 + "\n\n")  # Separator
        else:
            self.tasks_text_widget.insert(tk.END, "No tasks added yet.")

        self.tasks_text_widget.config(state="disabled")  # Disable editing after displaying
