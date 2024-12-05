from db_manager import DatabaseOperation
db_name = 'data.db'
db_ops = DatabaseOperation()

class Ticket(object):
    def __init__(self):
        self.ticketID = ""
        self.title = ""
        self.priority = ""
        self.status = ""
        self.creator_id = ""
        self.open_date = ""
        self.close_date = ""
        self.body = ""
        self.ticketTuple = ("",)
        
    def __str__(self):
        return (f"Ticket ID: {self.ticketID}, Title: {self.title}, "
            f"Priority: {self.priority}, Status: {self.status}, "
            f"Creator ID: {self.creator_id}, Open Date: {self.open_date}, "
            f"Close Date: {self.close_date}, Body: {self.body}")

    def set_all(self, ticketID:int, title:str, priority:str, status:str, creator_id:int,
                open_date:str, close_date:str, body:str):
        self.ticketID = ticketID
        self.title = title
        self.priority = priority
        self.status = status
        self.creator_id = creator_id
        self.open_date = open_date
        self.close_date = close_date
        self.body = body
    def set_all_tuple(self, ticket):
        self.ticketID = ticket[0]
        self.title = ticket[1]
        self.priority = ticket[2]
        self.status = ticket[3]
        self.creator_id = ticket[4]
        self.open_date = ticket[5]
        self.close_date = ticket[6]
        self.body = ticket[7]
    def set_most_noclose(self, ticketID:int, title:str, priority:str, status:str, creator_id:int,
                open_date:str, body:str):
        self.ticketID = ticketID
        self.title = title
        self.priority = priority
        self.status = status
        self.creator_id = creator_id
        self.open_date = open_date
        self.body = body
    def set_most_noID(self, title:str, priority:str, status:str, creator_id:int,
                open_date:str, body:str):
        self.title = title
        self.priority = str(priority)
        self.status = str(status)
        self.creator_id = str(creator_id)
        self.open_date = str(open_date)
        self.body = body
    def get_id(self) -> str:
        return self.ticketID
    def get_title(self) -> str:
        return self.title
    def get_ticket_by_id(self,ticketID):
        response = db_ops.get_ticket_by_id(ticketID)
        self.id = response[0]
        self.title = response[1]
        self.priority = response[2]
        self.status = response[3]
        self.creator_id = response[4]
        self.open_date = response[5]
        self.body = response[6]
        return self
    def get_tickets_by_user(self,userID):
        try:
            responses = db_ops.get_tickets_by_user(db_name,userID)
            tickets = []
            for response in responses:
                newTicket = Ticket()
                newTicket.set_all_tuple(response)
                tickets.append(newTicket)
            return tickets
        except TypeError as e:
            print(e)
    def get_name(self) -> str:
        return self.name
    def get_tuple_new(self) -> tuple:
        ticketTuple = (self.title,)
        ticketTuple += (self.priority, )
        ticketTuple += (self.status, )
        ticketTuple += (self.creator_id, )
        ticketTuple += (self.open_date, )
        ticketTuple +=(self.close_date, )
        ticketTuple += (self.body, )
        return ticketTuple
    def get_tuple(self) -> tuple:
        ticketTuple = (str(self.ticketID), )
        ticketTuple += (self.title,)
        ticketTuple += (self.priority, )
        ticketTuple += (self.status, )
        ticketTuple += (str(self.creator_id), )
        ticketTuple += (str(self.open_date), )
        ticketTuple += (str(self.close_date), )
        ticketTuple += (str(self.body), )
        return ticketTuple
    def get_from_DB(self, ticketID):
        response = db_ops.get_ticket_by_id(db_name,ticketID)
        print(response)

# Class Demo/Testing
newTicket = Ticket()
newTicket.set_most_noID("Blue","2","2",1,"06/10/2025","Hello?")
newTicketTuple = newTicket.get_tuple_new()
print(newTicketTuple)
print(type(newTicketTuple))
newTicketID = db_ops.add_ticket(db_name,newTicketTuple) 
print(newTicketID)

'''ticketsFromFrank = []
newTickets = Ticket()

ticketsFromFrank = newTickets.get_tickets_by_user(1)

for ticket in ticketsFromFrank:
    print(ticket)'''
