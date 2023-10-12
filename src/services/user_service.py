from src.models.User import User
import json
import uuid
from flask_jwt_extended import create_access_token
from bcrypt import hashpw, gensalt, checkpw

class UserService:
    def __init__(self, db_file):
        self.db_file = db_file

    def register_user(self, username, mail, password):
        users = self.load_users()
        for user in users:
            if user.username == username or user.mail == mail:
                return False
        id = str(uuid.uuid4())
        hashed_password = self.hash_password(password)
        new_user = User(id, username, mail, hashed_password)
        users.append(new_user)
        self.save_users(users)
        return True
    
    def login_user(self, username, password):
        user = self.find_user_by_username(username)

        if user and self.check_password(user, password):
            access_token = create_access_token(identity=user.id)
            return access_token

        return False

    def load_users(self):
        try:
            with open(self.db_file, 'r') as file:
                data = json.load(file)
            users = data.get('users', [])
            users = [User(**user) for user in users]
        except FileNotFoundError:
            users = []
        return users

    def find_user_by_username(self, username):
        users = self.load_users()
        for user in users:
            if user.username == username:
                return user
        return None
    
    def find_user_by_id(self, id):
        users = self.load_users()
        for user in users:
            if user.id == id:
                return user
        return None

    
    def save_users(self, users):
        data = {'users': [user.__dict__ for user in users]}
        with open(self.db_file, 'w') as file:
            json.dump(data, file)

    def check_password(self, user, password):
        stored_password = user.password
        return checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))        

    def hash_password(self, password):
        return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')
