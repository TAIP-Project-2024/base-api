import psycopg2
from psycopg2 import pool
from django.conf import settings


class PostgreSQLConnectionPool:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PostgreSQLConnectionPool, cls).__new__(cls)
            cls._instance._pool = pool.SimpleConnectionPool(
                minconn=1,  # Minimum number of connections
                maxconn=20,  # Maximum number of connections
                # TODO: add connection details (user, password, database, etc)
            )
        return cls._instance

    def get_conn(self):
        # Obtain a connection from the pool
        return self._pool.getconn()

    def put_conn(self, conn):
        # Return a connection to the pool
        self._pool.putconn(conn)

    def close_all(self):
        # Close all connections of the pool
        self._pool.closeall()
