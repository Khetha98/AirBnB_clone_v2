#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")
    
    @property
    def cities(self):
        var = models.storage.all()
        list_a = []
        res = []
        for key in var:
            city = key.replace(".", " ")
            city = shlex.split(city)
            if (city[0] == 'City'):
                list_a.append(var[key])
        for element in list_a:
            if (element.state_id == self.id):
                res.append(element)
            return (res)
