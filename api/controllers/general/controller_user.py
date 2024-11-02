from repositories.postgres_repository import PostgresRepository
from view.view_login import ViewLogin
from models.users import User
from datetime import datetime
import bcrypt


class ControllerUser:
    def __init__(self, user, view, repository):
        # Dependency Injection Pattern: The ControllerUser class depends on User, ViewLogin, and PostgresRepository,
        # which are injected during initialization.
        self.user = user
        self.view = view
        self.repository = repository

    def add_user(self, email, password, conf_password, first_name, last_name):
        # Check if passwords match
        if password != conf_password:
            print("Passwords do not match! Please try again.")
            return

        # Check if email already exists
        existing_user = self.repository.read("users", f"email = '{email}'")
        if existing_user:
            print("Email already exists in the system!")
            return

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Set user details
        self.user.set_user(email, hashed_password, first_name, last_name)

        # Insert user into the database
        self.repository.create("users", {
            "email": email,
            "password": hashed_password,
            "first_name": first_name,
            "last_name": last_name,
            "created_at": datetime.now()
        })

        print("Registration successful!")
        self.view.show_login({"email": email, "first_name": first_name, "last_name": last_name})

    def login_user(self, email, password):
        # Check if the user exists
        user_data = self.repository.read("users", f"email = '{email}'")
        if not user_data:
            print("User not found!")
            return

        # Check password
        db_password = user_data[0][2]  # Assuming password is in the third column
        if bcrypt.checkpw(password.encode('utf-8'), db_password.encode('utf-8')):
            print("Login successful!")
            self.view.show_login({"email": email, "first_name": user_data[0][3], "last_name": user_data[0][4]})
        else:
            print("Incorrect password!")

    def get_user_events(self):
        # Return all events from the `users` table
        return self.repository.read("users")
