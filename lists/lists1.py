l1=[]
l2=list()

body_parts=['head', 'torso', 'arms', 'legs']

print(body_parts[0][::-1])

nums=[7,8,4,6,5,1,2,1]

for num in nums:
    print(num**2)

for part in body_parts:
    print(part[::-1])
print(body_parts)


tasks=['eat', 'sleep', 'code', 'repeat', 'take care of family', 'have fun']

print(enumerate(tasks))

for index, task_at_index in enumerate(tasks):
    print(index, task_at_index)


def contains(values, target):
    found=False
    for value in values:
        if target==value:
            found=True
            break
    return found


def sum_positive_nums(values):
    total=0
    for value in values:
        if value>0:
            continue
        total+=value
    return total