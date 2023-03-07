# Strings: ordered, inmutable, text representation
from timeit import default_timer as timer
myString = "Hello world!"
print(myString)
myString = 'Hello world 2!'
print(myString)

# ------------ Escape character \ ------------
myString = 'I\'m a programmer'
print(myString)

# ------------ Multiline string ------------
myString = """Hello world! 3
Hello world! 3"""
print(myString)

# ------------ Accessing elements in a string ------------
myString = "Hello world!"
char = myString[0]  # First character
char = myString[1]  # Second character
char = myString[-1]  # Last character
print(char)

# ------------ Changing elements in a string ------------
# myString[0] = "h" # TypeError

# ------------ Substring ------------
myString = "Hello World"
print(myString)
substring = myString[1:5]  # Slice from indeces 1 to 5, excluding 5
print(substring)
substring = myString[:5]  # Slice from indeces 0 to 5, excluding 5
print(substring)
substring = myString[1:]  # Slice from indeces 1 to last
print(substring)
substring = myString[:]  # Returns a copy of the string
print(substring)
substring = myString[::2]  # Slice from indeces 0 to last, in step of 2
print(substring)
substring = myString[::-1]  # Slice from indeces last to 0
print(substring)

# ------------ Concatenate strings (+) ------------
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

# ------------ Iterate through a string ------------
for x in greeting:
    print(x)

# ------------ Check a substring's existence in a string ------------
if 'ell' in greeting:  # Can be a substring
    print("yes")
else:
    print("no")

# ------------ Remove trailing white spaces in a string ------------
myString = "      This sentence has spaces between      "
print(myString)
myString = myString.strip()
print(myString)

# ------------ Convert to upper/lower case ------------
myString = "Hello World!"
print(myString.upper())
print(myString.lower())

# ------------ Check if string starts/ends with another string ------------
print(myString.startswith("Hello"))
print(myString.endswith("World!"))

# ------------ Find index of substring ------------
print(myString.find("orl"))

# ------------ Count how many substrings are ------------
print(myString.count("l"))

# ------------ Replace a substring with another ------------
print(myString.replace("World", "Universe"))

# ------------ Split a string ------------
myString = "how are you doing?"
myList = myString.split()  # Splits between spaces (" ") as default
print(myList)

# ------------ Join a list ------------

myList = ['a'] * 1000000

# bad
# start = timer()
# myString = ''
# for i in myList:
#     myString += i
# stop = timer()
# print(stop - start)

# good
start = timer()
myNewString = " ".join(myList)
stop = timer()
print(stop - start)

# ------------ Format strings ------------
# oldest
var = "Tom"
myString = "the variable is %s" % var
print(myString)

var = 14
myString = "the OLDEST variable is %d" % var
print(myString)

var = 3.1416
myString = "the OLDEST variable is %.2f" % var
print(myString)

# old
var = "Tom"
myString = "the OLD variable is {}".format(var)
print(myString)

var = 2.7818
var2 = 6
myString = "the OLD variable is {:.2f} and {}".format(var, var2)
print(myString)

# newest (since Python 3.6)

# Allows expressions
myString = f"the NEWEST variable is {var:.2f} and {var2 * 3}"
print(myString)
