from tinydb import TinyDB, Query


# Users database
users_db = TinyDB('Database/users.json')
# Instance of query database
User = Query()


class UserDB():
    """
    Class for operating on User database.
    """

    def __init__(self , user_name:str , email:str = 'nil', password:str = 'nil'):

        self.user_name = user_name
        self.email = email
        self.password = password


    # function to enter new user.
    def insert_user(self):
        """
        Function inputs new user to the database
        """
        users_db.insert(
            {
                'user_name' : self.user_name,
                'email' : self.email,
                'password' : self.password
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
        if users_db.search(User.user_name == self.user_name):
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
        users_db.remove(User.user_name == self.user_name)


    # Function to get user ID
    def get_id(self):
        """
        Function gets user ID from database with user_name provided

        Input:
        user_name : String 
        """
        id = (users_db.get(User.user_name == self.user_name).doc_id)
        return int(id)



class ContactDB():
    """
    This class contains all functions for manipulating contacts that belong to users.
    """

    def __init__(self, first_name:str, last_name:str, number:str, user_id:int, category:str = 'nil'):

        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.category = category
        self.user_id = user_id


    def create_contact_db(self):
        db_name = self.user_id