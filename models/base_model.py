#!/usr/bin/python3
"""
Defines the BaseModel class.
It defines all common attributes/methods for other classes
"""

from datetime import datetime
import uuid


class BaseModel:
    """
    Represents the base model for the Airbnb Clone project
    """

    def __init__(self, **kwargs):
        """
        Initialize a new BaseModel.
        Defines the attributes: id, created_at, updated_at
        :param **kwargs: Key/value pairs of arguements (dict).
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Method to update public instance attribute
        'updated_at' with the current datetime

        Save to storage later - models.storage.save()
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Method to returns a dictionary containing all
        keys/values of __dict__ of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict