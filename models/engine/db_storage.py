#!/usr/bin/python3
"""
DataBase Storage using SQLAlchemy
DataBase Storage using SQLAlchemy
"""
from os import getenv
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, scoped_session
# from models.base_model import Base

class DBStorage():
    """
    Manipulate the DB that's storing data
    Arguments:
        __engine: engine var to start the db
        __session: Session that's used to manipulate db
    """
    __engine = None
    __session = None
    pass

    def __init__(self):
        """
        DBStorage Constructor
        getting the need variables from the environment to create
        the database url that's need for creating the database engine
        and drops all tables if the environment is set to 'test'
        """
        dialect = 'mysql'
        driver = 'mysqldb'
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')
        db_url = '{}+{}://{}:{}@{}/{}'.format(dialect,driver,
                                              user,password,host,db_name)

        # try:
        #     engine = create_engine(db_url)
        #     Session = sessionmaker(bind=engine)
        #     # ... rest of your code ...
        # except Exception as e:
        #     print(f"An error occurred: {e}")
        
        # DBStorage.__engine = create_engine(db_url, pool_pre_ping=True)
        
        # if getenv('HBNB_ENV') == 'test':
            # Base.metadata.drop_all(self.__engine)
        print('+++ db_storage.py <<>> __init__() +++')

    def all(self, cls=None):
        """
        Get all objects from the database.
        If a class is specified, return all objects of that class.
        Otherwise, return all objects from all classes.
        Returns:
            dict: A dictionary containing objects indexed by their ID.
        """
        # objs_list = []
        objs_dict = {}
        # if cls:
        #     objs_list = self.__session.query(cls).all()
        # else:
        #     for curr_cls in Base.__subclasses__():
        #         data = self.__session.query(curr_cls).all()
        #         objs_list.extend(data)
        # for obj in objs_list:
        #     key = '{}.{}'.format(obj.to_dict()['__class__'],
        #                          obj.to_dict()['id'])
        #     objs_dict[key] = obj
        print('+++ db_storage.py <<>> all() +++')
        return objs_dict

    def new(self, obj):
        """
        Add a new object to the current database session.
        Args:
            obj (BaseModel): The object to be added.
        """
        # self.__session.add(obj)
        print('+++ db_storage.py <<>> new() +++')

    def save(self):
        """Commit changes to the current database session."""
        # self.__session.commit()
        print('+++ db_storage.py <<>> save() +++')

    def delete(self, obj=None):
        """
        Delete an object from the database session.
        Args:
            obj (BaseModel, optional): The object to be deleted.
        """
        # if obj:
        #     self.__session.delete(obj)
        print('+++ db_storage.py <<>> delete() +++')

    def reload(self):
        """
        Creating the tables when importing the module
        and creating session factory using scoped session
        which will handle closing the session automatically
        and make the session is thread-safe
        """
        # Base.metadata.create_all(self.__engine)
        # session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # session_factory_scope = scoped_session(session_factory)
        # self.__session = session_factory_scope()
        print('+++ db_storage.py <<>> reload() +++')
