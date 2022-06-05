class Admin:
    def __init__(self):
        self.admins = {}

    def add_admin(self, username, password):
        self.admins[username] = password

    def check_admin(self, username, password):
        if username in self.admins:
            if self.admins[username] == password:
                return True
        return False