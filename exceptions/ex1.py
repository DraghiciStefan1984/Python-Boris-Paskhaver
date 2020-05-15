def divide(n):
    try:
        calculation=5/n
    except:
        calculation=5
    return calculation


def divide_2(n):
    try:
        return 5/n
    except:
        pass


def divide_3(n):
    try:
        return 5/n
    except ZeroDivisionError:
        return 'zero division error'  


print(divide(0))
print(divide(8))
print(divide_2(0))
print(divide_2(8))
print(divide_3(0))
print(divide_3(8))