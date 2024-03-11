#!/usr/bin/python3
"""Defines a class User that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """
        Initializes User instance

        Public class attributes:
            email (str): The email of the user.
            password (str): The password of the user.
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
        """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
