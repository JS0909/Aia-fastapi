class Caculator(object):
    def __init__(self, first, second): 
        self.first = first
        self.second = second
            
    def sum(self) :
        return self.first + self.second
    
    def subtract(self) :
        return self.first - self.second

    def divide(self) :
        return self.first / self.second
    
    def multiple(self) :
        return self.first * self.second
    