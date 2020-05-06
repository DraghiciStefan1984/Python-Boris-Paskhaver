from copy import deepcopy


a=3
print(hex(id(a)))
a=[12,12]
print(hex(id(a)))
a='fdss'
print(hex(id(a)))

x=3
y=x
print(hex(id(x)))
print(hex(id(y)))

students1=['Ana', 'Emil', 'Radu']
students2=['Ana', 'Emil', 'Radu']
athletes=students1
print(hex(id(students1)))
print(hex(id(students2)))
print(hex(id(athletes)))

#check if the memory address of students is the same with athletes
print(students1 is athletes)
#check if the values of students are the same with athletes
print(students1 == athletes)

print(students1 is students2)
print(students1 == students2)

a='hello'
b='hello'
print(a is b)
print(a == b)


l1=[1,2,3]
l2=l1[:]
l3=[1,2,3]
print(hex(id(l1)))
print(hex(id(l2)))
print(hex(id(l3)))
print(l1 is l2)
print(l1 == l2)
print(l1 is l3)
print(l1 == l3)

l4=l1.copy()
print(hex(id(l1)))
print(hex(id(l4)))
print(l1 is l4)
print(l1 == l4)

l5=deepcopy(l1)
print(hex(id(l1)))
print(hex(id(l5)))
print(l1 is l5)
print(l1 == l5)