stocks={'MSFT', 'AAPL', 'GOOG', 'AAPL', 'IBM', 'FB', 'IBM'}

print(stocks)

s=set([4,5,6,4,5,6,5,4])
print(s)

print(set({'unu': 1, 'doi':2}))
print(set('dfsghjfds'))

s.add(('dsa', 32))
print(s)

s.update((32, 56, 67), ['sd', '34'])
print(s)

# print(s.remove(2))
print(s.discard(3))