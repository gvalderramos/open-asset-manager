from pymongo import MongoClient


class ModelBase(object):
    _CONN_STR = "mongodb://dbuser:Pass1234@127.0.0.1:27017/openassetmanagerdb"

    def __init__(self) -> None:
        self._client = MongoClient(self._CONN_STR)
    
    @property
    def db(self):
        return self._client.openassetmanagerdb
