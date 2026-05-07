a=(1,23,42,1,False,"Rohit","Shivam")
print(a)
print(type(a)) # <class 'tuple'>

no=a.count(1)
print(no)

print(a.count(-1)) # 0 coz its not present there
i=a.index("Rohit")
print(i)

# if we concat in that case it will create a new tuple because tuple is immutable
b=(1,2,3)
c=a+b
print(c) # (1, 23, 42, 1, False, 'Rohit', 'Shivam', 1, 2, 3)

print(3 in a)   # False because 3 is not present in the tuple
print(1 in a)   # True because 1 is present in the tuple

# to get length of the tuple
print(len(a))  # 7

#unpacking a tuple
a,b,c=b
print(a)  # 1
print(b)  # 2
print(c)  # 3

#slicing a tuple
arr=(1,2,3,4,5,6,7,8,9,0,0)
print(arr[0])  # 3
print(arr[1:4])
print(sum(arr))  # 45

# min and max functions work on tuples as well only if they have are comparable data types
# if not then gives an error if there are mixed data types
print(min(arr))  # 1
print(max(arr))  # 9

t = ('banana', 'apple', 'cat')
print(min(t))  # apple
print(max(t))  # apple

#a.append(9) # this will give an error because we cant change the value of a tuple

print(arr.count(0))  # 2 because 0 is present twice in the tuple
