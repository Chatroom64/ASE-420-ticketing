from db_manager import DatabaseOperation
db_name = 'data.db'
db_ops = DatabaseOperation()

class Reply(object):
    def __init__(self):
        self.replyID = ""
        self.creator_id = ""
        self.post_date = ""
        self.body = ""
        self.ticket_ = ""
        self.replyTuple = ("",)
        
    def __str__(self):
        return (f"reply ID: {self.replyID}, Creator ID: {self.creator_id}, "
            f"post_date: {self.post_date}, , Body: {self.body}"
            f"Ticket ID: {self.ticket_id}")

    def set_all(self, replyID:int, creator_id:int, post_date:str, 
                         body:str, ticket_id:str):
        self.replyID = replyID
        self.creator_id = creator_id
        self.post_date = post_date
        self.body = body
        self.ticket_id = ticket_id
    def set_all_tuple(self, reply):
        self.replyID = reply[0]
        self.creator_id = reply[1]
        self.post_date = reply[2]
        self.body = reply[3]
        self.ticket_id = reply[4]
    def set_most_noclose(self, replyID:int, creator_id:int, post_date:str, 
                         body:str, ticket_id:str):
        self.replyID = replyID
        self.creator_id = creator_id
        self.post_date = post_date
        self.body = body
        self.ticket_id = ticket_id
    def set_most_noID(self, creator_id:int, post_date:str, 
                         body:str, ticket_id:str):
        self.creator_id = creator_id
        self.post_date = post_date
        self.body = body
        self.ticket_id = ticket_id
 
    def get_id(self) -> str:
        return self.replyID
    def get_title(self) -> str:
        return self.title
    def get_reply_by_id(self,replyID):
        reply = db_ops.get_reply_by_id(replyID)
        self.replyID = reply[0]
        self.creator_id = reply[1]
        self.post_date = reply[2]
        self.body = reply[3]
        self.ticket_id = reply[4]
        return self
    def get_replies_by_ticket(self,ticketID):
        try:
            responses = db_ops.get_replies_by_ticket_id(db_name,ticketID)
            replys = []
            for response in responses:
                newReply = Reply()
                newReply.set_all_tuple(response)
                replys.append(newReply)
            return replys
        except TypeError as e:
            print(e)
    def get_name(self) -> str:
        return self.name
    def get_tuple_new(self) -> tuple:
        replyTuple = (self.creator_id,)
        replyTuple += (self.post_date, )
        replyTuple += (self.body, )
        replyTuple += (self.ticket_id, )
        return replyTuple
    def get_tuple(self) -> tuple:
        replyTuple = (str(self.replyID), )
        replyTuple += (str(self.creator_id),)
        replyTuple += (self.post_date, )
        replyTuple += (self.body, )
        replyTuple += (self.ticket, )
        return replyTuple
    def get_from_DB(self, replyID):
        response = db_ops.get_reply_by_id(db_name,replyID)
        print(response)


# Class Demo/Testing
'''print("adding a new reply")
newReply = Reply()
newReply.set_most_noID(1,"02/10/2025","So as per our last email...",1)
newReplyTuple = newReply.get_tuple_new()
print(newReplyTuple)
print(type(newReplyTuple))
newReplyID = db_ops.add_reply(db_name,newReplyTuple) 
print(newReplyID)'''


'''newReplyA = Reply()
newReplyA.set_most_noID(1,"03/10/2025","Hello World",1)
newReplyATuple = newReplyA.get_tuple_new()
print(newReplyATuple)
print(type(newReplyATuple))
newReplyAID = db_ops.add_reply(db_name,newReplyATuple) 
print(newReplyAID)'''

# getting multiple replies test
'''repliesFromFrank = []
newReplies = Reply()

repliesFromFrank = newReplies.get_replies_by_ticket(1)

for reply in repliesFromFrank:
    print(reply)'''