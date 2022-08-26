class Score(object):
    def __init__(self, korean, english, math):
        self.korean = korean
        self.english = english
        self.math = math 
        
    def average_score(self):
        average = (self.korean + self.english + self.math)/3
        return round(average, 2)