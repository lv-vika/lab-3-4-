from enum import Enum


class ChemistryType(Enum):
    INTERIOR = 0
    EXTERIOR = 1
    UNDERTHEHOOD = 2


class ChemistryItem:
    def __init__(self, type_of_object, name, price, balance_in_stock, brand):
        self._type_of_object = type_of_object
        self._name = name
        self._price = price
        self._balance_in_stock = balance_in_stock
        self._brand = brand

    def __str__(self):
        return f"name: {self._name}\n"\
               f"price: {self._price}\n"\
               f"balance_in_stock: {self._balance_in_stock}\n"\
               f"brand: {self._brand}\n"

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_balance(self):
        return self._balance_in_stock

    def get_brand(self):
        return self._brand
