t = (1, 2, 3)          # original tuple
temp = list(t)         # convert to list (mutable)
temp[0] = 10           # change first value
t = tuple(temp)        # convert back to tuple
print(t)               # print updated tuple

a, b, c = t            # unpack tuple into variables
print(a)               # print first value

t10 = (1, 2)           # first tuple
t20 = (3, 4)           # second tuple
t30 = t10 + t20        # concatenate tuples
print(t30)             # print combined tuple

t33 = (1, 2, 3)        # new tuple
print("the count of 2 is ", t33.count(2))  # count occurrences of 2