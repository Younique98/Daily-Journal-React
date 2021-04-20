import sqlite3
import json
from models import Mood
def get_all_moods():
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
            m.id,
            m.label  
        FROM Moods m
               """)

        # Initialize an empty list to hold all mood representations
        moods = []

        # Convert rows of data into a Python list
        ## dataset pretty much fetche al lthat was executed at line 65
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an mood instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # mood class above.
            ## This makes a new mood instance and we're calling it the properties on the class in the modal folder mood.py

# Create a Mood Instance from the current row
            mood = Mood(row['id'], row['label'])


    # Add the dictionary representation of the mood to the list
            moods.append(mood.__dict__)
    
    # Use `json` package to properly serialize list as JSON
    # changes from a dict to a jsonString
    return json.dumps(moods)

def get_single_mood(id):
    with sqlite3.connect("./journal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            m.id,
            m.label
        FROM Moods m

        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an mood instance from the current row
        # turning into a class object
        mood = Mood(data['id'], data['label'])
## dumps turns it back into a string from an dictionary
# read right to left from mood.dict to the dumps then to json
        return json.dumps(mood.__dict__)