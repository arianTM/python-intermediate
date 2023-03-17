# itertools: product, permutations, combinations, accumulate,
# groupby, and infinite iterators
# iterator: data type that can be used in a FOR LOOP (lists, tuples..)

from itertools import (combinations, combinations_with_replacement,
                       permutations, product, accumulate, groupby)
# Infinite iterators
from itertools import (count, cycle, repeat)
import operator

# ------------------- Product -------------------
a = [1, 2]  # n = 2
b = [3, 4]  # m = 2
p = product(a, b, repeat=2)  # Cartesian product of a and b
p_list = list(p)
print(p)
print(p_list)
print(len(p_list))  # n * m = 2 * 2

# ------------------- Permutations -------------------
a = [1, 2, 3, 4]  # n = 4
m = 2
p = permutations(a, m)  # m-length permutations of elements in a
p_list = list(p)
print(p)
print(p_list)
print(len(p_list))  # n! / (n - m)!

# ------------------- Combinations -------------------
a = [1, 2, 3, 4]
m = 2
c = combinations(a, m)  # m-length combinations of elements in a
c_list = list(c)
print(c)
print(c_list)
print(len(c_list))
# c_wr is same as c, but elements can combine with themselves
c_wr = combinations_with_replacement(a, m)
c_wr_list = list(c_wr)
print(c_wr)
print(c_wr_list)
print(len(c_wr_list))

# ------------------- Accumulate -------------------
a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul)
print(a)
print(acc)
print(list(acc))

b = [3, 2, 10, 9]
acc2 = accumulate(b, func=max)
print(b)
print(acc2)
print(list(acc2))

# ------------------- Groupby -------------------


def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)  # Can use lambda too
for key, val in group_obj:
    print(key, list(val))

# ------------------- Infinite iterators -------------------
for i in count(10):
    print(i)
    if i == 15:
        break

a = [1, 2, 3]
j = 0
for i in cycle(a):
    print(i)
    j += 1
    if j == 8:
        break

number_to_repeat = 1
n_iterations = 4
for i in repeat(number_to_repeat, n_iterations):
    print(number_to_repeat)
