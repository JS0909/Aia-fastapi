from app.models.user import User

class UserService(object):
    def __init__(self)->None: 
        pass

    def calculate(self, id, pw):
        user =  User(id, pw)
        print('ID: '+user.id, 'PW: '+user.pw)