import icecream as ic
from dataclasses import dataclass
@dataclass # 데코레이터

class Context:
    path: str
    fname: str
    train: object
    test: object
    id: str
    label: str

    @property
    def path(self): return self._path
    
    @path.setter
    def path(self, path): self._path = path
    
    @property
    def fname(self) -> str : return self._fname
    
    @fname.setter
    def fname(self, fname): self._fname = fname
    
    @property
    def train(self) -> object: return self._train

    @train.setter
    def train(self, train): self._train = train
    
    @property
    def test(self) -> object: return self._test
    
    @test.setter
    def test(self, test): self._test = test
    
    @property
    def id(self) -> str: return self._id
    
    @id.setter
    def id(self, id): self._id = id
    
    @property
    def label(self) -> str: return self._label
    
    @label.setter
    def label(self, label): self._label = label
    
    @staticmethod
    def show_spec(param):
        ic(param.shape)
        ic(param.columns)
        ic(param.info())
        ic(param.describe())
        ic(param)