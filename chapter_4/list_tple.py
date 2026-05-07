# just like array in other languages, but with more features
# one distinction is that list can contain different types of data

my_list = [1, 2, 3, 'four', 'five', 6.0]
print(my_list)  # [1, 2, 3, 'four', 'five', 6.0]

print(my_list[0])  # 1

# also strings are immutable in python which means we cant change their value
a = 'old'

# a[0] = 'n'  # this will give an error because we cant change the value of a string

print(a)  # old

# lists are mutable unlike strings
my_list[0] = 'one'

print(my_list)  # ['one', 2, 3, 'four', 'five', 6.0]


# LIST INDEXING

print(my_list[0])  # 'one'
print(my_list[3])  # 'four'
print(my_list[-1])  # 6.0

print(my_list[1:4])  # [2, 3, 'four']

print(my_list[:3])  # ['one', 2, 3]

print(my_list[3:])  # ['four', 'five', 6.0]


# LIST METHODS

my_list.append('seven')

# insert an element at a specific index
my_list.insert(0, 'zero')

# above adds the zero string at the beginning of the list
# and shifts all the other elements to the right

print(my_list)

# ['zero', 'one', 2, 3, 'four', 'five', 6.0, 'seven']


my_list.reverse()

print(my_list)

# ['seven', 6.0, 'five', 'four', 3, 2, 'one', 'zero']


# this will give an error because
# we cant sort a list with different types of data

# my_list.sort()


l1 = [3, 2, 11, 1, 2]

l1.sort()

print(l1)  # [1, 2, 2, 3, 11]


l1.pop()  # this will remove the last element of the list

print(l1)  # [1, 2, 2, 3]


# this will remove the first element of the list
# and returns removed element

l1.pop(0)

print(l1)  # [2, 2, 3]


# this will remove the first occurrence
# of the element 2 from the list

l1.remove(2)

print(l1)  # [2, 3]


# in list if u run just the methods it affects the original one
# so need to print the list after the method to see the changes

# but in string methods it returns a new string
# and does not change the original one