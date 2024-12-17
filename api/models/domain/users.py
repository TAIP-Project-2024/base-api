class User:
    def __init__(self, email=None, password=None, first_name=None, last_name=None):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def set_user(self, email, password, first_name, last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def get_user_details(self):
        return {
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
