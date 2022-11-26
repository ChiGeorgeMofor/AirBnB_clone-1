#!/usr/bin/python3
""" defines the place class model """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Creates the Place model.
    arguments:
    city_id(string): unique id of the city
    user_id(string): unique id of the user
    name(string): the name of the place
    description(string): description of the place
    number_rooms(integer):number of rooms required
    number_bathrooms(integer):number of bathrooms
    max_guest(integer): maximum number of guest the place can take
    price_by_night(integer): price it takes to spend just a night
    latitude(float): latitude of the place
    longitude(float): longitude of the place
    amenity_ids([string]): A list of amenities and their unique id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
