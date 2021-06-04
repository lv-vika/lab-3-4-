from models import *
from manager import *


def main ():
    a = AirFreshener("Allure sport", 139, 10, "Dope", "strawberry")
    b = Oil("oil1", 300, 25, "brand1", 10, 400)
    c = AirFreshener("AirWick", 101, 34, "Lemon Flower", 250)
    d = WindshieldWasher (c )

    objects = [a, b, c, d]
    manager_object = CarChemistryStoreManager(objects)

    out1 = manager_object.sort_by_price(False)
    print("sorted by price")
    for i in out1:
        print(i)

