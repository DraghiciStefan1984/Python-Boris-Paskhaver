# def countdown_from(num):
#     start=num
#     while num>0:
#         print(start)
#         start-=1

def countdown_from(num):
    if num<=0:
        return
    print(num)
    return countdown_from(num-1)


def reverse(s):
    if len(s)==1:
        return s
    return s[-1]+reverse(s[:-1])

countdown_from(10)
print(reverse('abcd'))