from connect import DatabaseConnection
import sqlite3
class DatabaseOperation:
    def execute_db_query(self, db_name:str, sql:str, params:tuple) -> int:
        try:
            # Initialize the database connection.
            db_conn = DatabaseConnection(db_name)
            with db_conn.connect() as connection:
                cursor = connection.cursor()               
                # execute the command
                try:
                    cursor.execute(sql, params)
                    connection.commit()
                    lastid = cursor.lastrowid
                except sqlite3.Error as e:
                    print(e)
                return lastid
        except sqlite3.Error as e:
            print(e)
    def execute_db_update(self, db_name:str, sql:str, object:tuple) -> int:
        try:
            # Initialize the database connection.
            db_conn = DatabaseConnection(db_name)
            connection = db_conn.connect()
            cursor = connection.cursor()
            
            recordID = object.ID

            # execute the command
            cursor.execute(sql, object, recordID)
            connection.commit()
            rowcount = cursor.rowcount
            return rowcount
        except sqlite3.Error as e:
            print(e)

    # adding to the database
    def add_user(self,db_name:str,user:tuple) -> int:
        sql = ''' INSERT INTO users(name, role, email, password)
        VALUES(?,?,?,?)'''
        # get id for confirmation
        lastid = self.execute_db_query(db_name,sql,user)
        # return the last id
        return lastid
    def add_ticket(self,db_name:str,ticket:tuple) -> int:
        sql = ''' INSERT INTO tickets(title, priority, status, creator_id, open_date, close_date, body)
        VALUES(?, ?, ?, ?, ?, ?, ?)'''
        # get id for confirmation
        lastid = self.execute_db_query(db_name,sql,ticket)
        # return the last id
        return lastid
    def add_reply(self,db_name:str,reply:tuple) -> int:
        sql = ''' INSERT INTO replies(creator_id, post_date, body, ticket_id)
        VALUES(?, ?, ?, ?)'''
        # get id for confirmation
        lastid = self.execute_db_query(db_name,sql,reply)
        # return the last id
        return lastid   
    def add_signin(self,db_name:str,login:tuple) -> int:
        sql = ''' INSERT INTO signin(username, password)
        VALUES(?,?)'''
        # get id for confirmation
        lastid = self.execute_db_query(db_name,sql,login)
        return lastid

    # UPDATE items in database
    def update_user(self,db_name:str,user:tuple,userID) -> int:
        sql = '''UPDATE users 
        SET name=?, role=?, email=?, password=? 
        WHERE id = ? '''
        rowcount = self.execute_db_update(db_name,sql,user,userID)
        return rowcount
    def update_ticket(self,db_name:str,ticket:tuple,ticketID):
        sql = '''UPDATE tickets 
        SET title=?, priority=?, status=?, creator_id=?, open_date=?, 
        close_date=?, body=? WHERE id=?'''
        rowcount = self.execute_db_update(db_name,sql,ticket,ticketID)
        return rowcount
    def update_reply(self,db_name:str,reply:tuple,replyID):
        sql = '''UPDATE replies SET body=? WHERE id=?'''
        rowcount = self.execute_db_update(db_name,sql,reply,replyID)
        return rowcount

    # DELETE items in database
    def delete_user(self,db_name:str,userID):
        sql = 'DELETE FROM users WHERE id = ?'
        try:
            with sqlite3.connect(db_name) as conn:
                cur = conn.cursor()
                cur.execute(sql,(userID))
                conn.commit()
        except sqlite3.OperationalError as e:
            print(e)
    # delete ticket
    def delete_ticket(self,db_name:str,ticketID):
        sql = 'DELETE FROM tickets WHERE id = ?'
        try:
            with sqlite3.connect(db_name) as conn:
                cur = conn.cursor()
                cur.execute(sql,(ticketID))
                conn.commit()
        except sqlite3.OperationalError as e:
            print(e)
    # delete reply
    def delete_reply(self,db_name:str,replyID):
        sql = 'DELETE FROM tickets WHERE id = ?'
        try:
            with sqlite3.connect(db_name) as conn:
                cur = conn.cursor()
                cur.execute(sql,(replyID))
                conn.commit()
        except sqlite3.OperationalError as e:
            print(e)
        
    # GET from databse
    # get single user by id
    def get_user_by_id(self,db_name:str,creator_id):
        sql = '''SELECT * FROM users WHERE id = ?'''
        try:
            with sqlite3.connect(db_name) as conn:
                cur = conn.cursor()
                cur.execute(sql, (creator_id,))
                reply = cur.fetchone()
                return reply  # Return the user as a tuple
        except sqlite3.Error as e:
            print(f"Error fetching reply by ID: {e}")
            return reply
    # get single user by email
    def get_user_by_email(self,db_name:str,email:str):
        sql = '''SELECT * FROM users WHERE email = ?'''
        try:
            with sqlite3.connect(db_name) as conn:
                cur = conn.cursor()
                cur.execute(sql, email)
                reply = cur.fetchone()
                return reply  # Return the user as a tuple
        except sqlite3.Error as e:
            print(f"Error fetching users by Email: {e}")
    # get single ticket by id
    def get_ticket_by_id(self,db_name:str,ticket_id):
        sql = '''SELECT * FROM tickets WHERE id = ?'''
        try:
            with sqlite3.connect(db_name) as conn:
                cur = conn.cursor()
                cur.execute(sql, (ticket_id,))
                reply = cur.fetchone()
                return reply  # Return the ticket as a tuple
        except sqlite3.Error as e:
            print(f"Error fetching reply by ID: {e}")
            return None
    # get all replies for a user
    def get_tickets_by_user(self,db_name:str,creator_id:int):
        sql = '''SELECT * FROM tickets WHERE creator_id = ? ORDER BY open_date'''
        try:
            with sqlite3.connect(db_name) as conn:
                cur = conn.cursor()
                cur.execute(sql, (creator_id,))
                replies = cur.fetchall()
                return replies  # Return a list of tickets
        except sqlite3.Error as e:
            print("Error fetching tickets by user ID:")
            print(e)
    # get single reply by id
    def get_reply_by_id(self,db_name:str,reply_id):
        sql = '''SELECT * FROM replies WHERE id = ?'''
        try:
            with sqlite3.connect(db_name) as conn:
                cur = conn.cursor()
                cur.execute(sql, (reply_id,))
                reply = cur.fetchone()
                return reply  # Return the reply as a tuple
        except sqlite3.Error as e:
            print(f"Error fetching reply by ID: {e}")
            return None
    # get all replies for a ticket
    def get_replies_by_ticket_id(self,db_name:str,ticket_id):
        sql = '''SELECT * FROM replies WHERE ticket_id = ? ORDER BY post_date'''
        try:
            with sqlite3.connect(db_name) as conn:
                cur = conn.cursor()
                cur.execute(sql, (ticket_id,))
                replies = cur.fetchall()
                return replies  # Return a list of replies
        except sqlite3.Error as e:
            print(f"Error fetching replies by ticket ID: {e}")
            return None
        
