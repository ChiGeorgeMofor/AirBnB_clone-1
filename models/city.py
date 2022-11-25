#!/usr/bin/python3
""" Defines the City class module """
from models.base_model import BaseModel


class City(BaseModel):
    """ Creates the city class
    argument:
    state_id: the unique identification number of the state
    name: the name of the city
    """

    state_id = ""
    name = ""
