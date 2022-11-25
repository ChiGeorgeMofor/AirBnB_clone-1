#!/usr/bin/python3
""" Defines the User Class model """

from models.base_model import BaseModel


class User(BaseModel):
    """ creates the user class
    arguments:
    email(str): Email address of the user
    password(str): user password
    first_name(str): user first name
    last_name(str): user last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
