#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """
        Getter method for the list of City objects linked to the current State.
        """
        if models.storage.__class__.__name__ != 'DBStorage':
            return []

        associated_cities = []

        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                associated_cities.append(city)

        return associated_cities
