ice_cream={'Stefan':'ciocolata', 'Gabi':'fructe', 'Bogdan':'vanilie'}

print(len(ice_cream))

nums={'unu':1, 'doi':2, 'trei':3, 'patru':4, 'cinci':5}
print(nums['unu'])

# if this key does not exist, it will return a default value
print(nums.get('sase', 6))

employees={'devs': ['Stefan', 'Bogdan', 'Ana', 'Andrei'],
            'managers': ['Gabi', 'Victor'],
            'qa': ['Maria', 'Vlad'],
            'sales': ['Monica', 'Andrei']}

#adding a key to a dict
employees['human resources']=['Simona', 'Claudiu']
print(employees['managers'])

employees['devs'][1]='Vali'
print(employees['devs'])