class Parent:
    def __init__(self):
        self.__private_attribute=None

    def __private_method(self):
        print('private method from parent')



class Child:
    pass


c=Child()
#c._Parent__private_method()

##########################################################

class FrozenFood:
    def thaw(self, minutes):
        print(f'Thawing for {minutes} minutes.')

    def store(self):
        print('put in freezer.')


class Dessert:
    def add_weight(self):
        print('putting on weight...')

    def store(self):
        print('put in refrigerator.')


class IceCream(FrozenFood, Dessert):
    pass

i=IceCream()
i.thaw(10)
i.add_weight()
i.store()
print(IceCream.mro())