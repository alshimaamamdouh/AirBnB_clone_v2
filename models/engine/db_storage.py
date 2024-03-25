#!/usr/bin/python3
""" deine db """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    '''
    Database Engine
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''instantiation
        '''
        # self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
        #                               format(getenv("HBNB_MYSQL_USER"),
        #                                      getenv("HBNB_MYSQL_PWD"),
        #                                      getenv("HBNB_MYSQL_HOST"),
        #                                      getenv("HBNB_MYSQL_DB")),
        #                               pool_pre_ping=True)
        # Retrieve MySQL connection details from environment variables
        MySQL_user = getenv('HBNB_MYSQL_USER')
        MySQL_pwd = getenv('HBNB_MYSQL_PWD')
        MySQL_host = getenv('HBNB_MYSQL_HOST')
        MySQL_database = getenv('HBNB_MYSQL_DB')
        # Create engine
        # The string form of the URL is dialect[+driver]://user:password@host/dbname[?key=value..],
        self.__engine = create_engine(
            f'mysql+mysqldb://{MySQL_user}:{MySQL_pwd}@{MySQL_host}/{MySQL_database}', pool_pre_ping=True)
        # Get the env variable
        env_var = getenv('HBNB_ENV')
        # Drop all tables if env_var = 'test
        if env_var == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        '''query on the current database session '''
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        '''add the object to the current database session 
        '''
        self.__session.add(obj)

    
    def save(self):
        ''' commit all changes of the current database session'''
        self.__session.commit()
    
    def delete(self, obj=None):
        '''delete from the current database session obj
        '''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''create all tables in the database &
        create the current database session
        '''
        # 1. Create tables
        Base.metadata.create_all(bind=self.__engine)
        # open session object to interact with data
        # 1.Session class is defined using sessionmaker()
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        # 2.The session obj is then set up using its default constructor
        self.__session = Session()
        
        
    def close(self):
        """Close the working session."""
        self.__session.remove()
