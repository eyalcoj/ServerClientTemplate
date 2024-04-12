from src.server.user import ServerUser


class UsersDatabase:
    def __init__(self):
        self.users = {}

    def add_user(self, identifier, user: ServerUser):
        if identifier in self.users:
            print(f"User with identifier {identifier} already exists.")
            return False
        self.users[identifier] = {'user': user}
        return True

    def get_user(self, identifier):
        return self.users.get(identifier)

    def update_user(self, identifier, user: ServerUser = None):
        if identifier in self.users:
            if user:
                self.users[identifier]['user'] = user
            return True
        return False

    def remove_user(self, identifier):
        if identifier in self.users:
            del self.users[identifier]
            return True
        return False
