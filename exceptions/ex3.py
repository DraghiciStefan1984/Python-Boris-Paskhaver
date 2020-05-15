x=10

try:
    print(x+3)
except NameError:
    print('x is not defined')
else:
    print('this is printed if there is no error')
finally:
    print('this will always be printed')