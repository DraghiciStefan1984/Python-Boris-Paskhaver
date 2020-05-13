class SushiPlatter:
    def __init__(self, salmon, tuna, shrimp, squid):
        self.salmon=salmon
        self.tuna=tuna
        self.shrimp=shrimp
        self.squid=squid

    @classmethod
    def lunch_special_A(cls):
        return cls(salmon=20, tuna=0, shrimp=20, squid=0)

    @classmethod
    def tuna_lover(cls):
        return cls(salmon=0, tuna=100, shrimp=20, squid=0)


sushi=SushiPlatter(salmon=10, tuna=8, shrimp=5, squid=13)
lunch=SushiPlatter.lunch_special_A()
print(lunch.salmon)
print(lunch.tuna)
print(lunch.shrimp)
print(lunch.squid)

tuna=SushiPlatter.tuna_lover()
print(tuna.tuna)



class Counter():
    count=0
    def __init__(self):
        Counter.count+=1

c1=Counter()
c2=Counter()
c3=Counter()
c4=Counter()
print(c1.count)
print(c3.count)



class WeatherForecast:
    def __init__(self, temperatures):
        self.temperatures=temperatures

    @staticmethod
    def convert_from_fahrenheit_to_celsius(fahr):
        return round((5/9)*(fahr-32), 2)

    def in_celsius(self):
        return [self.convert_from_fahrenheit_to_celsius(temp) for temp in self.temperatures]