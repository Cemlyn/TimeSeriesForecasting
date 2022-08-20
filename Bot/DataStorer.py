import uuid
from datetime import datetime
from typing import Callable


class DataStoreException(Exception):
    pass


class DataStore:
    def __init__(self,
                 name=(uuid.uuid4()),
                 cold_start=True,
                 padding=True,
                 differential=300,
                 indicators=list()):
        self._name = name
        self._init_time = datetime.today().strftime('%Y-%m-%d %H:%m:%S')
        self._cold_start = cold_start
        self._indicators = indicators
        self._data = list()
        self._differential = differential
        self._counter = 0
    
    def add_datum(self,datum):
        # check correct object type
        if not isinstance(datum,dict):
            raise DataStoreException('datum must be a python dictionary type object')
            
        # check it has the correct keys
        if 'timestamp' not in datum:
            raise DataStoreException('timestamp key must be provided in datum')
            
        if len(self._data)==0:
            self._data.append(datum)
            self._data_df = pd.DataFrame(datum,index=[self._counter])
            self._counter+=1
        else:
            # check the time differential between data points
            differential = datum['timestamp'] - self._data[-1]['timestamp']
            if differential!=self._differential:
                raise DataStoreException(f'differential of {differential} did not match the stated differential.')
                
            self._data.append(datum)
            
            data_df = pd.DataFrame(datum,index=[self._counter])
            self._data_df = pd.concat([self._data_df,data_df],axis=0)
            self._counter+=1
            
            self.calc_indicators()
            
    def calc_indicators(self):
        for indicator in self._indicators:
            if isinstance(indicator, Callable):
                print(indicator(self._data_df))
            else:
                print('fail')