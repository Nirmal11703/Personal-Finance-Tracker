import sqlite3
from tabulate import tabulate
import os

# === Set your database path here ===
db_path = 'finance_tracker.db'

# Print the path to make sure it's correct
print("Using DB file at:", os.path.abspath(db_path))

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Fetch all tables and views
cursor.execute("SELECT name, type FROM sqlite_master WHERE type IN ('table', 'view');")
tables = cursor.fetchall()

if not tables:
    print("\nNo tables or views found in the database.")
else:
    print(f"\nFound {len(tables)} table(s)/view(s) in '{db_path}'")

    for table in tables:
        table_name, table_type = table
        print(f"\n=== {table_type.upper()}: {table_name} ===")

        cursor.execute(f"PRAGMA table_info('{table_name}');")
        columns = cursor.fetchall()

        headers = ["CID", "Column Name", "Data Type", "Not Null", "Default Value", "Primary Key"]
        print(tabulate(columns, headers=headers, tablefmt="fancy_grid"))

conn.close()
print("\nDone!")
