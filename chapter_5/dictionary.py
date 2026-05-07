# dictionary is a collection of key value pairs
# is also used to store the collection of data in a way that we
# can access it using keys instead of index like in list and tuple

marks={
    "Rohit": 90,
    "Shivam": 85,
    "Amit": 80,
    "Suresh": 75
}

print(marks)  # {'Rohit': 90, 'Shivam': 85, 'Amit': 80, 'Suresh': 75}
print(type(marks))  # <class 'dict'>

# here the random access is not possible like below
# print(marks[0])  # this will give an error because we
# cant access the value using index

# to access the value we need to use the key
print(marks["Rohit"])  # 90
print(marks["Shivam"])  # 85

# here in dictionary the lookup is veryfast because it uses hash table data structure to store the data
# so the time complexity of lookup is O(1) on average case and O(n) in worst case when there are hash collisions
# generally its O(1)

 