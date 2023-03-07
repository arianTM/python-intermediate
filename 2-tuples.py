# Tuples: ordered, inmutable, allows duplicate elements
import sys
import timeit
my_tuple = ("Max", 28, "Boston")
my_tuple = "Max", 28, "Boston"  # Parenthesis are optional
print(my_tuple)

# ---- Handle one element in tuples ----
my_tuple = ("Max")  # Non tuple
print(type(my_tuple))
my_tuple = ("Max",)  # Tuple
print(type(my_tuple))

# ---- Built-in 'tuple' constructor ----
my_tuple = tuple(["Max", 28, "Boston"])
print(my_tuple)

# ---- Accessing elements ----
item = my_tuple[0]  # First item
item = my_tuple[1]  # Second item
item = my_tuple[2]  # Third item
# item = myTuple[3]  # IndexError
item = my_tuple[-1]  # Last item
print(item)

# ---- Changing elements ----
# myTuple[0] = "Tim"  # TypeError

# ---- Iterate over a tuple ----
for i in my_tuple:
    print(f"{i} --> Keep iterating")

if "Max" in my_tuple:
    print("Max is in tuple")
else:
    print("Max is not in tuple")

# ---- Length of a tuple ----
my_tuple = ('a', 'p', 'p', 'l', 'e')
print(len(my_tuple))

# ---- Count item in a tuple ----
print(my_tuple.count("p"))

# ---- Index of item in a tuple ----
print(my_tuple.index("l"))

# ---- Cast a tuple into a list ----
my_list = list(my_tuple)
print(my_list)

# ---- Cast a list into a tuple ----
my_tuple2 = tuple(my_list)
print(my_tuple2)

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
my_tuple = "Max", 28, "Boston"
# Unpacking (number of variables should equal tuple length)
name, age, city = my_tuple
print(name)
print(age)
print(city)

my_tuple = tuple(range(5))
i1, *i2, i3 = my_tuple
print(i1)
print(i2)
print(i3)

# -----------------------------------
# Tuples are more efficient that lists, but cannot changes its elements
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list, "bytes"))
print(sys.getsizeof(my_tuple, "bytes"))

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
# -----------------------------------
