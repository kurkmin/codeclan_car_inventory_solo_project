import unittest
from models.manufacturer import Manufacturer

class TestManufacturer(unittest.TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer("Audi", "luxury", "Germany")

    def test_manufacturer_has_name(self):
        self.assertEqual("Audi", self.manufacturer.name)

    def test_manufacturer_has_position(self):
        self.assertEqual("luxury", self.manufacturer.position)

    def test_manufacturer_has_country(self):
        self.assertEqual("Germany", self.manufacturer.country)

