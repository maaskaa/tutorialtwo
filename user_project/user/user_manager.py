class User:
    def __init__(self, username, email):
        if not username or not email:
            raise ValueError("Username and email are required.")
        self.username = username
        self.email = email

    def change_email(self, new_email):
        if "@" not in new_email:
            raise ValueError("Imnvalid email format")
        self.email = new_email
        
class UserManager:
    def __init__(self):
        self.users = {}
    def add_user(self, username, email):
        if username in self.users:
            raise ValueError('user alredy exists')
        user = User(username, email)
        self.users[username] = user
        return user

    def get_user(self, username):
        return self.users.get(username)

    def remove_user(self, username):
        if username not in self.users:
            raise ValueError('user not found.')
        del self.users[username]
        return True