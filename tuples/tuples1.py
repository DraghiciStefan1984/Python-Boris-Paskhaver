foods=('cartofi prajiti', 'copane', 'ou')
print(type(foods))

numbers=tuple([23, 12, 78])
letters1=tuple('abcd')
print(letters1)

letters2=(['abvahgsd'])
print(letters2)

birthday=(4, 10, 1984)
print(len(birthday))
print(birthday[1])
# birthday[1]=20
# print(birthday)

addresses=(['Bucuresti', 'Racovita', 6], ['Brasov', 'Sforii', 1])
addresses[0][1]='Baia de arama'
addresses[0][2]=1
print(addresses)


employee=('Stefan', 'Radu', 'Manager', 35)
employee_list=[*employee]
print(employee_list)

name1, name2, position, age=employee
print(name1, position)

first_name, last_name, *other_info=employee
print(first_name, last_name, other_info)

name, *other, age=employee
print(name, other, age)


a=10
b=8
a, b=b, a
print(a, b)