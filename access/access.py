import sqlite3
conn = sqlite3.connect("data.db")
cursor = conn.cursor()
# creates the table that stores credentials
def create_table():
    cursor.execute("CREATE TABLE signin(usernames VARCHAR, passwords VARCHAR)")
    conn.commit()
def add_user():
    username = input("Create username: ")
    password = input("Create password: ")
    role = "client"
    cursor.execute("INSERT INTO signin (usernames, passwords) VALUES (?, ?)", (username, password,))
    conn.commit()
def auth_user():
    username = input("Username: ")
    password = input("Password: ")
    isUsername = username == usernames
    isPassword = password == passwords
    # create signup page
def signup_page():
    try:
        with sqlite3.connect("data.db") as conn:
            add_user()
            print(f'Account created for {username}')
    except sqlite3.Error as e:
        print(e)
    finally:
        print('Welcome, {username}!')
signup_page()
# Create the signin page
def signin_page():
    try:
        with sqlite3.connect("data.db") as conn:
            add_user()
            print(f'Account created')
    except sqlite3.Error as e:
        print(e)
    finally:
        print('Welcome back, {username}!')