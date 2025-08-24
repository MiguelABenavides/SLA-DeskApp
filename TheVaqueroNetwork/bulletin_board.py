# bulletin_board_panel.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as VaquerosMessager  # Used for showing messages
from database import add_announcement, get_announcements  # Import database functions for announcements


class BulletinBoardPanel(ttk.Frame):
    def __init__(self, parent, username):
        """
        Initializes the BulletinBoardPanel.
        This panel allows users to post and view announcements.

        Args:
            parent: The parent widget (e.g., the content frame of the dashboard).
            username (str): The username of the currently logged-in user.
        """
        super().__init__(parent, padding="10 10 10 10")
        self.username = username
        self.pack(fill="both", expand=True)  # Make the panel fill its parent frame

        # --- Panel Title and Description ---
        tk.Label(self, text="Bulletin Board", font=("Inter", 16, "bold"), fg="#0056b3", bg="white").pack(pady=20) # UTRGV Blue for heading
        tk.Label(self, text="Browse and post announcements.", font=("Inter", 12), bg="white", fg="#555555").pack(pady=10)

        # --- Announcement Posting Section ---
        post_frame = ttk.Frame(self, padding="10 10 10 10")
        post_frame.pack(pady=10, padx=20, fill="x")

        ttk.Label(post_frame, text="New Announcement Title:").pack(pady=(5, 0), anchor="w")
        self.announcement_title_entry = ttk.Entry(post_frame, width=60)
        self.announcement_title_entry.pack(pady=(0, 10), fill="x")

        ttk.Label(post_frame, text="Announcement Content:").pack(pady=(5, 0), anchor="w")
        self.announcement_content_text = tk.Text(post_frame, height=5, width=60, font=("Inter", 12), relief="flat", borderwidth=1, bg="#f0f0f0", fg="#333333")
        self.announcement_content_text.pack(pady=(0, 10), fill="x", expand=True)

        ttk.Button(
            post_frame,
            text="Post Announcement",
            command=self._post_announcement,  # Calls the method to post an announcement
            style='Post.TButton'
        ).pack(pady=10)

        # --- Display Announcements Section ---
        tk.Label(self, text="Recent Announcements:", font=("Inter", 14, "bold"), fg="#333333", bg="white").pack(pady=(20, 10), anchor="w", padx=20)

        # Text widget to display announcements, with scrollbar
        self.announcements_text_widget = tk.Text(
            self,
            font=("Inter", 12),
            bg="#f8f8f8",
            fg="#333333",
            relief="flat",
            borderwidth=1,
            height=15,
            wrap="word"
        )
        self.announcements_text_widget.pack(fill="both", expand=True, padx=20, pady=10)

        scrollbar = ttk.Scrollbar(self.announcements_text_widget, command=self.announcements_text_widget.yview)
        self.announcements_text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Load and display announcements when the panel is initialized
        self._display_announcements()

    def _post_announcement(self):
        """
        Handles posting a new announcement.
        Saves the announcement to the database and refreshes the displayed list.
        """
        title = self.announcement_title_entry.get().strip()
        content = self.announcement_content_text.get("1.0", tk.END).strip()

        if title and content:
            if add_announcement(self.username, title, content):
                VaquerosMessager.showinfo("Announcement Posted", "Your announcement has been posted!")
                self.announcement_title_entry.delete(0, tk.END)  # Clear title field
                self.announcement_content_text.delete("1.0", tk.END)  # Clear content field
                self._display_announcements()  # Refresh the displayed list
            else:
                VaquerosMessager.showerror("Error", "Failed to post announcement to database.")
        else:
            VaquerosMessager.showwarning("Input Error", "Please enter both a title and content for the announcement.")

    def _display_announcements(self):
        """
        Retrieves announcements from the database and displays them in the UI.
        """
        self.announcements_text_widget.config(state="normal")  # Enable editing to clear/insert
        self.announcements_text_widget.delete(1.0, tk.END)  # Clear existing content

        announcements = get_announcements()  # Fetch all announcements

        if announcements:
            for ann_id, username, title, content, timestamp in announcements:
                self.announcements_text_widget.insert(tk.END, f"Title: {title}\n")
                self.announcements_text_widget.insert(tk.END, f"Posted by: {username} on {timestamp}\n")
                self.announcements_text_widget.insert(tk.END, f"Content: {content}\n")
                self.announcements_text_widget.insert(tk.END, "-" * 50 + "\n\n")  # Separator
        else:
            self.announcements_text_widget.insert(tk.END, "No announcements posted yet.")

        self.announcements_text_widget.config(state="disabled")  # Disable editing after displaying
