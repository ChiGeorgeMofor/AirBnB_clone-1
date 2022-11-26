#!/usr/bin/python3
""" defines the base_model """


from datetime import datetime

import models
from uuid import uuid4


class BaseModel:
    """ Creates the base model class
    that serves as a mother class to all other classes """

    def __init__(self, *args, **kwargs):

        if kwargs:
            tf = "%Y-%m-%dT%H:%M:%S.%f"
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"], tf)
        kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], tf)

        for key, value in kwargs.item():
            if key != "__class__":
                setattr(self, key, value)
    else:
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def save(self):
        """ updates the updated at time with the current date time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """ string representation of BaseModel class """
        sc = self.__class__.__name__
        return "[{}] ({}) {}".format(sc, self.id, self.__dict__)

    def to_dict(self):
        """ representation of an instance in dict format """
        new_dict = dict(self.__dict__)
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
