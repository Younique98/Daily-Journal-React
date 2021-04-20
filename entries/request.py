import sqlite3
import json
from models import Entry
from models import Mood
from models import Tag


# Function with a single parameter

def create_entry(new_entry):
    with sqlite3.connect("./journal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO JournalEntries
            ( date, concept, entry, moodId )
        VALUES
            ( ?, ?, ?, ?);
        """, (new_entry['date'], new_entry['concept'],
              new_entry['entry'], new_entry['moodId']))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the entry dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_entry['id'] = id


    return json.dumps(new_entry)

def delete_entry(id):
    with sqlite3.connect("./journal.db") as conn:
        db_cursor = conn.cursor()
# triple quotes is a string you can add new lines too
#example >>> print("this is a string")
    # this is a string
    # >>> print("""this is a string
    # ... his is a hot""")
    # this is a string
    # this is a hot
        db_cursor.execute("""
        DELETE FROM JournalEntries
        WHERE id = ?
        """, (id, ))

    # Iterate the entryS list, but use enumerate() so that you
    # can access the index value of each item
    

def update_entry(id, new_entry):
    with sqlite3.connect("./journal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE JournalEntries
            SET
                date = ?,
                concept = ?,
                entry = ?,
                moodId = ?
        WHERE id = ?
        """, (new_entry['date'], new_entry['concept'],
              new_entry['entry'], new_entry['moodId'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./journal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        #variable the database con.cursor() lets us talk to the database
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        #dbcursor tells it what sql command to execute in this case its SELECT
        db_cursor.execute("""
        SELECT
            j.id,
            j.date,
            j.concept,
            j.entry,
            j.moodId,
            m.label mood_label,
            t.name    
        FROM JournalEntries j
        JOIN Moods m
            ON m.id = j.moodId
        JOIN Entry_Tag e
            ON e.entry_id = j.id
        JOIN Tag t
            ON t.id = e.tag_id
               """)

        # Initialize an empty list to hold all entry representations
        entries = []

        # Convert rows of data into a Python list
        ## dataset pretty much fetche al lthat was executed at line 65
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entry instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # entry class above.
            ## This makes a new entry instance and we're calling it the properties on the class in the modal folder entry.py
            entry = Entry(row['id'], row['date'], row['concept'], row['entry'],
                    row['moodId'])

# Create a Mood Instance from the current row
            mood = Mood(row['id'], row['mood_label'])

# tag instance creation
            tag = Tag(row['id'], row['name'])

# turn tag to a dictionary 
            entry.tag = tag.__dict__
    # Add the dictionary representation of the entries to the mood to the list
            entry.mood = mood.__dict__

    # Add the dictionary representation of the entry to the list
            entries.append(entry.__dict__)
    
    # Use `json` package to properly serialize list as JSON
    # changes from a dict to a jsonString
    return json.dumps(entries)

def get_single_entry(id):
    with sqlite3.connect("./journal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.concept,
            e.entry,
            e.moodId
        FROM JournalEntries e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an entry instance from the current row
        # turning into a class object
        entry = Entry(data['id'], data['date'], data['concept'],
                            data['entry'], data['moodId'])
## dumps turns it back into a string from an dictionary
# read right to left from entry.dict to the dumps then to json
        return json.dumps(entry.__dict__)