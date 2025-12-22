import sqlite3

conn = sqlite3.connect("home.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS appliance_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    appliance_name TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Database and table created successfully")