#########################

"""
sql = '''SELECT * FROM users'''
try:
    with sqlite3.connect("data.db") as conn:
        cur = conn.cursor()
        cur.execute(sql)
        response = cur.fetchall()
        print(response)
except sqlite3.Error as e:
    print(f"Error fetching users: {e}")
print("User Exists Test")
"""

"""sql = '''SELECT * FROM users WHERE email = ?'''
try:
    with sqlite3.connect("data.db") as conn:
        cur = conn.cursor()
        cur.execute(sql, ("frank@mail.com",))
        reply = cur.fetchone()
        print(type(reply))
        print(reply)
except sqlite3.Error as e:
    print(f"Error fetching users by Email: {e}")"""


"""
sql = '''SELECT * FROM tickets'''
try:
    with sqlite3.connect("data.db") as conn:
        cur = conn.cursor()
        cur.execute(sql)
        response1 = cur.fetchall()
        print(response1)
except sqlite3.Error as e:
    print(f"Error fetching tickets: {e}")
print("tickets exist test")
"""


"""
sql = '''SELECT * FROM replies'''
try:
    with sqlite3.connect("data.db") as conn:
        cur = conn.cursor()
        cur.execute(sql)
        response2 = cur.fetchall()
        print(response2)
except sqlite3.Error as e:
    print(f"Error fetching replies: {e}")"""

########################### 