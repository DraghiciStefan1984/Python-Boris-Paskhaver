def add_positive_numbers(a, b):
    try:
        if a<=0 or b<=0:
            raise ValueError('both numbers must be positive')
        return a+b
    except ValueError as e:
        return f'caught value error: {e}'


print(add_positive_numbers(34, 23))
print(add_positive_numbers(-34, 23))



class NegativeNumbersError(Exception):
    pass


def add_positive_numbers_2(a, b):
    try:
        if a<=0 or b<=0:
            raise NegativeNumbersError('both numbers must be positive')
        return a+b
    except NegativeNumbersError as e:
        return f'caught negative numbers error: {e}'

print(add_positive_numbers_2(34, 23))
print(add_positive_numbers_2(-34, 23))