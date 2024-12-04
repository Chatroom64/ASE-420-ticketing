import sqlite3
conn = sqlite3.connect("data.db")
cursor = conn.cursor()
def status_edit():
    status = input("Status: ")
def priority_edit():
    priority = input("Priority: ")