# Strings: ordered, inmutable, text representation
from timeit import default_timer as timer
my_string = "Hello world!"
print(my_string)
my_string = 'Hello world 2!'
print(my_string)

# ------------ Escape character \ ------------
my_string = 'I\'m a programmer'
print(my_string)

# ------------ Multiline string ------------
my_string = """Hello world! 3
Hello world! 3"""
print(my_string)

# ------------ Accessing elements in a string ------------
my_string = "Hello world!"
char = my_string[0]  # First character
char = my_string[1]  # Second character
char = my_string[-1]  # Last character
print(char)

# ------------ Changing elements in a string ------------
# myString[0] = "h" # TypeError

# ------------ Substring ------------
my_string = "Hello World"
print(my_string)
substring = my_string[1:5]  # Slice from indeces 1 to 5, excluding 5
print(substring)
substring = my_string[:5]  # Slice from indeces 0 to 5, excluding 5
print(substring)
substring = my_string[1:]  # Slice from indeces 1 to last
print(substring)
substring = my_string[:]  # Returns a copy of the string
print(substring)
substring = my_string[::2]  # Slice from indeces 0 to last, in step of 2
print(substring)
substring = my_string[::-1]  # Slice from indeces last to 0
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
my_string = "      This sentence has spaces between      "
print(my_string)
my_string = my_string.strip()
print(my_string)

# ------------ Convert to upper/lower case ------------
my_string = "Hello World!"
print(my_string.upper())
print(my_string.lower())

# ------------ Check if string starts/ends with another string ------------
print(my_string.startswith("Hello"))
print(my_string.endswith("World!"))

# ------------ Find index of substring ------------
print(my_string.find("orl"))

# ------------ Count how many substrings are ------------
print(my_string.count("l"))

# ------------ Replace a substring with another ------------
print(my_string.replace("World", "Universe"))

# ------------ Split a string ------------
my_string = "how are you doing?"
my_list = my_string.split()  # Splits between spaces (" ") as default
print(my_list)

# ------------ Join a list ------------

my_list = ['a'] * 1000000

# bad
# start = timer()
# myString = ''
# for i in myList:
#     myString += i
# stop = timer()
# print(stop - start)

# good
start = timer()
my_new_string = " ".join(my_list)
stop = timer()
print(stop - start)

# ------------ Format strings ------------
# oldest
var = "Tom"
my_string = "the variable is %s" % var
print(my_string)

var = 14
my_string = "the OLDEST variable is %d" % var
print(my_string)

var = 3.1416
my_string = "the OLDEST variable is %.2f" % var
print(my_string)

# old
var = "Tom"
my_string = "the OLD variable is {}".format(var)
print(my_string)

var = 2.7818
var2 = 6
my_string = "the OLD variable is {:.2f} and {}".format(var, var2)
print(my_string)

# newest (since Python 3.6)

# Allows expressions
my_string = f"the NEWEST variable is {var:.2f} and {var2 * 3}"
print(my_string)
