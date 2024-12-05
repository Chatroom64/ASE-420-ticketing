try:
    import tkinter as tk                # python 3
    from tkinter import ttk
    from tkinter.messagebox import showinfo
    from tkinter import font as tkfont  # python 3
    from db_manager import DatabaseOperation
    from user import User
    from ticket import Ticket
    from reply import Reply

except ImportError:
    import Tkinter as tk     # python 2
    from tkinter import ttk
    import tkFont as tkfont  # python 2
    from tkinter.messagebox import showinfo
#  Based off of https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter/7557028#7557028
# and https://www.pythontutorial.net/tkinter/tkraise/

db_ops = DatabaseOperation()
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.shared_data = {
            "username": tk.StringVar(),
            "tickettitle": tk.StringVar()
        }
        
        self.title('Ticket Tracker')
        self.geometry('300x500')

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, CreateTicket, PageTwo):
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
        label = ttk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = ttk.Button(self, text="Create a Ticket",
                            command=lambda: controller.show_frame("CreateTicket"))
        button2 = ttk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


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
        #title entry
        title_entry = ttk.Entry(self, textvariable=self.controller.shared_data["tickettitle"])
        title_entry.pack(padx=5, pady=5, fill='x', expand=False)
        title_entry.focus()

        # priority label
        title_label = ttk.Label(self, text='Pick a Priority:')
        title_label.pack()
        # priority radio
        selected = tk.StringVar()
        for priority in priorities:
            priority_radio = ttk.Radiobutton(self, 
                                     text=priority[0], 
                                     value=priority[1], 
                                     variable=selected)
            priority_radio.pack(fill='x', padx=5,pady=5)

        #status text field
        status_label = ttk.Label(self, text = "Status:")
        status_label.pack()

        status_entry = ttk.Entry()

        # creatorID
        
        # open_date

        # close_date

        # body text

        #create ticket button
        self.button = ttk.Button(self, text='Create Ticket')
        self.button['command'] = self.button_clicked
        self.button.pack(fill='x',expand=True, padx=20, pady=10)

        # return button
        homebutton = ttk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("HomePage"))
        homebutton.pack()

    def button_clicked(self):
        tickettitle = self.controller.shared_data["tickettitle"].get()
        showinfo(title='Information', message=f'You created a ticket! Title: {tickettitle}')
        # this would be where I would call the method to createticket in DB if I was ready for that.


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
    app = App()
    app.mainloop()
    db_ops.get_tickets_by_user(userID)