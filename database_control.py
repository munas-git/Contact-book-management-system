import uuid
from tinydb import TinyDB, Query
from tinydb.operations import set


# Instance of UUID
uuid_gen = uuid.uuid1()


# Instance of database querier.
User = Query()
# database creation.
database = TinyDB('Database/contactBookDb.json')



class UserTable():
    """
    Class for operating on Database (UserTable).
    """

    def __init__(self , user_name:str, password:str, email:str = 'nil'):

        # Parameters for users.
        self.user_name = user_name
        self.email = email.lower()
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
        self.users_table.remove((User.user_name == self.user_name) & (User.password == self.password))


    # Function to get user ID
    def get_id(self) -> int:
        """
        Function gets user ID from database with user_name provided

        Input:
        user_name : String 
        """
        id = (self.users_table.get(User.user_name == self.user_name).doc_id)
        return int(id)



class ContactTableSetUp():
    """
    Class for Setting up table on Database (ContactTable).
    """

    def __init__(self, user_id:int, first_name:str = 'nil', last_name:str = 'nil', address:str = 'nil', organization:str = 'nil', number:str = 'nil', email:str = 'nil', social_handle = 'nil', category:str = 'nil'):

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.address = address
        self.organization = organization
        self.number = number
        self.email = email.lower()
        self.social_handle = social_handle
        self.category = category.title()
        self.user_id = user_id
        
        # Generating database table name using user ID
        self.table_name = 'user_'+str(self.user_id)+'_contacts'
        # User's contact database creation
        self.users_contact_table = database.table(self.table_name)


    def insert_contact(self) -> None:
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
                'contact_id' : str(uuid_gen),
                'user_id' : self.user_id,
                'first_name' : self.first_name,
                'last_name' : self.last_name,
                'address' : self.address,
                'organization' : self.organization,
                'number' : self.number,
                'email' : self.email,
                'social_handle' : self.social_handle,
                'category' : self.category,
            }
        )


    def return_all_contacts(self, table_name) -> list:
        """
        Function returns all contacts for the specified user with the table_name provided.
        Input:
         self
         table_name:str - Name of table to return all contacts from

        Return:
         all_contacts:list 

        """
        table = database.table(table_name)
        all_contacts = table.all()
        return(all_contacts)


class ContactTableManipulation():

    def __init__ (self, table_id, contact_id):
        self.table_id = table_id
        self.contact_id = contact_id

    def delete_contact(self) -> None:
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


    def update_first_name(self, new_first_name:str) -> None:
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
        self.users_contact_table.update(set('first_name', new_first_name)), ((User.first_name == self.first_name) & (User.last_name == self.last_name) & (User.number == self.number) & (User.user_id == self.user_id))
    

    def update_last_name(self, new_last_name:str) -> None:
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
    

    def update_number(self, new_number:str) -> None:
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


    def update_category(self, new_category:str) -> None:
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
    

    def update_email(self, new_email:str) -> None:
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
    

    def search_for_contact(self, contact_id, table_name) -> list:
        """
        Function returns dictionary in list containing matching contacts info.
        Input:
         self
         name:str - name of contact
         table_name:str - Name of table to return all contacts from

        Return:
         contact_details: Dictionary in list containing searched contact details.
        """
        table = database.table(table_name)
        contact_details = table.search(User.contact_id == contact_id)
        return contact_details



    def update_contact(self, new_last_name:str) -> None:
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