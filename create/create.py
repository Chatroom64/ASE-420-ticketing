import sqlite3
from tkinter import Tk, Button, Label, Entry, messagebox
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

def ticket_create():
    title = input("Title: ")
    body = input("Description: ")
    username = ""
    date = ""
    priority = ""
    status = "Active"

