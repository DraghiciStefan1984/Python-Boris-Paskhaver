def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def calculate(func, a, b):
    return func(a, b)

print(calculate(subtract, 12, 8))
print(calculate(add, 32, 15))


def gallons_to_cups(gallons):
    def gallons_to_quarts(gallons):
        print(f'converting {gallons} to quarts!')
        return gallons*4
    def quarts_to_pints(quarts):
        print(f'converting {quarts} to pints!')
        return quarts*2
    def pints_to_cups(pints):
        print(f'converting {pints} to cups!')
        return pints*2
    quarts=gallons_to_quarts(gallons)
    pints=quarts_to_pints(quarts)
    cups=pints_to_cups(pints)
    return cups

print(gallons_to_cups(12))