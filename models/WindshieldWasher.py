from models import CarChemistryItem, ChemistryType


class WindshieldWasher(CarChemistryItem):
    def __init__(self, name, price, balance_in_stock, brand, alcohol_content, freezing_point):
        super().__init__(ChemistryType.UNDERTHEHOOD, name, price, balance_in_stock, brand)
        self.__viscosity = alcohol_content
        self.__freezing_point = freezing_point

    def __str__(self):
        return f"name: {self._name}\n" \
               f"price: {self._price}\n" \
               f"balance_in_stock: {self._balance_in_stock}\n" \
               f"brand: {self._brand}\n" \
               f"alcohol_content: {self.__alcohol_content}\n" \
               f"freezing_point: {self.__freezing_point}\n"
