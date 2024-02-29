#!/usr/bin/python3
import unittest
from models.city import City
from datetime import datetime
from models import storage


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()
    def test_instance(self):
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)
        
    def test_attributes(self):
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
    def test_defaults(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)
    def test_to_dict(self):
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)
        self.assertEqual(city_dict['state_id'], self.city.state_id)
        self.assertEqual(city_dict['name'], self.city.name)
    def test_save(self):
        initial_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(initial_updated_at, self.city.updated_at)