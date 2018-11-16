"""User Model"""
users = []

class UserModel:
    """Class user model"""
    def __init__(self):
        """Initialize the user model class"""
        self.db = users

    def add_users(self, firstname, lastname, username, email, password):
        """Adding new users"""
        payload = {
            'user_id' : len(users) + 1,
            'firstname': firstname, 
            'lastname' : lastname,
            'username' : username,
            'email' : email,
            'password' : password      
        }
        usr = self.db.append(payload)
        return usr

    def get_all_users(self):
        """Returning all users"""
        return self.db

 
