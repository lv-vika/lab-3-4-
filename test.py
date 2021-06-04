import unittest
from manager import *
from models import *


class TestCarChemistry(unittest.TestCase):

    def setUp(self) -> None:
        self.a = AirFreshener("Allure sport", 139, 25, "Dope", "strawberry")
        self.b = Oil("oil1", 300, 10, "brand1", 10, 400)
        self.c = AirFreshener("AirWick", 101, 200, "Lemon Flower", 250)
        self.d = WindshieldWasher("Prestone", 520, 34, "Washer Fluid", 70, -32)

        objects = [self.a, self.b, self.c, self.d]
        self.car_manager = CarChemistryStoreManager(objects)

    def test_sort_by_price(self):
        self.assertEqual(self.car_manager.sort_by_price(False), [self.c, self.a, self.b, self.d])

    def test_sort_by_balance(self):
        self.assertEqual(self.car_manager.sort_by_balance(False), [self.b, self.a, self.d, self.c])

    def test_search_by_name(self):
        self.assertEqual(self.car_manager.search_by_name("oil1"), [self.b])