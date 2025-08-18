import sqlite3

def init_db():
    """
    Initializes the SQLite database and creates the users table if it doesn't exist.
    """
    conn = sqlite3.connect('vaquero_network.db') # Connects to or creates the database file
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
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
