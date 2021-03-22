from models import ChemistryItem, ChemistryType


class AirFreshener(ChemistryItem):
    def __init__(self, name, price, balance_in_stock, brand, flavor):
        super().__init__(ChemistryType.INTERIOR, name, price, balance_in_stock, brand)
        self.__flavor = flavor

    def __str__(self):
        return f"name: {self._name}\n" \
               f"price: {self._price}\n" \
               f"balance_in_stock: {self._balance_in_stock}\n" \
               f"brand: {self._brand}\n" \
               f"flavor: {self.__flavor}\n"

    def get_flavor(self):
        return self.__flavor
