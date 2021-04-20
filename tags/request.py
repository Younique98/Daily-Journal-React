import sqlite3
import json
from models import Tag


def get_all_tags():
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
            t.id,
            t.name 
        FROM Tag t
               """)

        # Initialize an empty list to hold all tag representations
        tags = []

        # Convert rows of data into a Python list
        ## dataset pretty much fetche al lthat was executed at line 65
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an tag instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # tag class above.
            ## This makes a new tag instance and we're calling it the properties on the class in the modal folder tag.py

# Create a tag Instance from the current row
            tag = Tag(row['id'], row['name'])


    # Add the dictionary representation of the tag to the list
            tags.append(tag.__dict__)
    
    # Use `json` package to properly serialize list as JSON
    # changes from a dict to a jsonString
    return json.dumps(tags)

def get_single_tag(id):
    with sqlite3.connect("./journal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            t.id,
            t.name
        FROM Tag t
        WHERE t.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an tag instance from the current row
        # turning into a class object
        tag = Tag(data['id'], data['name'])
## dumps turns it back into a string from an dictionary
# read right to left from tag.dict to the dumps then to json
        return json.dumps(tag.__dict__)