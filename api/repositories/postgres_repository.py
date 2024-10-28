import psycopg2
from psycopg2 import sql
from db_template import DbTemplate

"""
    Concrete implementation of DbTemplateRepository:
        PostgreSQL Repository
"""

class Postgres(DbTemplate):
    def __init__(self, db_config):
        # TODO: connection
        self.connection = psycopg2.connect(**db_config)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def create(self, data):
        # TODO
        pass

    def get(self, id):
        # TODO
        pass

    def update(self, id, new_data):
        # TODO
        pass

    def delete(self, id):
        # TODO
        pass

    def close(self):
        self.cursor.close()
        self.connection.close()
