# Lists: ordered, mutable, allows duplicate elements
myList = ["banana", "cherry", "apple"]
print(myList)

# Allows more than one data type
# myList2 = list()
myList2 = [5, True, "apple"]
print(myList2)

# Access with index
item = myList[0]  # First element
item = myList[1]  # Second element
item = myList[2]  # Third element
item = myList[-1]  # Last element

# Iterate over a list
for i in myList:
    print(i)

# Check item's existence in a list
if "banana" in myList:
    print("yes")
else:
    print("no")

# List length
length = len(myList)
print(length)

# Append element in a list
myList.append("lemon")
print(myList)

# Insert element in a list at a specific index
myList.insert(1, "blueberry")  # At index 1, insert "blueberry"
print(myList)

# Remove last element and return it in a list
item = myList.pop()
print(f"Last item removed: {item}")
print(myList)

# Popping an empty list will give an IndexError

# Remove a specific element
myList.remove("cherry")  # .remove returns None
print(f"Item removed: cherry")
print(myList)

# Clear list
example = [1, True, "asd"]
example.clear()
print(example)

# Reverse list
numList = [5, 3, 7]
print(numList)
numList.reverse()
print(numList)

# Sort list
numList.sort()
print(numList)

# Return a copy of sorted list (without changing the original list)
ordered = sorted(myList)
print(myList)
print(ordered)

# Multiply a list
fiveZeros = [0] * 5
print(fiveZeros)

# Concatenate two or more lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
new_list = list1 + list2 + list3
print(new_list)

# ---------- Slicing ----------
myList = list(range(1, 10))
sliced = myList[1:3]  # Includes index 1, excludes index 3
print(sliced)
sliced = myList[:3]  # From index 0 to index 3, excluding 3
print(sliced)
sliced = myList[1:]  # From index 1 to last index
print(sliced)
# From index 1 to index 7, excluding index 7, with step 2
sliced = myList[1:7:2]
print(sliced)
# From index 7 to index 1, excluding index 7, with step 2
sliced = myList[1:7:-2]

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

myList = list(range(1, 7))
myList2 = [i**2 for i in myList]
print(myList)
print(myList2)

# ---------------------------------------------------------------
