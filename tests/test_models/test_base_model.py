#!/usr/bin/python3
"""
Defines unittests for the BaseModel class
models/base_model.py.

Unittest test cases:
    TestBaseModel_instantiation (create)
    TestBaseModel_save
    TestBaseModel_to_dict
    TestBaseModel___str__ print
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """
    Testing instantiation of the BaseModel class.
    """

    def test_no_args_instantiates(self):
        """
        Test if BaseModel is instantiated
        And it's a class
        """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        """Test for new instances"""
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test for id instances"""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        """Test for created at instances"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test for updated at instances"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        """Test for two models unique ids"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        """Test that two models are different created at"""
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)


if __name__ == "__main__":
    unittest.main()
