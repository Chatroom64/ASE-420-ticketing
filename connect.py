import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        # Initialize the database connection.
        self.db_name = db_name
        self.connection = None

    def connect(self):
        # Establish a connection to the database.
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def close(self):
        # Close the database connection.
        if self.connection:
            self.connection.close()
            self.connection = None
