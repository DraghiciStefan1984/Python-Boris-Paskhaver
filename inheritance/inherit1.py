class Store:
    def __init__(self):
        self.owner='Stefan'

    def exclaim(self):
        return 'Come and buy stuff!'


class CoffeeShop(Store):
    def sell_coffee(self):
        return 'here is your coffee'

    def exclaim(self):
        return 'welcome to the coffe shop'


c=CoffeeShop()
print(c.owner)
print(c.exclaim())
print(c.sell_coffee())



class Animal:
    def __init__(self, name):
        self.name=name

    def eat(self, food):
        return f'{self.name} is enjoying the {food}.'


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed
    pass


d=Dog('Bobby', 'dweeb')
print(d.eat('bone'))