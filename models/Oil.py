from models import ChemistryItem, ChemistryType


class Oil(ChemistryItem):
    def __init__(self, name, price, balance_in_stock, brand, viscosity, flash_point):
        super().__init__(ChemistryType.UNDERTHEHOOD, name, price, balance_in_stock, brand)
        self.__viscosity = viscosity
        self.__flash_point = flash_point

    def __str__(self):
        return f"name: {self._name}\n" \
               f"price: {self._price}\n" \
               f"balance_in_stock: {self._balance_in_stock}\n" \
               f"brand: {self._brand}\n" \
               f"viscosity: {self.__viscosity}\n" \
               f"flash_point: {self.__flash_point}\n"

    def get_viscosity(self):
        return self.__viscosity

    def get_flash_point(self):
        return self.__flash_point
