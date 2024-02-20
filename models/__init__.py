#!/usr/bin/python3
"""models init that reloading the storage with every execution"""
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()   
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
