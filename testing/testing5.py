import unittest


class Address():
    def __init__(self, city, state):
        self.city=city
        self.state=state


class Owner():
    def __init__(self, name, age):
        self.name=name
        self.age=age


class Restaurant():
    def __init__(self, address, ower):
        self.address=address
        self.ower=ower

    @property
    def owner_age(self):
        return self.ower.age

    def summary(self):
        return f'This restaurant is owner by {self.ower.name}, located in {self.address.city}.'


#tests
class TestRestaurant(unittest.TestCase):
    def setUp():
        address=Address(city='Bucharest', state='Romania')
        owner=Owner(name='Stefan', age=35)
        self.restaurant=Restaurant(address, ower)

    def tearDown():
        address=None
        ower=None
        self.restaurant=None

    def test_owner_age(self):
        self.assertEqual(self.restaurant.ower.age, 35)



if __name__=='__main__':
    unittest.main()