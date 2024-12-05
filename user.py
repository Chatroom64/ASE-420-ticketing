from db_manager import DatabaseOperation
db_name = 'data.db'
db_ops = DatabaseOperation()

class User(object):
    def __init__(self):
        self.userID = ""
        self.name = ""
        self.role = ""
        self.email = ""
        self.password = ""
        self.userTuple = ("",)
    def __str__(self):
        # allows print(user) to return the values of the user object
        return (f"User ID: {self.userID}, Name: {self.name}, "
            f"Role: {self.role}, Email: {self.email}")

    def set_all(self, userID:int, userName:str, userRole:str, 
                userEmail:str, userPassword:str):
        self.userID = userID
        self.name = userName
        self.role = userRole
        self.email = userEmail
        self.password = userPassword
    def set_most_noID(self, userName:str, userRole:str, userEmail:str, userPassword:str):
        self.name = userName
        self.role = userRole
        self.email = userEmail
        self.password = userPassword
    def get_id(self) -> str:
        return self.userID
    def fetch_user_by_email(self,db_name:str, userEmail:str):
        email = (userEmail, )
        response = db_ops.get_user_by_email(db_name,email)
        
        if response:  # Ensure response is not None
            self.userID = response[0]
            self.name = response[1]
            self.role = response[2]
            self.email = response[3]
            self.password = response[4]
            return self
        else:
            raise ValueError(f"No user found with email: {userEmail}")
    def get_name(self) -> str:
        return self.name
    def get_tuple_new(self) -> tuple:
        userTuple = (self.name,)
        userTuple += (self.role, )
        userTuple += (self.email, )
        userTuple += (self.password, )
        return userTuple
    def get_tuple(self) -> tuple:
        userTuple = (str(self.userID), )
        userTuple += (self.name,)
        userTuple += (self.role, )
        userTuple += (self.email, )
        userTuple += (self.password, )
        return userTuple
    def get_from_DB(self, userID):
        response = db_ops.get_user_by_id(db_name,userID)
        print(response)

# Class Demo/Testing
'''newUser = User()
newUser = newUser.fetch_user_by_email(db_name,"frank@mail.com")
print(type(newUser))
print(newUser)
'''
'''newUser = User()
print(type(newUser))
newUser.set_all(" ","Frank","Client","frank@mail.com","Test1")
newUserTuple = newUser.get_tuple_new()
print(newUserTuple)
print(type(newUserTuple))
newUserID = db_ops.add_user(db_name,newUserTuple) 

print(newUserID)
'''
'''newID = db_ops.add_user(db_name, newUserTuple)
user1 = user.getFromDB(newID)'''
