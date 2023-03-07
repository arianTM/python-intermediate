# Dictionary: Key-value pairs, unordered, mutable
my_dict = {"name": "Max", "age": 28, "city": "New York"}
print(my_dict)

# ------------ Built-in 'dict' constructor ------------
my_dict2 = dict(name="Mary", age=27, city="Boston")
print(my_dict2)

# ------------ Access the value of a key ------------
value = my_dict["name"]  # key: "name" --> value: "Max"
print(value)

# ------------ Add a key-value pair ------------
my_dict["email"] = "max@xyz.com"
print(my_dict)

# ------------ Change the value of a key ------------
my_dict["email"] = "coolmax@xyz.com"
print(my_dict)

# ------------ Delete a key-value pair ------------
del my_dict["email"]
print(my_dict)
# --> Alternatives <--
# myDict.pop("email")

# ------------ Delete last inserted key-value pair ------------
# myDict.popitem()
print(my_dict)

# ------------ Check item's existence in dictionary ------------
if "name" in my_dict:
    print(my_dict["name"])

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

for key, value in my_dict.items():
    print(f"{key} --> {value}")

# ------------ Copy a dictionary ------------
my_dict_cpy = my_dict  # Shallow copy
my_dict_cpy = my_dict.copy()  # Deep copy
my_dict_cpy = dict(my_dict)  # Deep copy
print(my_dict)
print(my_dict_cpy)

my_dict_cpy["email"] = "max@xyz.com"
print(my_dict)
print(my_dict_cpy)

# ------------ Merge dictionaries ------------
my_dict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
my_dict2 = dict(name="Mary", age=27, city="Boston")

my_dict.update(my_dict2)
print(my_dict)

# ------------ Integer keys ------------
my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

value = my_dict[3]
print(value)

# ------------ Tuple keys ------------
my_tuple = (8, 7)
my_dict = {my_tuple: 15}
print(my_dict)

# Lists cannot be keys because they are not hashable, as they are mutable
