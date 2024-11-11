from abc import ABC, abstractmethod

"""
    Template class for database repositories
"""


class DbTemplate(ABC):
    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def update(self, id, new_data):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def close(self):
        pass
