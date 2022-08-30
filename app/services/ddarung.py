from app.models.ddarung import DDarung
from app.utils.context import Context
import pandas as pd

class DDarungService:
    
    ddarung = DDarung()
    
    def preprocess(self, path, train, test):
        model = self.ddarung
        this = model.context
        this.train = model.from_csv(path, train)
        this.test = model.from_csv(path, test)
        this.id = this.test['id']
        this = model.missing_value_process_median(this)
        
        return this
        
    def submit(self, path, train, test):
        this = self.preprocess(path, train, test)
        Context.show_spec(this.train)
