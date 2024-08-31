import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('timetable.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE teachers
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             name TEXT, 
             subject TEXT, 
             class TEXT)''')

# Save (commit) the changes and close the connection
conn.commit()
conn.close()
