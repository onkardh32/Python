# ================= SET METHODS =================

# sets store unique unordered values
s = {1, 2, 3}
print(s)  # {1, 2, 3}

# add() adds single element
s.add(4)
print(s)  # {1, 2, 3, 4}

# update() adds multiple elements
s.update([5, 6])
print(s)  # {1, 2, 3, 4, 5, 6}

# remove() removes element and gives error if not found
s.remove(6)
print(s)  # {1, 2, 3, 4, 5}

# discard() removes element without error if not found
s.discard(10)
print(s)  # {1, 2, 3, 4, 5}

# pop() removes random element
s.pop()
print(s)

# clear() removes all elements
a = {1, 2, 3}
a.clear()
print(a)  # set()

# union() combines two sets
x = {1, 2}
y = {2, 3}
print(x.union(y))  # {1, 2, 3}

# intersection() returns common elements
print(x.intersection(y))  # {2}

# difference() returns elements from first set only
print(x.difference(y))  # {1}

# symmetric_difference() returns non common elements
print(x.symmetric_difference(y))  # {1, 3}

# issubset() checks if all elements exist in another set
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))  # True

# issuperset() checks if set contains all elements
print(b.issuperset(a))  # True

# copy() creates copy of set
c = b.copy()
print(c)  # {1, 2, 3}


# ================= NORMAL FUNCTIONS / OPERATORS =================

# len() returns total elements
print(len(b))  # 3

# in checks if value exists
print(2 in b)  # True

# not in checks if value does not exist
print(10 not in b)  # True


# IMP

st = set()

st.add(1)
st.add(2)
st.add(2.0)

# In Python:
# 2 == 2.0 returns True

# Sets store only unique values
# so 2 and 2.0 are treated as same element

print(st)

# Output can be:
# {1, 2}
# or
# {1, 2.0}

# because internally Python keeps only one of them

print(len(st))  # 2

# length is 2 because:
# set contains only:
# 1 and 2 (or 2.0)

print(2==2.0)  # True   
# explain this beahvior
# In Python, the integer 2 and the floating-point number 2.0 are considered equal because they represent the same numerical value.
# When you compare them using the equality operator (==), Python checks their values rather than their types, resulting in True. 
# However, they are of different types (int and float), but for the purpose of comparison, they are treated as equal.

# python equality op first check if two operands are of same type then if they
# are of same type then it checks their values and if they are of 
# different types then it checks if they are of compatible types and
# if they are compatible types then it checks their values and if they are not compatible types then it returns False


#IMPORTANT
print(2 == 2.0)  # True

# explain this behavior

# In Python, integer 2 and floating point number 2.0
# are considered equal because both represent the same numerical value.

# Python compares their values, not just their data types.

# so:
# 2 == 2.0  -> True

# even though:
# type(2) -> int
# type(2.0) -> float

# Python automatically performs type compatibility checks
# between numeric data types like:
# int, float, complex

# if values are numerically equal,
# equality operator returns True

# examples

print(5 == 5.0)  # True

print(3 == 3.5)  # False

print(2 == "2")  # False

# because string and integer are not numerically compatible both string and integer are of different types and they are not compatible types so it returns False
# both are of different types and they are not compatible types so it returns False
# coz string is diff and cannot be converted to int and int cannot be converted to string so they are not compatible types so it returns False

# IMP
# s={} is set not dic s=set() is set


#PS can you change the values inside a list which is contained in set?
# No you cannto and first you cannot have a list inside a 
# set because lists are mutable and sets require immutable elements.
# so below is wrpng
# s = {1, 2, [3, 4]}  # This will raise a TypeError because lists are unhashable and cannot be added to a set.

