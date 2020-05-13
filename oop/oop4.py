stats={'name': 'bbq chicken', 'price':20, 'size':'extra large', 'ingredients': ['chicken', 'sauce', 'cheese', 'vegetables']}

class Pizza:
    def __init__(self, stats):
        for key, value in stats.items():
            setattr(self, key, value)


pizza=Pizza(stats)
print(pizza.name)
print(pizza.price)
print(pizza.ingredients)
print(getattr(pizza, 'size'))
print(getattr(pizza, 'ingredients'))

print()

for attr in ['name', 'price', 'size', 'ingredients', 'diameter']:
    print(getattr(pizza, attr, 'placeholder'))

print(hasattr(pizza, 'name'))

attrs_to_delete=['name', 'price']
for attr in attrs_to_delete:
    if hasattr(pizza, attr):
        delattr(pizza, attr)
print(pizza.__dict__)