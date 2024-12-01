from connect import DatabaseConnection
import sqlite3

class DatabaseOperation:
    def execute_db_query(db_name, sql, *params):
        try:
            # Initialize the database connection.
            db_conn = DatabaseConnection(db_name)
            connection = db_conn.connect()
            cursor = connection.cursor()
            
            # execute the command
            cursor.execute(sql, *params)
            connection.commit()
            lastid = cursor.lastrowid
            # close the connection
            connection.close()
            return lastid
        except sqlite3.Error as e:
            print(e)
    def execute_db_update(db_name, sql, object):
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
            # close the connection
            connection.close()
            return rowcount
        except sqlite3.Error as e:
            print(e)

    # adding to the database
    def add_user(db_name,user):
        sql = ''' INSERT INTO users(name, role, email, password)
        VALUES(?,?,?,?)'''
        # get id for confirmation
        lastid = self.execute_db_query(db_name,sql,user)
        # return the last id
        return lastid
    def add_ticket(db_name,ticket):
        sql = ''' INSERT INTO tickets(title, priority, status, creator_id, open_date, close_date, body)
        VALUES(?, ?, ?, ?, ?, ?, ?)'''
        # get id for confirmation
        lastid = self.execute_db_query(db_name,sql,ticket)
        # return the last id
        return lastid
    def add_reply(db_name,reply):
        sql = ''' INSERT INTO replies(creator_id, post_date, body, ticket_id)
        VALUES(?, ?, ?, ?)'''
        # get id for confirmation
        lastid = self.execute_db_query(db_name,sql,reply)
        # return the last id
        return lastid   

    # UPDATE items in database
    def update_user(db_name,user,userID):
        sql = '''UPDATE users 
        SET name=?, role=?, email=?, password=? 
        WHERE id = ? '''
        rowcount = self.execute_db_update(db_name,sql,user,userID)
        return rowcount
    def update_ticket(db_name,ticket,ticketID):
        sql = '''UPDATE tickets 
        SET title=?, priority=?, status=?, creator_id=?, open_date=?, 
        close_date=?, body=? WHERE id=?'''
        rowcount = self.execute_db_update(db_name,sql,ticket,ticketID)
        return rowcount
    def update_reply(db_name,reply,replyID):
        sql = '''UPDATE replies SET body=? WHERE id=?'''
        rowcount = self.execute_db_update(db_name,sql,reply,replyID)
        return rowcount

    # DELETE items in database
    def delete_user(db_name,userID):
        sql = 'DELETE FROM users WHERE id = ?'
        try:
            with sqlite3.connect(db_name) as conn:
                cur = conn.cursor()
                cur.execute(sql,(userID))
                conn.commit()
        except sqlite3.OperationalError as e:
            print(e)
    # delete ticket
    def delete_ticket(db_name,ticketID):
        sql = 'DELETE FROM tickets WHERE id = ?'
        try:
            with sqlite3.connect(db_name) as conn:
                cur = conn.cursor()
                cur.execute(sql,(ticketID))
                conn.commit()
        except sqlite3.OperationalError as e:
            print(e)
    # delete reply
    def delete_reply(db_name,replyID):
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
    def get_reply_by_id(self, db_name, user_id):
        sql = '''SELECT * FROM users WHERE id = ?'''
        try:
            with sqlite3.connect(db_name) as conn:
                cur = conn.cursor()
                cur.execute(sql, (user_id,))
                reply = cur.fetchone()
                return reply  # Return the user as a tuple
        except sqlite3.Error as e:
            print(f"Error fetching reply by ID: {e}")
            return None
    # get single ticket by id
    def get_ticket_by_id(self, db_name, ticket_id):
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
    def get_tickets_by_user(self, db_name, user_id):
        sql = '''SELECT * FROM tickets WHERE user_id = ? ORDER BY post_date'''
        try:
            with sqlite3.connect(db_name) as conn:
                cur = conn.cursor()
                cur.execute(sql, (user_id,))
                replies = cur.fetchall()
                return replies  # Return a list of tickets
        except sqlite3.Error as e:
            print(f"Error fetching replies by ticket ID: {e}")
            return None
    # get single reply by id
    def get_reply_by_id(self, db_name, reply_id):
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
    def get_replies_by_ticket_id(self, db_name, ticket_id):
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