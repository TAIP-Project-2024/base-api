from io import BytesIO, StringIO
from dotenv import load_dotenv, find_dotenv
import os

from pymongo import MongoClient

from gridfs import GridFS

from api.repositories.general.security_aop import logging_and_security
class FileRepository:

    def __init__(self, client, db, collection):
        self._closed = False
        self.client = MongoClient(client)
        self.db = self.client[db]
        self.fs = GridFS(self.db, collection=collection)

    def close(self):
        """Explicitly close the MongoDB client."""
        if not self._closed:
            self.client.close()
            self._closed = True

    def __del__(self):
        """Destructor to ensure resources are released if close() is not called."""
        try:
            self.close()
        except Exception:
            # Suppress any exception during interpreter shutdown
            pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__del__()

    @logging_and_security
    def add(self, name, file_buffer):
        """Add a new graph to GridFS"""
        file_id = self.fs.put(file_buffer, filename=name)
        return file_id

    @logging_and_security
    def get(self, name):
        """Retrieve a file by its name"""
        file = self.fs.find_one({"filename": name})
        if file:
            buffer = BytesIO(file.read())
            return buffer
        else:
            return None

    def get_all_names(self):
        """Retrieve all drawing names from GridFS"""
        file_names = [file.filename for file in self.fs.find()]
        return file_names

    def check_exists(self, name):
        return self.fs.exists({"filename": name})

    @logging_and_security
    def update(self, name, graph_drawing_file_buffer):
        """Update an existing file by its name"""
        file = self.fs.find_one({"filename": name})
        if file:
            self.fs.delete(file._id)
        file_id = self.fs.put(graph_drawing_file_buffer, filename=name)
        return file_id

    @logging_and_security
    def delete(self, name):
        """Delete a drawing by its name"""
        file = self.fs.find_one({"filename": name})
        if file:
            self.fs.delete(file._id)
            return True
        return False

    def delete_from_list(self, list):
        """
        Deletes from a list of drawing id's
        """
        for id in list:
            self.fs.delete(id)

    def find_by_regex(self, regex):
        query = {"filename" : {"$regex" : regex}}
        return list(self.fs.find(query))