#!/usr/bin/python3
""" This module contain Relational DB engine. """


from os import getenv
from sqlalchemy import create_engine
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.base_model import Base


class DBStorage:
    """ This module contain Relational DB engine. """

    __engine = None
    __session = None

    def __init__(self):
        """ The class custructor Method. """

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                                        getenv("HBNB_MYSQL_USER"),
                                        getenv("HBNB_MYSQL_PWD"),
                                        getenv("HBNB_MYSQL_HOST"),
                                        getenv("HBNB_MYSQL_DB")
                                        ), pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session (self.__session) all
        objects depending of the class name (argument cls). """

        if cls:
            if type(cls) == str:
                cls = globals()[cls]
            result = self.__session.query(cls)
            dic = {}
            for obj in result:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                dic[key] = obj
            return dic

        else:
            c_ls = ["City", "State", "User", "Place"]
            dic = {}
            for clss in c_ls:
                cls = globals()[clss]
                cls_set = self.__session.query(cls)
                for obj in cls_set:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    dic[key] = obj
            return dic

    def new(self, obj):
        """ add the object to the current database
        session (self.__session). """

        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current
        database session (self.__session). """

        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database
        session obj if not None. """

        self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database. """

        from sqlalchemy.orm import sessionmaker, scoped_session
        from sqlalchemy.ext.declarative import declarative_base

        Base.metadata.create_all(bind=self.__engine)

        Session = scoped_session(
                sessionmaker(bind=self.__engine, expire_on_commit=False)
                )
        self.__session = Session()
