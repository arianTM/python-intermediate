# Sets: unordered, mutable, no duplicates
my_set = {1, 2, 3, 1, 2}
print(my_set)

# ------------ Built-in 'set' constructor ------------
my_set = set("Hello")
print(my_set)

# ------------ Empty set ------------
my_set = set()  # mySet = {} creates a dict
print(type(my_set))

# ------------ Add items ------------
print(my_set)  # Empty set
my_set.add(1)
my_set.add(2)
my_set.add(3)
print(my_set)

# ------------ Remove items ------------

my_set.remove(3)
# mySet.remove(4) # KeyError

print(my_set)

my_set.discard(4)  # Same as remove but no error

print(my_set.pop())

print(my_set)

# ------------ Clear set ------------
my_set.clear()
print(my_set)

# ------------ Iterate through a set ------------
my_set = {1, 2, 3, 4, 5}
for i in my_set:
    print(i)

# ------------ Check item's existence in a set ------------
if 1 in my_set:
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
