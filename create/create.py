try:
    import tkinter as tk                # python 3
    from tkinter import ttk
    from tkinter.messagebox import showinfo
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2
#  Based off of https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter/7557028#7557028
# and https://www.pythontutorial.net/tkinter/tkraise/

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
        for F in (StartPage, CreateTicket, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
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

        # label
        self.label = ttk.Label(self, text='Create a Ticket')
        self.label.pack()

        # title label
        self.title_label = ttk.Label(self, text='Ticket Title:')
        self.title_label.pack()
        #title entry
        self.title_entry = ttk.Entry(self, textvariable=self.controller.shared_data["tickettitle"])
        self.title_entry.pack(padx=5, pady=5, fill='x', expand=False)
        self.title_entry.focus()

        #button
        self.button = ttk.Button(self, text='Create Ticket')
        self.button['command'] = self.button_clicked
        self.button.pack(fill='x',expand=True, padx=20, pady=10)

    def button_clicked(self):
        tickettitle = self.controller.shared_data["tickettitle"].get()
        showinfo(title='Information', message=f'You created a ticket! Title: {tickettitle}')


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