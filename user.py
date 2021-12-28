USER_NAME_ADMIN = "ADMIN"
PASSWORD = "PASSWORD"
CODE_ADMIN = "A123456"

def login(username, password, code):
    if USER_NAME_ADMIN == username and PASSWORD == password and CODE_ADMIN == code:
        if username==username and password== password and code==code:
            return True
    else:
        return False
class student:
    def __init__(self,username,password, code):
        self.username=username
        self.password=password
        self. code=code
    def show_course(self):
        pass
    def choice_course(self):
        pass
    def show_list_choice(self):
        pass
    def show_list_update(self):
        pass