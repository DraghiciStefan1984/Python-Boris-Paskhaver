creator='Stefan'
PI=3.14

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def area(radius):
    return PI*radius*radius

print(add(10, 18))

if __name__=='__main__':
    print('only run as calculator is executed as a script')