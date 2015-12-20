"""Data Structures in python3"""

import array

# Build a list of Unicode codepoints from a string

symbols = '$¢£¥€¤'

codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

# with list comprehension a.k.a listcomps with are meant to build a list
codes = [ord(symbol) for symbol in symbols]

print(codes)

# map and filter vs listcomps

beyond_ascii = [ord(s) for s in symbols if ord(s) > 200]  # using a list comps
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 200, map(ord, symbols)))  # using map and filter
print(beyond_ascii)

# Cartesian product using a list comprehension
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

# Initializing a tuple and an array from a generator expression
print(tuple(ord(symbol) for symbol in symbols))
print(array.array('I', (ord(symbol) for symbol in symbols)))

# Cartesian product in a generator expression
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

# Tuples used as records
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
travel_ids = [('USA', '3E4278919'), ('Brazil', 'S82384949'), ('ESP', 'E1291947')]
for passpost in sorted(travel_ids):
    print('%s/%s' % passpost)
