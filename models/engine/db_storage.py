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
        """DBStorage Constructor
        getting the need variables from the environment to create
        the database url that's need for creating the database engine"""
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
        """Fetching records of all tables
        or based on a specific table name"""
        objs_list = []
        objs_dict = {}
        if cls:
            objs_list = self.__session.query(cls).all()
        else:
            for curr_cls in Base.__subclasses__():
                data = self.__session.query(curr_cls).all()
                objs_list.extend(data)
        for obj in objs_list:
                key = '{}.{}'.format(obj.to_dict()['__class__'],
                        obj.to_dict()['id'])
                objs_dict[key] = obj
        return objs_dict

    def new(self, obj):
        """Creating new record"""
        self.__session.add(obj)

    def save(self):
        """Saving or commitng a new record
        to a specific table"""
        self.__session.commit()

    def delete(self, obj=None):
        """Removing table or object"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creating the tables when importing the module
        and creating session factory using scoped session
        which will handle closing the session automatically
        and make the session is thread-safe"""
        Base.metadata.create_all(DBStorage.__engine)
        session_factory = sessionmaker(DBStorage.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)
