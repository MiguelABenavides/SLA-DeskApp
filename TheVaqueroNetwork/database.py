import sqlite3

def init_db():
    """
    Initializes the SQLite database and creates the users, tasks, emergency_contacts, and announcements tables if they don't exist.
    """

    conn = sqlite3.connect('vaquero_network.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY (username) REFERENCES users(username)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emergency_contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            contact_name TEXT NOT NULL,
            contact_number TEXT NOT NULL,
            FOREIGN KEY (username) REFERENCES users(username)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS announcements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (username) REFERENCES users(username)
        )
    ''')

    conn.commit()
    conn.close()

def add_user(username, password):
    """
    Adds a new user to the database. Returns True on success, False on failure (e.g., username already exists).
    """

    try:
        conn = sqlite3.connect('vaquero_network.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def validate_user(username, password):
    """
    Checks if a username and password combination exists in the database. Returns True if a match is found, otherwise False.
    """

    conn = sqlite3.connect('vaquero_network.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def add_task(username, title, description=None, due_date=None):
    """
    Adds a new task for a user. Returns the ID of the new task on success, None on failure.
    """

    try:
        conn = sqlite3.connect('vaquero_network.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (username, title, description, due_date) VALUES (?, ?, ?, ?)",
            (username, title, description, due_date)
        )
        task_id = cursor.lastrowid
        conn.commit()
        return task_id
    except Exception as e:
        print(f"Error adding task: {e}")
        return None
    finally:
        conn.close()

def get_tasks(username):
    """
    Retrieves all tasks for a specific user. Returns a list of task tuples.
    """

    conn = sqlite3.connect('vaquero_network.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, due_date, status FROM tasks WHERE username = ?", (username,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def get_task(task_id):
    """
    Retrieves a specific task by ID. Returns a task tuple or None if not found.
    """

    conn = sqlite3.connect('vaquero_network.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, title, description, due_date, status FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()
    conn.close()
    return task

def update_task(task_id, title=None, description=None, due_date=None, status=None):
    """
    Updates an existing task. Returns True on success, False on failure.
    """

    try:
        conn = sqlite3.connect('vaquero_network.db')
        cursor = conn.cursor()

        cursor.execute("SELECT title, description, due_date, status FROM tasks WHERE id = ?", (task_id,))
        current = cursor.fetchone()

        if not current:
            return False

        new_title = title if title is not None else current[0]
        new_description = description if description is not None else current[1]
        new_due_date = due_date if due_date is not None else current[2]
        new_status = status if status is not None else current[3]

        cursor.execute(
            "UPDATE tasks SET title = ?, description = ?, due_date = ?, status = ? WHERE id = ?",
            (new_title, new_description, new_due_date, new_status, task_id)
        )
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Error updating task: {e}")
        return False
    finally:
        conn.close()

def delete_task(task_id):
    """
    Deletes a task by ID. Returns True on success, False on failure.
    """
    try:
        conn = sqlite3.connect('vaquero_network.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Error deleting task: {e}")
        return False
    finally:
        conn.close()

def add_emergency_contact(username, contact_name, contact_number):
    """
    Adds a new emergency contact for a specific user. Returns True on success, False on failure.
    """
    try:
        conn = sqlite3.connect('vaquero_network.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO emergency_contacts (username, contact_name, contact_number) VALUES (?, ?, ?)",
            (username, contact_name, contact_number)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error adding emergency contact: {e}")
        return False
    finally:
        conn.close()

def get_emergency_contacts(username):
    """
    Retrieves all emergency contacts for a specific user. Returns a list of contact tuples (id, contact_name, contact_number).
    """

    conn = sqlite3.connect('vaquero_network.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, contact_name, contact_number FROM emergency_contacts WHERE username = ?",
        (username,)
    )
    contacts = cursor.fetchall()
    conn.close()
    return contacts

def add_announcement(username, title, content):
    """
    Adds a new announcement to the bulletin board. Returns True on success, False on failure.
    """

    try:
        conn = sqlite3.connect('vaquero_network.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO announcements (username, title, content) VALUES (?, ?, ?)",
            (username, title, content)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error adding announcement: {e}")
        return False
    finally:
        conn.close()

def get_announcements():
    """
    Retrieves all announcements from the bulletin board, ordered by timestamp (newest first). Returns a list of announcement tuples (id, username, title, content, timestamp).
    """
    conn = sqlite3.connect('vaquero_network.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, title, content, timestamp FROM announcements ORDER BY timestamp DESC")
    announcements = cursor.fetchall()
    conn.close()
    return announcements
