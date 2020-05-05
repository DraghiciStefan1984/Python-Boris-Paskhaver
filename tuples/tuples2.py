def accept(*args):
    print(type(args))
    print(args)

accept('abs')
accept(1,2,3,4,5,6)
accept([7,84,651])


def custom_max_num(*numbers):
    greatest=numbers[0]
    for number in numbers:
        if number>greatest:
            greatest=number
    return greatest

print(custom_max_num(78))
print(custom_max_num(78,22, 89, 56, 10, 111, 78, 56, 186))


def product(a, b):
    return a*b

nums1=[45, 78]
nums2=(56, 12)

print(product(*nums1))
print(product(*nums2))