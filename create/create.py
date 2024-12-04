import sqlite3
from tkinter import Tk, Button, Label, Entry, messagebox
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

def create_table():
    cursor.execute("CREATE TABLE tickets()")
    conn.commit()
def ticket_create():
    title = input("Title: ")
    body = input("Description: ")
    username = ""
    date = ""
    priority = ""
    status = "Active"
def ticket_post():
    cursor.execute()