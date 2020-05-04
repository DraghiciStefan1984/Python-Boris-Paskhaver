metals=['gold', 'silver', 'platinum', 'iron', 'chrome']
empty=[]
l1=['unu', 'doi', '']
l2=['unu', 'doi', None]
nums=[4,9,8,65,13,20,48,65,3,1]

print(list(filter(lambda metal: len(metal)<5, metals)))
print(list(filter(lambda metal: 'p' in metal, metals)))

#all returns bool if all elems from a list are truthy or falsy
print(all(metals))
print(all([]))
print(all(l1))
print(all(l2))

#all returns bool if any elem from a list is truthy or falsy
print(any(metals))
print(any([]))
print(any(l1))
print(any(l2))

#other
print(max(nums))
print(min(nums))
print(sum(nums))


#dir returns a list of all available methods of an objects
print('\n\n')
print(dir(list))
print('\n\n')
print(dir(set))
print('\n\n')
print(dir(dict))
print('\n\n')
print(dir(object))
print('\n\n')
print(dir(None))

#format will return a str representation of a number
number=3.14588666
print(format(number,'.2f'))
print(format(0.5, '%'))
