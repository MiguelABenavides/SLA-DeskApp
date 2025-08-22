import sqlite3

def init_db():
    """
    Initializes the SQLite database and creates the users and tasks tables if they don't exist.
    """
    conn = sqlite3.connect('vaquero_network.db') # Connects to or creates the database file
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

    conn.commit()
    conn.close()

def add_user(username, password):
    """
    Adds a new user to the database.
    Returns True on success, False on failure (e.g., username already exists).
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
    Checks if a username and password combination exists in the database.
    Returns True if a match is found, otherwise False.
    """
    conn = sqlite3.connect('vaquero_network.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def add_task(username, title, description=None, due_date=None):
    """
    Adds a new task for a user.
    Returns the ID of the new task on success, None on failure.
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
    Retrieves all tasks for a specific user.
    Returns a list of task tuples.
    """
    conn = sqlite3.connect('vaquero_network.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, due_date, status FROM tasks WHERE username = ?", (username,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def get_task(task_id):
    """
    Retrieves a specific task by ID.
    Returns a task tuple or None if not found.
    """
    conn = sqlite3.connect('vaquero_network.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, title, description, due_date, status FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()
    conn.close()
    return task

def update_task(task_id, title=None, description=None, due_date=None, status=None):
    """
    Updates an existing task.
    Returns True on success, False on failure.
    """
    try:
        conn = sqlite3.connect('vaquero_network.db')
        cursor = conn.cursor()

        # Get current task data
        cursor.execute("SELECT title, description, due_date, status FROM tasks WHERE id = ?", (task_id,))
        current = cursor.fetchone()

        if not current:
            return False

        # Use current values if new ones aren't provided
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
    Deletes a task by ID.
    Returns True on success, False on failure.
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
