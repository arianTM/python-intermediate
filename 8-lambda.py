from functools import reduce

# lambda arguments: expression


def add10(x): return x + 10
# add10 = lambda x: x + 10


result = add10(5)
print(result)


def mult(x, y): return x*y
# mult = lambda x, y: x * y


result = mult(2, 7)
print(result)

# --------------------- SORTED ------------------------

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])  # Sort according to y
print(points2D)
print(points2D_sorted)

points2D_sorted = sorted(points2D, key=lambda x: sum(x)
                         )  # Sort according to x+y
print(points2D_sorted)

# --------------------- MAP ------------------------

a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x*2, a)
print(a)
print(list(b))
c = [x*2 for x in a]  # List comprehension
print(c)

# --------------------- FILTER ------------------------

b = filter(lambda x: x % 2 == 0, a)
print(list(b))
c = [x for x in a if x % 2 == 0]
print(c)

# --------------------- REDUCE ------------------------

a = [1, 2, 3, 4]
product_a = reduce(lambda x, y: x*y, a)
print(product_a)
