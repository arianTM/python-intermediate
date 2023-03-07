# Sets: unordered, mutable, no duplicates
mySet = {1, 2, 3, 1, 2}
print(mySet)

# ------------ Built-in 'set' constructor ------------
mySet = set("Hello")
print(mySet)

# ------------ Empty set ------------
mySet = set()  # mySet = {} creates a dict
print(type(mySet))

# ------------ Add items ------------
print(mySet)  # Empty set
mySet.add(1)
mySet.add(2)
mySet.add(3)
print(mySet)

# ------------ Remove items ------------

mySet.remove(3)
# mySet.remove(4) # KeyError

print(mySet)

mySet.discard(4)  # Same as remove but no error

print(mySet.pop())

print(mySet)

# ------------ Clear set ------------
mySet.clear()
print(mySet)

# ------------ Iterate through a set ------------
mySet = {1, 2, 3, 4, 5}
for i in mySet:
    print(i)

# ------------ Check item's existence in a set ------------
if 1 in mySet:
    print("1 in set")
else:
    print("1 not in set")

# ------------ Union & Intersection ------------
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

# ------------ Difference ------------
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
diff = setA.difference(setB)
print(diff)

# ------------ Symmetric Difference ------------
diff = setA.symmetric_difference(setB)
print(diff)

# ------------ Union and update ------------
# setA.update(setB)
print(setA)

# ------------ Intersection and update ------------
# setA.intersection_update(setB)
print(setA)

# ------------ Difference and update ------------
# setA.difference_update(setB)
print(setA)

# ------------ Symmetric difference and update ------------
setA.symmetric_difference_update(setB)
print(setA)

# ------------ Subset ------------
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setA.issubset(setB))
print(setB.issubset(setA))

# ------------ Superset ------------
print(setA.issuperset(setB))
print(setB.issuperset(setA))

# ------------ Disjoint ------------
print(setA.isdisjoint(setB))
setC = {7, 8}
print(setA.isdisjoint(setC))

# ------------ Copy sets ------------
setA = {1, 2, 3, 4, 5, 6}
setB = setA  # Shallow copy
setB = setA.copy()  # Deep copy
setB = set(setA)  # Deep copy
setB.add(7)
print(setA)
print(setB)

# ------------ Frozen (inmutable) set ------------
a = frozenset([1, 2, 3, 4])
print(a)
# a.add(2) # AttributeError
