print(help(print))

nums=[7,8,4,5,1,2,5,6,2,3,5,6]
animals=['cat', 'dog', 'lion', 'bear', 'mouse', 'elephant', 'giraffe', 'aligator']

#map applies a function to every element in a list
#more efficient than a list comprehension

def cube(i):
    return i**3

cubes=map(cube, nums)
print(list(cubes))
print(list(map(len, animals)))

squares=list(map(lambda x: x**2, [1,2,3,4,6,5,7,8,9]))
print(squares)

#filter applies a fnction that returns a bool to a every element in a list
long_word_animals=[animal for animal in animals if len(animal)>5]
print(long_word_animals)

def is_animal_name_long(animal):
    return len(animal)>5

print(list(filter(is_animal_name_long, animals)))