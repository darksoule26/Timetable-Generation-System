import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Create the teachers table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        subject TEXT NOT NULL,
        class TEXT NOT NULL,
        type TEXT NOT NULL,
        num_classes INTEGER NOT NULL
    )
''')

print("Tables created successfully!")

# Commit the changes and close the connection
conn.commit()
conn.close()
