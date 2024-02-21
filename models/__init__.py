#!/usr/bin/python3
"""models init that reloading the storage
with every execution either from FileStorage or
from DBStorage based on the var HBNB_TYPE_STORAGE"""
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')

if str(storage_type) == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
