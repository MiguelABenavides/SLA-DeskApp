import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as VaquerosMessager
from database import add_emergency_contact, get_emergency_contacts


class EmergencyContactsPanel(ttk.Frame):
    def __init__(self, parent, username):
        """
        Initializes the EmergencyContactsPanel.
        This panel allows users to add and view their emergency contacts.
        """

        super().__init__(parent, padding="10 10 10 10")
        self.username = username
        self.pack(fill="both", expand=True)

        # Panel title and description
        tk.Label(self, text="Emergency Contacts & Quick Access", font=("Inter", 16, "bold"), fg="#333333", bg="white").pack(pady=20)
        tk.Label(self, text="Quick access to security, counseling, and health services.", font=("Inter", 12), bg="white", fg="#555555").pack(pady=10)

        # Frame for emergency contact input fields
        contact_input_frame = ttk.Frame(self, padding="10 10 10 10")
        contact_input_frame.pack(pady=20, padx=20, fill="x")

        # Contact name input
        ttk.Label(contact_input_frame, text="Contact Name:").pack(pady=(5, 0), anchor="w")
        self.emergency_contact_name_entry = ttk.Entry(contact_input_frame, width=40)
        self.emergency_contact_name_entry.pack(pady=(0, 10), fill="x")

        # Contact number input
        ttk.Label(contact_input_frame, text="Contact Number:").pack(pady=(5, 0), anchor="w")
        self.emergency_contact_number_entry = ttk.Entry(contact_input_frame, width=40)
        self.emergency_contact_number_entry.pack(pady=(0, 10), fill="x")

        # Button to add a new contact
        ttk.Button(
            contact_input_frame,
            text="Add Contact",
            command=self._add_emergency_contact,
            style='Emergency.TButton'
        ).pack(pady=10)

        # Frame to display the list of saved contacts
        self.saved_contacts_display_frame = ttk.Frame(self, padding="10 10 10 10")
        self.saved_contacts_display_frame.pack(pady=(20, 10), padx=20, fill="both", expand=True)

        # Label for the saved contacts list
        tk.Label(self.saved_contacts_display_frame, text="Saved Contacts:", font=("Inter", 14, "bold"), fg="#333333", bg="white").pack(pady=(0, 10), anchor="w")

        # Text widget to display contacts, with scrollbar
        self.contacts_text_widget = tk.Text(
            self.saved_contacts_display_frame,
            font=("Inter", 12),
            bg="#f8f8f8",
            fg="#333333",
            relief="flat",
            borderwidth=1,
            height=10,
            wrap="word"
        )
        self.contacts_text_widget.pack(fill="both", expand=True)

        # Scrollbar for the contacts text widget
        scrollbar = ttk.Scrollbar(self.contacts_text_widget, command=self.contacts_text_widget.yview)
        self.contacts_text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Load and display contacts when the panel is initialized
        self._display_emergency_contacts()

    def _add_emergency_contact(self):
        """
        Handles adding an emergency contact.
        Saves the contact to the database and refreshes the displayed list.
        """

        name = self.emergency_contact_name_entry.get().strip()
        number = self.emergency_contact_number_entry.get().strip()

        if name and number:
            # Call the database function to add the contact
            if add_emergency_contact(self.username, name, number):
                VaquerosMessager.showinfo("Contact Added", f"Contact '{name}' added successfully!")
                self.emergency_contact_name_entry.delete(0, tk.END)  # Clear input fields
                self.emergency_contact_number_entry.delete(0, tk.END)
                self._display_emergency_contacts()  # Refresh the displayed list of contacts
            else:
                VaquerosMessager.showerror("Error", "Failed to add contact to database.")
        else:
            VaquerosMessager.showwarning("Input Error", "Please enter both name and number for the contact.")

    def _display_emergency_contacts(self):
        """
        Retrieves emergency contacts from the database and displays them in the UI.
        """

        self.contacts_text_widget.config(state="normal")  # Enable editing to clear/insert
        self.contacts_text_widget.delete(1.0, tk.END)  # Clear existing content

        contacts = get_emergency_contacts(self.username)  # Fetch contacts for the current user

        if contacts:
            for contact_id, name, number in contacts:
                self.contacts_text_widget.insert(tk.END, f"Name: {name}\nNumber: {number}\n\n")
        else:
            self.contacts_text_widget.insert(tk.END, "No contacts added yet.")

        self.contacts_text_widget.config(state="disabled")  # Disable editing after displaying
