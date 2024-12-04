import sqlite3
from db_manager import DatabaseOperation
db_name = 'data.db'
db_ops = DatabaseOperation()

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

def auth_user():
    input_username = input("Username: ")
    input_password = input("Password: ")
    isUsername = input_username == username
    isPassword = input_password == password
    # create signup page
    
def signup_page(username: str, password: str):
    newUser = tuple(username,)
    newUser += tuple(password,)
    newID = db_ops.add_signin(db_name,newUser)
    print(newID)

# runtime code    
username = input("Username: ")
password = input("Password: ")
signup_page(username, password)