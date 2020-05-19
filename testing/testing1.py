def add(x, y):
    assert isinstance(x, int) and isinstance(y, int)
    return x+y

print(add(3, 5))
# print(add(3, '5'))


def sum_of_list(numbers):
    """
    return the sum of numbers in a list:
    >>>sum_of_list([1,2,3])
    6
    >>>sum_of_list([5,8,13])
    26
    """
    total=0
    for number in numbers:
        total+=number
    return total

if __name__=='__main__':
    import doctest
    doctest.testmod()