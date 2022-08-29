'''
Q1. 다음 결과 출력
   a  b  c
1  1  3  5
2  2  4  6

ic| df1:    a  b  c
         1  1  3  5
         2  2  4  6
'''
import pandas as pd
from icecream import ic
import random
import string

from pyparsing import col

class PandasQuiz(object):
    def __init__(self)->None:
        pass
    
    def quiz_01(self):
        df1 = pd.DataFrame.from_dict({'1' : [1, 3, 5], '2' : [2, 4, 6]}, columns=['a','b','c'], orient='index')
        ic(df1)
        
    '''         
    Q2. 다음 결과 출력
        A   B   C
    1   1   2   3
    2   4   5   6
    3   7   8   9
    4  10  11  12
    ic| df2:     A   B   C
            1   1   2   3
            2   4   5   6
            3   7   8   9
            4  10  11  12
    '''
    def quiz_02(self):
        df2 = pd.DataFrame.from_dict({'1':[1,2,3],'2':[4,5,6],'3':[7,8,9],'4':[10,11,12]}, columns=['A','B','C'],  orient='index')
        ic(df2)
    
    '''Q3 두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
        ic| df3:     0   1   2
                 0  95  25  74
                 1  44  24  97
    '''
    
    def quiz_03(self):
        df3 = pd.DataFrame.from_dict({'0':random.sample(range(10,100), 3), '1':random.sample(range(10,100), 3)}, orient='index')
        ic(df3)
        
        ''' 
        
        Q4 국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성. 단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기
        ic| self.id(): 'HKKHc'
        ic| self.score(): 22
        ic| df4:        국어  영어  수학  사회
                   lDZid  57  90  55  24
                   Rnvtg  12  66  43  11
                   ljfJt  80  33  89  10
                   ZJaje  31  28  37  34
                   OnhcI  15  28  89  19
                   claDN  69  41  66  74
                   LYawb  65  16  13  20
                   QDBCw  44  32   8  29
                   PZOTP  94  78  79  96
                   GOJKU  62  17  75  49
        
        '''   
    def quiz_04(self):
        ic(self.id())
        ic(self.score())
        df4 = pd.DataFrame.from_dict({self.id():self.score()}, orient='index', columns=['국어', '영어', '수학', '사회'])
        for i in range(8):
            df4 = pd.concat([df4,pd.DataFrame.from_dict({self.id():self.score()}, orient='index', columns=['국어', '영어', '수학', '사회'])],axis=0)
        
        ic(df4)
        
    
    def id(self):
        rand_str = ''
        for i in range(5):
            rand_str += random.choice(string.ascii_letters)
        return rand_str
    
    def score(self):
        return random.sample(range(0,100), 4)
