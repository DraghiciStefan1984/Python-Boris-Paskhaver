import collections


Book=collections.namedtuple('Book', ['title', 'author'])
art_of_war=Book('Art of war', 'Sun Tsu')
inteligent_investor=Book('Inteligent investor', 'Ben Graham')


class Library:
    def __init__(self, *books):
        self.books=books
        self.librarians=[]

    def __len__(self):
        return len(self.books)


l1=Library(art_of_war)
print(len(l1))

l2=Library(art_of_war, inteligent_investor)
print(len(l2))



class CrayonBox:
    def __init__(self):
        self.crayons=[]

    def add(self, crayon):
        self.crayons.append(crayon)

    def __getitem__(self, index):
        return self.crayons[index]

    def __setitem__(self, index, value):
        self.crayons[index]=value


c=CrayonBox()
c.add('blue')
c.add('yellow')
c.add('red')
print(c[0])
c[1]='white'
print(c[1])