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