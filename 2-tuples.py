# Tuples: ordered, inmutable, allows duplicate elements
import sys
import timeit
myTuple = ("Max", 28, "Boston")
myTuple = "Max", 28, "Boston"  # Parenthesis are optional
print(myTuple)

# ---- Handle one element in tuples ----
myTuple = ("Max")  # Non tuple
print(type(myTuple))
myTuple = ("Max",)  # Tuple
print(type(myTuple))

# ---- Built-in 'tuple' constructor ----
myTuple = tuple(["Max", 28, "Boston"])
print(myTuple)

# ---- Accessing elements ----
item = myTuple[0]  # First item
item = myTuple[1]  # Second item
item = myTuple[2]  # Third item
# item = myTuple[3]  # IndexError
item = myTuple[-1]  # Last item
print(item)

# ---- Changing elements ----
# myTuple[0] = "Tim"  # TypeError

# ---- Iterate over a tuple ----
for i in myTuple:
    print(f"{i} --> Keep iterating")

if "Max" in myTuple:
    print("Max is in tuple")
else:
    print("Max is not in tuple")

# ---- Length of a tuple ----
myTuple = ('a', 'p', 'p', 'l', 'e')
print(len(myTuple))

# ---- Count item in a tuple ----
print(myTuple.count("p"))

# ---- Index of item in a tuple ----
print(myTuple.index("l"))

# ---- Cast a tuple into a list ----
myList = list(myTuple)
print(myList)

# ---- Cast a list into a tuple ----
myTuple2 = tuple(myList)
print(myTuple2)

# ---- Slicing ----
a = tuple(range(1, 11))
b = a[2:5]  # Slices from indeces 2 to 5, excluding 5
print(b)
b = a[:5]  # Slices from indeces 0 to 5, excluding 5
print(b)
b = a[2:]  # Slices from index 2 to last index
print(b)
b = a[::2]   # Slices from index 0 to last index, in step of 2
print(b)
b = a[::-1]  # Slices from last index to index 0
print(b)

# ---- Unpacking ----
myTuple = "Max", 28, "Boston"
# Unpacking (number of variables should equal tuple length)
name, age, city = myTuple
print(name)
print(age)
print(city)

myTuple = tuple(range(5))
i1, *i2, i3 = myTuple
print(i1)
print(i2)
print(i3)

# -----------------------------------
# Tuples are more efficient that lists, but cannot changes its elements
myList = [0, 1, 2, "hello", True]
myTuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(myList, "bytes"))
print(sys.getsizeof(myTuple, "bytes"))

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
# -----------------------------------
