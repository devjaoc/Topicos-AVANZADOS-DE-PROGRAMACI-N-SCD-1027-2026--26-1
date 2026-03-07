class User:
    def __init__(self, username):
        self.username = username
        #self.role = role  # "admin", "student", "teacher"
    def getRole(self):
        return self.username
        