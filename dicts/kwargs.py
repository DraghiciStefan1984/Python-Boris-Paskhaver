def collect_arguments(a, b):
    print(a, b)


def collect_arguments_and_args(a, b, *args):
    print(a, b, args)

def collect_args(*args):
    print(args)


def collect_kwargs(**kwargs):
    print(kwargs)


def args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


collect_arguments(23, 90)
collect_arguments_and_args(23, 56, 76, 45, 22, 67)
collect_args(1, 2, 4, 6, 'sdas')
collect_kwargs(a=1, b=2, c=2)
args_and_kwargs(7, 8, 9, 10, 'sdas', a=10, b=20, c=20)


def height_to_meters(feet, inches):
    total_inches=(feet*12)+inches
    return total_inches*0.0254

stats={'feet':5, 'inches':11}
print(height_to_meters(5, 11))
print(height_to_meters(**stats))