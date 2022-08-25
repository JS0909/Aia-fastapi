from app.models.user import User

class UserService(object):
    def __init__(self)->None: 
        pass

    def user(self, id, pw):
      user = User(id, pw)
      print('ID:', user.id_())
      print('PW:', user.pw_())