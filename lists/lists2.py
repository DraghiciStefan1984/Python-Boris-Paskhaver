letters=['f','g','d','h','f','j','h','f','g','d','f']
print(letters)
letters[3:6]=['a']
print(letters)
letters=['f','g','d','h','f','j','h','f','g','d','f']
letters[3:6]=['a','a','a','a','a']
print(letters)

print([1,3,2]+[7,9,8]+[8,9,4])
print([78,46]+[89])

numbers=[1,2,3,4,6,5,7,8,9]
squares=[]
for number in numbers:
    squares.append(number**2)
print(squares)

numbers.append([8,4,5,1,6])
print(numbers)

numbers=[1,2,3,4,6,5,7,8,9]
numbers.extend([7,8,9,4,6,5,1,3])
print(numbers)
numbers.insert(7,888)
print(numbers)
print(numbers.pop())
print(numbers)
del numbers[-10:-15]
print(numbers)
numbers.remove(8)
print(numbers)
print(numbers.count(1))
print(numbers)
numbers.reverse()
print(numbers)
numbers.clear()
print(numbers)
print(numbers.count(1))