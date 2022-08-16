from tinydb import TinyDB, Query
from tinydb.operations import set


# Instance of database querier.
User = Query()
# database creation.
database = TinyDB('Database/database.json')



class UserTable():
    """
    Class for operating on Database (UserTable).
    """

    def __init__(self , user_name:str, password:str, email:str = 'nil'):

        # Parameters for users.
        self.user_name = user_name
        self.email = email
        self.password = password
        # Addition of Users table to database
        self.users_table = database.table("Users")


    # function to enter new user.
    def insert_user(self) -> None:
        """
        Function inputs new user to the User database table
        """
        self.users_table.insert(
            {
                'user_name' : self.user_name,
                'email' : self.email,
                'password' : self.password,
            }
        )


    # Function to check if a user already exists in the database.
    def user_exists(self) -> bool:
        """
        Function checks for the existence of a user in the database

        Input:
         user_name : String

        Return:
         Boolean value
        """
        if self.users_table.search(User.user_name == self.user_name):
            return True
        else:
            return False


    # Function to delete user
    def delete_user(self) -> None:
        """
        Function deletes user from database with user_name provided

        Input:
        user_name : String 
        """
        self.users_table.remove(User.user_name == self.user_name)


    # Function to get user ID
    def get_id(self) -> int:
        """
        Function gets user ID from database with user_name provided

        Input:
        user_name : String 
        """
        id = (self.users_table.get(User.user_name == self.user_name).doc_id)
        return int(id)



class ContactTable():
    """
    Class for operating on Database (ContactTable).
    """

    def __init__(self, first_name:str, last_name:str, number:str, user_id:int, category:str = 'nil', email:str = 'nil'):

        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.category = category
        self.user_id = user_id
        self.email = email
        # Genetating database table name
        table_name = 'user_'+str(self.user_id) #########################################
        # User's contact database creation
        self.users_contact_table = database.table(table_name)

    
    def insert_contact(self):
        """
        Function to insert new contact into the database (Contact table).

        Input:
         self: first_name : str
         self: last_name : str
         self: number : str
         self: category : str
         self: email : str

        """
        self.users_contact_table.insert(
            {
                'user_id' : self.user_id,
                'first_name' : self.first_name,
                'last_name' : self.last_name,
                'number' : self.number,
                'category' : self.category,
                'email' : self.email,
            }
        )

    
    def delete_contact(self):
        """
        Function deletes a contact from a specified users account in the database (..contact_table) with contact first_name, last_name, number and user_id provided

        Input:
         self : user_id
         self : first_name
         self : last_name
         self : number

        Return:
         nothing 
        """
        self.users_contact_table.remove((User.first_name == self.first_name) & (User.last_name == self.last_name) & (User.number == self.number) & (User.user_id == self.user_id))


    def update_first_name(self, new_first_name:str):
        """
        Function updates a contact first_name for a specified contact for a specified users account in the database (..contact_table) that matchs the provided contact first_name, last_name, number and user_id provided

        Input:
         self : user_id
         self : first_name
         self : last_name
         self : number
         new_name : New First-Name Entery / Former First-Name Replacement

        Return:
         nothing 
        """
        # self.users_contact_table.update(set('first_name', new_first_name), (User.first_name == self.first_name))
        self.users_contact_table.update(set('first_name', new_first_name)), ((User.first_name == self.first_name) & (User.last_name == self.last_name) & (User.number == self.number) & (User.user_id == self.user_id))
    

    def update_last_name(self, new_last_name:str):
        """
        Function updates a contact last_name for a specified contact for a specified users account in the database (..contact_table) that matchs the provided contact first_name, last_name, number and user_id provided

        Input:
         self : user_id
         self : first_name
         self : last_name
         self : number
         new_name : New Last-Name Entery / Former Last-Name Replacement

        Return:
         nothing 
        """
        self.users_contact_table.update(set('last_name', new_last_name), ((User.first_name == self.first_name) & (User.last_name == self.last_name) & (User.number == self.number) & (User.user_id == self.user_id)))
    

    def update_number(self, new_number:str):
        """
        Function updates a contact number for a specified contact for a specified users account in the database (..contact_table) that matchs the provided contact first_name, last_name, number and user_id provided

        Input:
         self : user_id
         self : first_name
         self : last_name
         self : number
         new_name : New Number / Former Number Replacement

        Return:
         nothing 
        """
        self.users_contact_table.update(set('number', new_number), ((User.first_name == self.first_name) & (User.last_name == self.last_name) & (User.number == self.number) & (User.user_id == self.user_id)))


    def update_category(self, new_category:str):
        """
        Function updates a contact category for a specified contact for a specified users account in the database (..contact_table) that matchs the provided contact first_name, last_name, number and user_id provided

        Input:
         self : user_id
         self : first_name
         self : last_name
         self : number
         new_category : New Category / Former Category Replacement

        Return:
         nothing 
        """
        self.users_contact_table.update(set('category', new_category), ((User.first_name == self.first_name) & (User.last_name == self.last_name) & (User.number == self.number) & (User.user_id == self.user_id)))
    

    def update_email(self, new_email:str):
        """
        Function updates a contact category for a specified contact for a specified users account in the database (..contact_table) that matchs the provided contact first_name, last_name, number and user_id provided

        Input:
         self : user_id
         self : first_name
         self : last_name
         self : number
         new_category : New Email / Former Email Replacement

        Return:
         nothing 
        """
        self.users_contact_table.update(set('email', new_email), ((User.first_name == self.first_name) & (User.last_name == self.last_name) & (User.number == self.number) & (User.user_id == self.user_id)))


# contact = ContactTable('munachi', 'ebereonwu', '08141822937', 1, 'friend')
# # contact.insert_contact()
# contact.update_first_name('david')

# test = UserTable('einsteinmuna', 'einsteinmunachiso@gmail.com', 'muna123')
# user_id = test.get_id()
# test.insert_user()
# test_1 = ContactTable('abraham', 'ogudu', '09036274527', user_id, 'friend', 'ogudu11@gmail.com')
# # test_1.insert_contact()
# test_1.update_last_name('school-mate')