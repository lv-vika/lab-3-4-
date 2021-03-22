class CarChemistryStoreManager:

    def __init__(self, chemistry=list):
        self.__chemistry = chemistry

    def sort_by_price(self, order):
        self.__chemistry.sort(key=lambda n: n.get_price(), reverse=order)
        return self.__chemistry

    def sort_by_balance(self, order):
        self.__chemistry.sort(key=lambda n: n.get_balance(), reverse=order)
        return self.__chemistry

    def search_by_name(self, name):
        out = list()
        for i in self.__chemistry:
            if i.get_name() == name:
                out.append(i)
        return out
