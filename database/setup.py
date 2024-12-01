import sqlite3

sql_statements = [ 
    """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY, 
            name text NOT NULL, 
            role INT NOT NULL, 
            email text NOT NULL,
            password text NOT NULL
        );""",

    """CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY, 
            title TEXT NOT NULL, 
            priority INT, 
            status text,
            creator_id INT NOT NULL, 
            open_date DATE NOT NULL, 
            close_date DATE, 
            body text NOT NULL,
            FOREIGN KEY (creator_id) REFERENCES users (id)
        );""",

    """CREATE TABLE IF NOT EXISTS reply (
            id INTEGER PRIMARY KEY,
            creator_id INT NOT NULL, 
            post_date DATE NOT NULL, 
            body text NOT NULL,
            ticket_id INT NOT NULL,
            FOREIGN KEY (creator_id) REFERENCES users (id),
            FOREIGN KEY (ticket_id) REFERENCES tickets (id)
        );""",

]

# create a database connection
try:
    with sqlite3.connect('data.db') as conn:
        # create a cursor
        cursor = conn.cursor()

        # execute statements
        for statement in sql_statements:
            cursor.execute(statement)

        # commit the changes
        conn.commit()

        print("Tables created successfully.")
except sqlite3.OperationalError as e:
    print("Failed to create tables:", e)
