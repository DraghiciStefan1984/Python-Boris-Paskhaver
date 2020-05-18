from datetime import date, time, datetime

d=date(2020, 5, 15)
print(d)

start=datetime.now()
for i in range(1000):
    print(i)
end=datetime.now()
print((end-start).seconds)

print(datetime(2020, 1, 1))

today=datetime.today()
print(today.strftime('%d'))
print(today.strftime('%d-%m'))
print(today.strftime('%d/%m/%y'))
print(today.strftime('%d/%m/%Y'))
print(today.strftime('%d/%m/%Y'))
print(today.strftime('%A'))
print(today.strftime('%A-%B'))
print(today.strftime('%A/%B/%C'))

birthday=datetime(1984, 4, 10)
today=datetime.now()
life_span=today-birthday
print(life_span)