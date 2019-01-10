from pymongo import MongoClient

from .core import BaseDBWrapper


class MongoDBWrapper(BaseDBWrapper):
    """
    Mongo db wrapper class
    """
    def get_client(self):
        self.get_required()
        if self.host and self.port:
            self.client = MongoClient(self.host, self.port)
        else:
            self.client = MongoClient(self.url)
        return self.client