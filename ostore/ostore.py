#
# OStore
#
import pymongo


class OStore:
    def __init__(self):
        self.config = {
            "host": "mongodb://localhost:27017/",
            "db": "ostore"
        }
        self._mongo = None
        self._db = None

    def connect(self):
        if self._mongo is None:
            self._mongo = pymongo.MongoClient(self.config['host'])
            self._db = self._mongo[self.config['db']]

    def save(self, col, dato):
        self.connect()
        result = self._db[col].insert_one(dato)
        return result.inserted_id

    def load(self, col, hash_id):
        self.connect()
        return self._db[col].find_one({"_id": hash_id})
