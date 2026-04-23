my_sets = {1, 2, 3}        # create a set
my_sets.add(4)             # add single element
my_sets.update([5, 6, 7])  # add multiple elements
print(my_sets)             # print updated set

a = {1, 2, 3, 4}           # first set
b = {4, 5, 6, 7}           # second set

print(a.union(b))          # all unique elements (merge)
print(a.difference(b))     # elements in a not in b
print(a.intersection(b))   # common elements

fs = frozenset([1, 2, 3])  # immutable set
print(fs)                  # print frozenset

print(a | b)               # union (shortcut)
print(a & b)               # intersection (shortcut)
print(a - b)               # difference (shortcut)