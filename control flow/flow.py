if 5>3:
    print('Yes...')

def positive_or_negative(num):
    if num>0:
        return 'positive'
    elif num<0:
        return 'negative'
    else:
        return 'zero'

zip_code="abc123"
check="Valid" if len(zip_code)==5 else "Invalid"
print(check)

if 5<10 and "good"=="good":
    print("a")
else:
    print("b")

value=55
if 10<value<100:
    print(value)


count=0
while count<10:
    print(count)
    count+=1