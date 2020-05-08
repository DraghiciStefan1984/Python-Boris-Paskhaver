n={1,2,3,4,5}
m={4,5,6,7,8,9}
p={1,2,3,4,5,6,7,8,9}

print('intersection1: ',n.intersection(m))
print('intersection2: ',n&m)

print('difference1: ',n.difference(m))
print('difference2: ',n-m)

print('union1: ',n.union(m))    
print('union2: ',n|m)

print('symmetric_diff1: ',n.symmetric_difference(m))    
print('symmetric_diff2: ',n^m)

print(n.issubset(m))
print(n.issubset(p))