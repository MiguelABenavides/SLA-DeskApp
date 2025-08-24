Developed By: Miguel Benavides, Gera Quintana, Mohammad Almutairi 

The Vaquero Network: Desktop Application
Project Overview

Welcome to The Vaquero Network, a social life application designed to enhance the student experience at UTRGV. This repository contains the code for the desktop application, built using Python with the Tkinter GUI framework. The app aims to streamline just a few aspects of student life by providing tools for managing activities, viewing events, browsing announcements, and accessing essential emergency contacts.

The application follows CRUD (Create, Read, Update, Delete) principles for data management across its features, ensuring users can fully interact with their information.
Features

The desktop application currently offers the following core functionalities, all accessible via a modern, themed dashboard:
1. User Authentication & Account Management

    Login: Securely log in with existing credentials.
<img width="399" height="409" alt="Screenshot 2025-08-23 at 11 36 31 PM" src="https://github.com/user-attachments/assets/438f4bb2-d516-4d7c-910c-7c23c36ce765" />

    Create Account: Register new user accounts.
<img width="878" height="717" alt="Screenshot 2025-08-23 at 11 38 08 PM" src="https://github.com/user-attachments/assets/83802b62-32c7-4a29-9714-040df123520c" />

    Persistent Storage: User data (including login info, tasks, contacts, and announcements) is stored locally using SQLite.

2. Dashboard Navigation

    An intuitive sidebar allows easy navigation between different sections of the app.
<img width="1066" height="783" alt="Screenshot 2025-08-23 at 11 40 17 PM" src="https://github.com/user-attachments/assets/462ad4e5-0669-405e-808e-3049197dcb0d" />

3. Activities/Task Schedule Manager

    Add New Task: Create tasks with a title, optional description, and due date.

    View Tasks: Display a list of all your active tasks.
<img width="1120" height="808" alt="Screenshot 2025-08-23 at 11 40 42 PM" src="https://github.com/user-attachments/assets/04f0f10e-92b9-47a2-b3fe-79ffc93e3e7e" />

4. Event Calendar

    Current Date Display: Shows today's date prominently.

    Interactive Calendar: A visually appealing, grid-based calendar for the current month, with navigation to view previous and next months.
<img width="1033" height="758" alt="Screenshot 2025-08-23 at 11 40 59 PM" src="https://github.com/user-attachments/assets/bf509c5c-fa33-4c13-8ef1-5a8d7fa8f98c" />

5. Bulletin Board

    Post Announcement: Create and share announcements with a title and content.

    View Announcements: Browse recent announcements posted by users.
<img width="1051" height="779" alt="Screenshot 2025-08-23 at 11 41 25 PM" src="https://github.com/user-attachments/assets/9543f665-4a9b-46f7-abee-454472ecafe0" />

6. Emergency Contacts & Quick Access

    Add Contact: Store names and phone numbers of emergency contacts.

    View Saved Contacts: Display a list of your emergency contacts.
<img width="1111" height="823" alt="Screenshot 2025-08-23 at 11 41 50 PM" src="https://github.com/user-attachments/assets/39f2fc95-0cb4-4a68-9c1e-276631a0cc9c" />

Technologies Used

    Python 3.x: The core programming language.

    Tkinter: Python's standard GUI library for creating the desktop interface.

    tkinter.ttk: The Themed Tkinter module, used for modernizing the UI widgets and applying consistent styling (inspired by UTRGV's blue and orange palette).

    SQLite: A lightweight, file-based database used for local data persistence (users, tasks, announcements, emergency contacts).

Project Structure

The application is modularly organized into several Python files:

TheVaqueroNetwork/
├── SLAMain.py              # Main application entry point

├── loginWindow.py          # Handles login and account creation UI/logic

├── dashboardWindow.py      # Orchestrates the main dashboard layout and panel loading

├── database.py             # Manages all SQLite database operations (tables, CRUD functions)

├── createAccount.py        # UI/logic for creating new user accounts

├── activity.py             # Panel for Activities/Task Schedule Manager

├── calendar_panel.py       # Panel for the Event Calendar

├── bulletin_board.py       # Panel for the Bulletin Board

├── emergency_contact.py    # Panel for Emergency Contacts & Quick Access

└── vaquero_network.db      # SQLite database file (generated on first run)


Setup and Installation

To get the desktop application running on your local machine:
1. Clone the Repository

git clone <your-repository-url>
cd TheVaqueroNetwork

2. Ensure Python is Installed

Make sure you have Python 3.10 or newer installed on your system.
3. Run the Application

Execute the main script from your terminal:

python SLAMain.py

The vaquero_network.db SQLite database file will be automatically created in the TheVaqueroNetwork directory upon the first run.
Agile Planning & Team Roles

This project is being developed using Agile methodologies, emphasizing iterative development and feedback. We have been conducting regular sprints.

    Version Control: All code changes are managed using Git and hosted on GitHub, utilizing feature branches for new developments.

    Team Roles: [This section would typically detail specific team member roles, e.g., Frontend Developer (Tkinter), Backend Developer (Database), QA Tester, Project Lead. You can fill this in based on your team's assignments.]
