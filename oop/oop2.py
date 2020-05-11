class Pokemon:
    def __init__(self, name, specialty, health=100):
        self.name=name
        self.specialty=specialty
        self.health=health

    def roar(self):
        print('Roaaaar!')

    def describe(self):
        print(f'I am {self.name}. I am a {self.specialty} Pokemon!')

    def take_damage(self, amount):
        self.health-=amount


squirtle=Pokemon('Squirtle', 'water')
charmander=Pokemon(name='Charmander', specialty='fire', health=110)
squirtle.roar()
charmander.roar()
squirtle.describe()
charmander.describe()


class SmartPhone:
    def __init__(self):
        self._company='Apple'
        self._firmware=10.0

    def get_os(self):
        return self._firmware

    def update_firmware(self):
        print('updating version')
        self._firmware+=1


iphone=SmartPhone()
print(iphone.get_os())
iphone.update_firmware()
print(iphone._firmware)