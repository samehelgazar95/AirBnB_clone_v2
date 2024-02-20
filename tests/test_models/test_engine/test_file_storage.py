#!/usr/bin/python3
import unittest
import os
import models
from models import base_model
from models.engine.file_storage import FileStorage


class TestBase(unittest.TestCase):
    """Testing instantiation and attributes"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_does_module_has_doc(self):
        doc = models.engine.file_storage.__doc__
        self.assertTrue(len(doc) > 0)

    def test_does_class_has_doc(self):
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_is_FileStorage_a_class(self):
        b = FileStorage()
        cls_name = "<class 'models.engine.FileStorage'>"
        self.assertTrue(str(b.__class__), cls_name)

    def test_does_FileStorage_has_private_file_path(self):
        obj = FileStorage()
        self.assertEqual(str, type(obj._FileStorage__file_path))

    def test_does_FileStorage_has_private_objects(self):
        obj = FileStorage()
        self.assertEqual(dict, type(obj._FileStorage__objects))

    def test_FileStorage_all(self):
        obj = FileStorage()
        self.assertEqual(dict, type(obj.all()))

    def test_new(self):
        instance = base_model.BaseModel()
        store = FileStorage()
        store.new(instance)
        key = f'{instance.__class__.__name__}.{instance.id}'
        self.assertIn(key, store._FileStorage__objects)

    def test_save(self):
        store = FileStorage()
        instance = base_model.BaseModel()
        store.new(instance)
        store.save()
        key = f'{instance.__class__.__name__}.{instance.id}'
        with open('file.json', 'r') as f:
            data = f.read()
        self.assertIn(key, data)

    def test_reload(self):
        store = FileStorage()
        instance = base_model.BaseModel()
        store.new(instance)
        store.save()
        store.reload()
        key = f'{instance.__class__.__name__}.{instance.id}'
        self.assertIn(key, store._FileStorage__objects)


if __name__ == "__main__":
    unittest.main()
