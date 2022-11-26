#!/usr/bin/python3
""" defines the review class model """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Creates the Review model
    arguments:
    place_id(str): unique id of the place
    user_id(str): unique id of the user
    text: the review text
    """

    place_id = ""
    user_id = ""
    text = ""
