# Lists: ordered, mutable, allows duplicate elements
my_list = ["banana", "cherry", "apple"]
print(my_list)

# Allows more than one data type
# myList2 = list()
my_list2 = [5, True, "apple"]
print(my_list2)

# Access with index
item = my_list[0]  # First element
item = my_list[1]  # Second element
item = my_list[2]  # Third element
item = my_list[-1]  # Last element

# Iterate over a list
for i in my_list:
    print(i)

# Check item's existence in a list
if "banana" in my_list:
    print("yes")
else:
    print("no")

# List length
print(len(my_list))

# Append element in a list
my_list.append("lemon")
print(my_list)

# Insert element in a list at a specific index
my_list.insert(1, "blueberry")  # At index 1, insert "blueberry"
print(my_list)

# Remove last element and return it in a list
item = my_list.pop()
print(f"Last item removed: {item}")
print(my_list)

# Popping an empty list will give an IndexError

# Remove a specific element
my_list.remove("cherry")  # .remove returns None
print("Item removed: cherry")
print(my_list)

# Clear list
example = [1, True, "asd"]
example.clear()
print(example)

# Reverse list
num_list = [5, 3, 7]
print(num_list)
num_list.reverse()
print(num_list)

# Sort list
num_list.sort()
print(num_list)

# Return a copy of sorted list (without changing the original list)
ordered = sorted(my_list)
print(my_list)
print(ordered)

# Multiply a list
five_zeros = [0] * 5
print(five_zeros)

# Concatenate two or more lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
new_list = list1 + list2 + list3
print(new_list)

# ---------- Slicing ----------
my_list = list(range(1, 10))
sliced = my_list[1:3]  # Includes index 1, excludes index 3
print(sliced)
sliced = my_list[:3]  # From index 0 to index 3, excluding 3
print(sliced)
sliced = my_list[1:]  # From index 1 to last index
print(sliced)
# From index 1 to index 7, excluding index 7, with step 2
sliced = my_list[1:7:2]
print(sliced)
# From index 7 to index 1, excluding index 7, with step 2
sliced = my_list[1:7:-2]

# ------------ Copying lists ------------
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org  # Shallow copy
list_cpy.append("lemon")
print(list_org)
print(list_cpy)

list_cpy = list_org.copy()  # Deep copy
# ------ Alternatives ------
list_cpy = list(list_org)
list_cpy = list_org[:]
# -------------------------
list_cpy.append("strawberry")
print(list_org)
print(list_cpy)

# ------------ Generate lists in base of other lists ------------

my_list = list(range(1, 7))
my_list2 = [i**2 for i in my_list]
print(my_list)
print(my_list2)

# ---------------------------------------------------------------
