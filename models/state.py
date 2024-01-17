#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ returns the list of City instances with state_id
            equals to the current State.id => It will be the FileStorage
            relationship between State and City. """

            ls = []
            all_city = models.storage.all("City")
            for key, value in all_city.items():
                if self.id == value.state_id:
                    ls.append(value)
            return ls
