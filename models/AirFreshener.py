from models import CarChemistryItem, ChemistryType


class AirFreshener(CarChemistryItem):
    def __init__(self, name, price, balance_in_stock, brand, flavor):
        super().__init__(ChemistryType.INTERIOR, name, price, balance_in_stock, brand)
        self.__flavor = flavor

    def __str__(self):
        return f"name: {self.name}\n" \
               f"price: {self.price}\n" \
               f"balance_in_stock: {self.balance_in_stock}\n" \
               f"brand: {self.brand}\n" \
               f"flavor: {self.__flavor}\n" \
