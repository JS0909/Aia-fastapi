from app.models.grade import Grade

class GradeService(object):
    def __init__(self,name,korean,english,math):
        self.credit = 0
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

    def get_grade(self):
        self.set_grade()
        return self.credit
    
    def set_grade(self):
        grade = Grade(self.name, self.korean, self.english, self.math)
        grade.set_avg()
        avg = grade.get_avg()
        if avg >=90:
            self.credit='A'
        elif avg >=80:
            self.credit='B'
        elif avg >=70:
            self.credit='C'
        elif avg >=60:
            self.credit='D'
        else:
            self.credit='F'
        
            