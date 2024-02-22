#!/usr/bin/python3
"""models init that reloading the storage with every execution"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
