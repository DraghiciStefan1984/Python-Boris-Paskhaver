def add(a=0, b=0):
    return a+b

def strict(s: str, i: int):
    return s*i

def strict_return(s: list, i: int)->list:
    return s*i


#test
print(add())
print(add(32, 89))
print(add(a=89, b=65))
print(strict('abc', 3))
print(strict_return([2,3,8], 5))