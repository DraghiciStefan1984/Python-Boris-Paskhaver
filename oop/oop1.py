class Guitar:
    def __init__(self, wood=None, year=None):
        print(f'a {self} has been created...')
        self.wood=wood
        self.year=year


g=Guitar()
print(g)