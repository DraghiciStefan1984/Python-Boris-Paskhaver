
def be_nice(fn):
    def inner(*args, **kwargs):
        print('I will execute you func.')
        fn(*args, **kwargs)
        print('I executed your func.')
    return inner

def be_nice_2(fn):
    def inner(*args, **kwargs):
        print('I will execute you func.')
        result=fn(*args, **kwargs)
        print('I executed your func.')
        return result
    return inner

@be_nice
def complex_func():
    print('some complex shit...')


@be_nice
def complex_func2(stakeholder):
    print(f'some complex shit for {stakeholder}...')


@be_nice_2
def complex_sum(a, b):
    return a+b


# print(be_nice(complex_func))
# result=be_nice(complex_func)
# result()
# be_nice(complex_func)()

complex_func()
complex_func2('Stefan')
complex_sum(32, 55)