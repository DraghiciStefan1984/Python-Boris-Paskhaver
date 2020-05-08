food={'rice': 9.99, 'chicken':12.55, 'fries':5, 'pork':7.5}

for key in food:
    print(key)

for value in food.values():
    print(value)

for key, value in food.items():
    print(key, value)

print('rice' in food.keys())

print(sorted(food))
print(sorted(food.values()))

concert_attendees=[
    {'name':'Maria', 'section':50, 'price':45.55},
    {'name':'Vlad', 'section':41, 'price':55.55},
    {'name':'Cristi', 'section':20, 'price':35.55},
]

for atendee in concert_attendees:
    for key, value in atendee.items():
        print(f'The {key} is {value}.')