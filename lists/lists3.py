l1=[7,8,4,5,6,1,3,2,4,6,5,3,1]
l2=l1.copy()
print(hex(id(l1)))
print(hex(id(l2)))

l3=[[6,5,1], ['a','s','d']]
l4=l3.copy()
print(l4)
print(hex(id(l3)))
print(hex(id(l4)))

s='Stefan, Bogdan, Gabi, Mama, Tata'
print(s.split(', '))
print('-'.join(['1','2','3']))

a1=[7,8,4,6,5,1,3,2]
a2=['d','r','t','f','g','j','h','k']
a3=[0,4,9,5,2,9,3,2]
z=zip(a1, a2, a3)
print(list(z))
for item in z:
    print(item)