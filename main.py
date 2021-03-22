from models import *
from manager import *


def main():
    a = AirFreshener("Allure sport", 139, 25, "Dope", "strawberry")
    b = Oil("oil1", 300, 10, "brand1", 10, 400)
    c = AirFreshener("AirWick", 101, 200, "Lemon Flower", 250)
    d = WindshieldWasher("Prestone", 520, 34, "Washer Fluid", 70, -32)

    objects = [a, b, c, d]
    manager_object = CarChemistryStoreManager(objects)

    out1 = manager_object.sort_by_price(False)
    print("sorted by price\n")  # [c, a, b, d]
    for i in out1:
        print(i)

    out2 = manager_object.sort_by_balance(False)  # [b a d c]
    print("sorted by balance\n")
    for i in out2:
        print(i)

    out3 = manager_object.search_by_name("oil1")
    print("searched by name\n")
    for i in out3:
        print(i)


if __name__ == "__main__":
    main()
