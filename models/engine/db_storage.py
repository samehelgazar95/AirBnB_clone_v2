#!/usr/bin/python3
""" DatabBase Storage for SQLAlchemy """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        dialect = 'mysql'
        driver = 'mysqldb'
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')
        db_url = '{}+{}://{}:{}@{}/{}'.format(
                dialect, driver, user,
                password, host, db_name)

        DBStorage.__engine = create_engine(db_url, pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        temp_list = []
        objects = {}
        if cls:
            temp_list.extend(self.__session.query(cls.__name__).all())
        else:
            for cur_cls in Base.__subclasses__():
                temp_list.extend(self.__session.query(cur_cls).all())
        for obj in temp_list:
            key = obj.name + '.' + obj.id
            objects[key] = obj
        return objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(DBStorage.__engine)
        session_factory = sessionmaker(DBStorage.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)
