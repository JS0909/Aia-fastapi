from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler, RobustScaler, StandardScaler,\
    QuantileTransformer, PowerTransformer
from sklearn.ensemble import RandomForestRegressor

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

from app.utils.context import Context

class DDarung:
    
    context = Context()
    
    def __init__(self):
        self.train_set = None
        self.test_set = None
    
    def hook(self, path, train, test):
        self.from_csv(path, train, test)
        self.data_preprocess(train)
        self.model()
        self.learning()
        self.evaluate_predict()
        

    # 1. data
    def from_csv(self, path, fname):
        this = self.context
        this.path = path
        this.fname = fname
        return pd.read_csv(this.path + this.fname)
    
    def data_preprocess(self, this):
        self.fillna_median(this)
        self.extract_label_in_train()
        self.xy_split()
    
    def fillna_median(self, this):
        train_set = this.train
        train_set = train_set.fillna(train_set.median())
        return this
        
    def extract_label_in_train(self):
        train_set = self.train_set
        x = train_set.drop(['count'], axis=1)
        y = train_set['count']
        return x, y
    
    def xy_split(self):
        x, y = self.extract_label_in_train()
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1234)
        return x_train, x_test, y_train, y_test
        
    
    # 2. model
    def model(self):
        model = RandomForestRegressor()
        return model

    # 3. compile, fit
    def learning(self):
        x_train, x_test, y_train, y_test = self.xy_split()
        self.model().fit(x_train, y_train)

    
    # 4. evaluate, predict
    def evaluate_predict(self):
        y_pred = model.predict(x_test)
        result = r2_score(y_test, y_pred)
        print('no scaler: ', round(result,4))
    

       



        

'''
# other scalers
sclist = [StandardScaler(),MinMaxScaler(),MaxAbsScaler(),RobustScaler(),QuantileTransformer(),
        PowerTransformer(method='yeo-johnson'), # 디폴트 
        PowerTransformer(method='box-cox')
            ]
            
for scl in sclist:

    if str(scl) == str(PowerTransformer(method='box-cox')):
        try:
            x_train = scl.fit_transform(x_train)
        except:
            print('box-cox 안됨')
            break
        
    x_train = scl.fit_transform(x_train)
    x_test = scl.transform(x_test)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    result = r2_score(y_test, y_pred)
    print(scl.__class__.__name__+'결과: ', round(result,4))
'''            
            
            
# no scaler:  0.7864
# StandardScaler결과:  0.7837
# MinMaxScaler결과:  0.787
# MaxAbsScaler결과:  0.7863
# RobustScaler결과:  0.7843
# QuantileTransformer결과:  0.7886
# PowerTransformer결과:  0.7925