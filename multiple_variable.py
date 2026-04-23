# Playing around with a simple list
my_list = [10, 20, 30]

# Let's see what's at the first position
print(my_list[0])

# Hmm, let's change that first value
my_list[0] = 33
print(my_list[0])

# Adding one more number at the end
my_list.append(40)

# The new number should be at index 3
print(my_list[3])

# Just checking what type this is (should be a list)
print(type(my_list))

# Negative indexing is cool — -4 means first element here
print(my_list[-4])


# Another list with fruits
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# Grab a slice from index 2 to 4 (5 is excluded)
print(thislist[2:5])

# Replace banana and cherry with something new
thislist[1:3] = ["watermelon", "grapes"]
print(thislist)

# How many items do we have now?
print(len(thislist))

# Let's insert something in the middle
thislist.insert(2, "watermelon")
print(thislist)

# Adding more fruits from another list
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Removing the first three items
del thislist[:3]
print(thislist)

# Clearing everything out (starting fresh)
thislist.clear()
print(thislist)

# Sorting... though it's empty now anyway
thislist.sort()
print(thislist)

# Making a copy of the list
newlist = thislist.copy()
print(newlist)