#!/usr/bin/python3
""" defines the state class model """

from models.base_model import BaseModel


class State(BaseModel):
    """ Creates the State Model
    arguments:
    name: the state's name
    """

    name = ""
