class CarChemistryStoreManager:
    def __init__(self, chemistry=list):
        self.__chemistry = chemistry

    def sort_by_price(self, order):
        self.__chemistry.sort(key=lambda n: n._price, reverse=order)
        return self.__chemistry
