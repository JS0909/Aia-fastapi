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
import numpy as np
from icecream import ic
import random
import string


class PandasQuiz(object):
    # 아무 역할을 하지 않는 생성자라면 없애도 무관. 디폴트로 생성되어 있음.
    
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
        ic(self.get_id())
        ic(self.get_score())
        ic(self.get_df())
    
    def get_id(self):
        return ''.join([random.choice(string.ascii_letters) for i in range(5)])
        
    def get_score(self):
        return random.sample(range(0,101), 4)
    
    def get_df(self):
        return pd.concat([pd.DataFrame.from_dict({self.get_id():self.get_score()}, orient='index', 
                                                 columns=['국어', '영어', '수학', '사회']) for i in range(10)], ignore_index=False)


    ''' 
    Q5 원하는 과목 점수만 출력하시오. (만약 국어라고 입력하면 아래와 같이 출력됨)
        hVoGW    93
        QkpKK    25
        oDmky    82
        qdTeX    51
        XGzWk    34
        PAwgj    85
        vnTmB    28
        wuxIm    58
        AOQFG    32
        jHChe    59
        Name: 국어, dtype: int64
    
    '''
    
    def quiz_05(self):
        print(self.get_df()[input('과목 입력>>')])
    
    
    ''' 
    Q6 원하는 학생점수만 출력하시오. (아이디가 랜덤이므로 맨 위에 학생점수 출력으로 대체함)
        lDZid  57  90  55  24
    '''
    def quiz_06(self):
        print(self.get_df().iloc[[0]])
        
        
    '''
    Q7 각 학생들의 점수의 총합과 마지막 행은 과목총점 추가해서 출력
        ic| df5:  국어   영어   수학   사회   과학    총점
            hVoGW   93   44   14   94   86   331
            QkpKK   25   54   29   10    8   126
            oDmky   82   65   31   31    2   211
            qdTeX   51   56   56    3   13   179
            XGzWk   34   32   67   48   23   204
            PAwgj   85   24   16    8   22   155
            vnTmB   28   80   52   43   48   251
            wuxIm   58   94   93   54   83   382
            AOQFG   32   50   95    1   52   230
            jHChe   59   37   80   27   39   242
            과목총점   547  536  533  319  376  2311
    '''
    def quiz_07(self):
        df = self.get_df()
        df['과학'] = random.sample(range(0, 101), 10)
        df['총점'] = df.sum(axis=1)
        df.loc['과목총점'] = df.sum(axis=0)
        ic(df)
        