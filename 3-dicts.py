# Dictionary: Key-value pairs, unordered, mutable
myDict = {"name": "Max", "age": 28, "city": "New York"}
print(myDict)

# ------------ Built-in 'dict' constructor ------------
myDict2 = dict(name="Mary", age=27, city="Boston")
print(myDict2)

# ------------ Access the value of a key ------------
value = myDict["name"]  # key: "name" --> value: "Max"
print(value)

# ------------ Add a key-value pair ------------
myDict["email"] = "max@xyz.com"
print(myDict)

# ------------ Change the value of a key ------------
myDict["email"] = "coolmax@xyz.com"
print(myDict)

# ------------ Delete a key-value pair ------------
del myDict["email"]
print(myDict)
# --> Alternatives <--
# myDict.pop("email")

# ------------ Delete last inserted key-value pair ------------
# myDict.popitem()
print(myDict)

# ------------ Check item's existence in dictionary ------------
if "name" in myDict:
    print(myDict["name"])

# try:
#     print(myDict["lastname"])
# except:
#     print("Error")

# ------------ Loop through a dictionary ------------
# for key in myDict:
#     print(key)

# for key in myDict.keys():
#     print(key)

# for value in myDict.values():
#     print(value)

for key, value in myDict.items():
    print(f"{key} --> {value}")

# ------------ Copy a dictionary ------------
myDict_cpy = myDict  # Shallow copy
myDict_cpy = myDict.copy()  # Deep copy
myDict_cpy = dict(myDict)  # Deep copy
print(myDict)
print(myDict_cpy)

myDict_cpy["email"] = "max@xyz.com"
print(myDict)
print(myDict_cpy)

# ------------ Merge dictionaries ------------
myDict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
myDict2 = dict(name="Mary", age=27, city="Boston")

myDict.update(myDict2)
print(myDict)

# ------------ Integer keys ------------
myDict = {3: 9, 6: 36, 9: 81}
print(myDict)

value = myDict[3]
print(value)

# ------------ Tuple keys ------------
myTuple = (8, 7)
myDict = {myTuple: 15}
print(myDict)

# Lists cannot be keys because they are not hashable, as they are mutable
