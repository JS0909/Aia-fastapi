from ctypes.wintypes import PWORD


class User(object):
    def __init__(self, id, pw):
        self.id = id
        self.pw = pw
        
    def user_return(self):
        return self.id, self.pw