import psycopg2
from psycopg2 import sql
from datetime import datetime

class PostgresRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost',
            database='PoliticalSentimentDB',
            user='postgres',
            password='pwd123',
            port=5432
        )
        # Repository Pattern: Manages PostgreSQL operations
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def create(self, table_name, data):
        columns = data.keys()
        values = [data[column] for column in columns]
        insert_statement = sql.SQL("INSERT INTO {table} ({fields}) VALUES ({values})").format(
            table=sql.Identifier(table_name),
            fields=sql.SQL(', ').join(map(sql.Identifier, columns)),
            values=sql.SQL(', ').join(sql.Placeholder() * len(values))
        )
        self.cursor.execute(insert_statement, values)

    def read(self, table_name, condition):
        query = sql.SQL("SELECT * FROM {table} WHERE {condition}").format(
            table=sql.Identifier(table_name),
            condition=sql.SQL(condition)
        )
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update(self, table_name, data, condition):
        columns = data.keys()
        values = [data[column] for column in columns]
        set_statement = sql.SQL(', ').join(
            sql.SQL("{} = {}").format(sql.Identifier(col), sql.Placeholder()) for col in columns
        )
        update_statement = sql.SQL("UPDATE {table} SET {values} WHERE {condition}").format(
            table=sql.Identifier(table_name),
            values=set_statement,
            condition=sql.SQL(condition)
        )
        self.cursor.execute(update_statement, values)

    def delete(self, table_name, condition):
        delete_statement = sql.SQL("DELETE FROM {table} WHERE {condition}").format(
            table=sql.Identifier(table_name),
            condition=sql.SQL(condition)
        )
        self.cursor.execute(delete_statement)

    def close(self):
        self.cursor.close()
        self.connection.close()
