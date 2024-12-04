import sqlite3
from db_manager import DatabaseOperation
db_name = 'data.db'
db_ops = DatabaseOperation()

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

def auth_user():
    username = input("Username: ")
    password = input("Password: ")
    isUsername = username == usernames
    isPassword = password == passwords
    # create signup page
    
def signup_page(username: str, password: str):
    newUser = tuple(username,)
    newUser += tuple(password,)
    newID = db_ops.add_signin(db_name,newUser)
    print(newID)
username = input("Username: ")
password = input("Password: ")
signup_page(username, password)

# Create the signin page
def signin_page():
    try:
        with sqlite3.connect("data.db") as conn:
            add_user()
            print(f'Signed in')
    except sqlite3.Error as e:
        print(e)
    finally:
        print('Welcome back, {username}!')