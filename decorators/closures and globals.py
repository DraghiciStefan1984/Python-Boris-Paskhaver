def outer():
    candy='snickers'

    def inner():
        return candy

    # return inner()
    return inner


print(outer())
func=outer()
print(func())


x=10

def change():
    global x
    x=20

print(x)
change()
print(x)


def outer():
    tea='black'
    def inner():
        nonlocal tea
        tea='green'
    inner()
    return tea

print(outer())