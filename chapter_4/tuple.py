# tuple is immutable data type in python which means we cant change the value

my_tuple = (1, 2, 3, 'four', 'five', 6.0)
print(my_tuple)  # (1, 2, 3, 'four', 'five', 6.0)
print(type(my_tuple))  # <class 'tuple'>        
a=(9)
print(type(a))  # <class 'int'> because we need to add a comma to make it a tuple
b=(9,)
print(type(b))  # <class 'tuple'> because we added a comma to make it

# cant do this
# a[0]=9;


# tuple methods
