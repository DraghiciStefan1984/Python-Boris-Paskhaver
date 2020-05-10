import functools

def be_nice(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        print('I will execute you func.')
        fn(*args, **kwargs)
        print('I executed your func.')
    return inner


@be_nice
def complex_func2(stakeholder):
    print(f'some complex shit for {stakeholder}...')

complex_func2('Bogdan')

help(complex_func2)