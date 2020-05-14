class Card:
    def __init__(self, rank, suit):
        self.rank=rank
        self.suit=suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def __repr__(self):
        return f'Card({self.rank}, {self.suit})'

    def __eq__(self, other):
        return self.rank==other.rank and self.suit==other.suit


c1=Card('Ace', 'Spades')
print(c1)
print(repr(c1))
c2=Card('Queen', 'Clubs')
c3=Card('Ace', 'Spades')
print(c1==c2)
print(c1==c3)



class Person:
    def __init__(self, age, height):
        self.age=age
        self.height=height

    def __gt__(self, other):
        return self.age>other.age and self.height>other.height


p1=Person(34, 177)
p2=Person(14, 123)
print(p1>p2)