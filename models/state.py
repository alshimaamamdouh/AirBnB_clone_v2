#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from models.base_model import Base
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ Getter """
            from models.engine.file_storage import FileStorage
            storage = FileStorage()
            cities_dict = storage.all(City)
            return [city for city  in cities_dict.values() if city.state_id == self.id]
