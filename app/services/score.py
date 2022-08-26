from app.models.score import Score

class ScoreService(object):
    def __init__(self)->None: 
        pass
    
    def average(self, korean, english, math):
        score=Score(korean, english, math)
        print(score.average_score())