from unittest.mock import Mock

pizza=Mock()
print(pizza)
print(type(pizza))

pizza.size='large'
pizza.price=15
pizza.toppings=['pepperoni', 'mushroom']

print(pizza.size)