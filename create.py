try:
    import tkinter as tk    
    import re        
    from tkinter import ttk, Text
    from tkinter.messagebox import showinfo
    from tkinter import font as tkfont  # python 3
    from db_manager import DatabaseOperation
    from user import User
    from ticket import Ticket
    from reply import Reply
except ImportError:
    import re
    import Tkinter as tk     # python 2
    from tkinter import ttk
    import tkFont as tkfont  # python 2
    from tkinter.messagebox import showinfo
#  Based off of https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter/7557028#7557028
# and https://www.pythontutorial.net/tkinter/tkraise/

db_ops = DatabaseOperation()
db_name = "data.db"
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.shared_data = {
            "loginstatus": bool,
            "selfselected":tk.StringVar(),
            "currentuser": User(),
            "tickets": [],
            "currentticket": Ticket(),
            "replies": [],
            "currentreply": Reply(),
            "username": tk.StringVar(),
            "userID": int,
            "tickettitle": tk.StringVar(),
            "ticketstatus": tk.StringVar(),
            "creatorid": tk.StringVar(),
            "open_date": tk.StringVar(),
            "close_date": tk.StringVar(),
            "body": tk.StringVar(),
        }
        
        tempTicket = Ticket()
        self.shared_data["userID"] = 1
        self.shared_data["tickets"] = tempTicket.get_tickets_by_user(self.shared_data["userID"])
        self.title('Ticket Tracker')
        self.geometry('450x600')

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, CreateTicket, PageTwo, TicketDetails):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button1 = ttk.Button(self, text="Create a Ticket",
                            command=lambda: controller.show_frame("CreateTicket"))
        button2 = ttk.Button(self, text="Go to TicketDetail",
                            command=lambda: controller.show_frame("TicketDetails"))
        button2 = ttk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()

        sep = ttk.Separator(self,orient='horizontal')
        sep.pack(fill="x")

        self.display_tickets()
        
    def display_tickets(self):
        tickets = self.controller.shared_data["tickets"]
        print(tickets)
        for ticket in tickets:
            ticket_button = ttk.Button(
                self,
                text=f"Title: {ticket.title} | Status: {ticket.status}",  # Access attributes directly
                command=lambda t=ticket: self.open_ticket_details(t)
            )
            ticket_button.pack(fill="x", padx=10, pady=5)

    def open_ticket_details(self, ticket):
        self.controller.frames["TicketDetails"].load_ticket(ticket)
        self.controller.show_frame("TicketDetails")

    def refresh_tickets(self):
        # Reload tickets from the database (or wherever they're stored)
        self.controller.shared_data["tickets"] = Ticket().get_tickets_by_user(self.controller.shared_data["userID"])
        self.display_tickets()

      
class CreateTicket(tk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        priorities = (('Critical', '1'),
                      ('Medium', '2'),
                      ('Low', '3'))

        # label
        self.label = ttk.Label(self, text='Create a Ticket')
        self.label.pack()

        # title label
        title_label = ttk.Label(self, text='Ticket Title:')
        title_label.pack()
        # title entry
        title_entry = ttk.Entry(self, textvariable=self.controller.shared_data["tickettitle"])
        title_entry.pack(padx=5, pady=5, fill='x', expand=False)
        title_entry.focus()

        # priority label
        priority_label = ttk.Label(self, text='Pick a Priority:')
        priority_label.pack()
        # Set up the selected_priority as an instance variable
        self.selected_priority = tk.StringVar()

        # priority radio buttons
        for priority in priorities:
            priority_radio = ttk.Radiobutton(self, 
                                            text=priority[0], 
                                            value=priority[1], 
                                            variable=self.selected_priority)
            priority_radio.pack(fill='x', padx=5, pady=5)

        # status text field
        status_label = ttk.Label(self, text="Status:")
        status_label.pack()

        status_entry = ttk.Entry(self, textvariable=self.controller.shared_data["ticketstatus"])
        status_entry.pack(padx=5, pady=5, fill='x', expand=False)
        status_entry.focus()

        # creatorID (disabled entry, assuming creator is logged in user)
        creator_label = ttk.Label(self, text="Creator:")
        creator_label.pack()

        creator_entry = ttk.Entry(self, text=self.controller.shared_data["currentuser"].userID)
        creator_entry.configure(state="disabled")
        creator_entry.pack(padx=5, pady=5, fill='x', expand=False)
        creator_entry.focus()

        # open_date
        opendate_label = ttk.Label(self, text="Open_Date:")
        opendate_label.pack()

        opendate_entry = ttk.Entry(self, textvariable=self.controller.shared_data["open_date"])
        opendate_entry.pack(padx=5, pady=5, fill='x', expand=False)
        opendate_entry.focus()

        # body text
        body_label = ttk.Label(self, text="Ticket Details:")
        body_label.pack()

        body_text = Text(self, height=8)
        body_text.insert('1.0', "Enter details about the problem here.")
        body_text.pack()

        # create ticket button
        self.button = ttk.Button(self, text='Create Ticket')
        self.button['command'] = self.button_clicked
        self.button.pack(fill='x', expand=True, padx=20, pady=10)

        # return button
        homebutton = ttk.Button(self, text="Go to the start page",
                                command=lambda: controller.show_frame("HomePage"))
        homebutton.pack()

    def button_clicked(self):
        # Get user inputs
        tickettitle = self.controller.shared_data["tickettitle"].get()
        ticketstatus = self.controller.shared_data["ticketstatus"].get()
        creatorid = 1
        # creatorid = self.controller.shared_data["currentuser"].userID
        opendate = self.controller.shared_data["open_date"].get()
        closedate = " "
        body_text = self.controller.shared_data["body"].get()

        # Access selected priority via instance variable
        priority = self.selected_priority.get()

        # Create the ticket object
        new_ticket = Ticket()
        new_ticket.set_most_noID(tickettitle, priority, ticketstatus, creatorid, opendate, body_text)

        # Prepare ticket tuple for DB insertion
        ticket_tuple = new_ticket.get_tuple_new()
        print(ticket_tuple)

        # Add the ticket to the database
        new_ticket_id = db_ops.add_ticket(db_name, ticket_tuple)

        # Display success message
        showinfo(title='Information', message=f'You created a ticket! Ticket ID: {new_ticket_id} Title: {tickettitle} Status: {ticketstatus}')

        # Optionally, clear the form or reset fields here
        self.controller.show_frame("HomePage")

class TicketDetails(tk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        
        # return button
        homebutton = ttk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("HomePage"))
        homebutton.pack()

        self.ticket_label = ttk.Label(self, text="Ticket Details", font=controller.title_font)
        self.ticket_label.pack(side="top", fill="x", pady=10)

        self.details = tk.StringVar()
        self.ticket_details = ttk.Label(self, textvariable=self.details)
        self.ticket_details.pack()

    def load_ticket(self, ticket):
        self.details.set(f"Title: {ticket.title}\nStatus: {ticket.status}\nDetails: {ticket.body}")

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    ticket = Ticket()
    app = App()
    app.mainloop()