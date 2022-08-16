from tinydb import TinyDB, Query, where


# Instance of database querier.
User = Query()
# database creation.
database = TinyDB('Database/database.json')



class UserTable():
    """
    Class for operating on Database (UserTable).
    """

    def __init__(self , user_name:str, email:str = 'nil', password:str = 'nil',):

        # Parameters for users.
        self.user_name = user_name
        self.email = email
        self.password = password
        # Addition of Users table to database
        self.users_table = database.table("Users")


    # function to enter new user.
    def insert_user(self):
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
    def user_exists(self):
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
    def delete_user(self):
        """
        Function deletes user from database with user_name provided

        Input:
        user_name : String 
        """
        self.users_table.remove(User.user_name == self.user_name)


    # Function to get user ID
    def get_id(self):
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
        table_name = str(first_name)+"_"+str(self.last_name)+"_contact_db"
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
        Function deletes a contact from a specified users account n the database (..contact_table) with user_name provided

        Input:
         self : user_id
         self : users_contact_table

        Return:
         nothing 
        """
        self.users_contact_table.remove((User.first_name == self.first_name) & (User.last_name == self.last_name) & (User.number == self.number) & (User.user_id == self.user_id))



contact = ContactTable('Caleb', 'Ogudu', '081418238598888', 1)
# contact.insert_contact()
contact.delete_contact()