# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# ------------------ Counter ------------------
my_string = "aaaaabbbcccc"
my_counter = Counter(my_string)
# Keys --> hashable elements (a, for example)
# Values --> frequency (5 for a)
print(my_counter)

# Counter is a dict
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

# Most common element
print(my_counter.most_common(2))  # The 2 most common element in tuple
print(my_counter.most_common(2)[0][0])  # The most common element

# Iterable for elements in counter
print(my_counter.elements())
print(list(my_counter.elements()))

# ------------------ Named Tuple ------------------
# Create a class 'Point' with fields x and y
PointConstructor = namedtuple("Point", 'x,y')
pt1 = PointConstructor(1, -4)
print(pt1)
print(pt1.x, pt1.y)

# ------------------ Ordered Dictionary ------------------
# Default dictionaries are also ordered since Python 3.7
ordered_dict = OrderedDict()
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["a"] = 1
ordered_dict["d"] = 4
print(ordered_dict)

# ------------------ Default Dictionary ------------------
# Returns default value (0) of the data type ('int') in case it doesnt exist
default_dict = defaultdict(int)
# int --> 0
# float --> 0.0
# list --> []
default_dict['a'] = 10
default_dict['b'] = 20
print(default_dict)
print(default_dict['a'])
print(default_dict['b'])
print(default_dict['c'])

# ------------------ Deque ------------------
# Deque: double-ended queue
d = deque()

# Append to the right
d.append(1)
d.append(2)
print(d)

# Append to the left
d.appendleft(3)
print(d)

# Pop from the right
d.pop()
print(d)

# Pop from the left
d.popleft()
print(d)

# Clear
d.clear()
print(d)

# Extend to the right
d.extend([4, 5, 6])

# Extend to the left
d.extendleft([3, 2, 1])
print(d)

# Rotate (shift)
d.rotate(1)
print(d)
d.rotate(2)
print(d)
