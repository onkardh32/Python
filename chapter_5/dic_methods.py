
marks={
    "Rohit": 90,
    "Shivam": 85,
    "Amit": 80,
    "Suresh": 75
}

# to get all the keys in the dictionary
print(marks.keys())  # dict_keys(['Rohit', 'Shivam', 'Amit', 'Suresh'])

# to get all the values in the dictionary
print(marks.values())  # dict_values([90, 85, 80, 75])

# to get all the key value pairs in the dictionary
print(marks.items()) 
# gives the list of (key-value) pairs in tuple form
# dict_items([('Rohit', 90), ('Shivam', 85), ('Amit', 80), ('Suresh', 75)])

# to update the dictonary (dictionary is mutable) 
# if entry is not present then it will add the entry in the dictionary
marks.update({"Rohit": 95, "Shivam": 90,"Onkar": 70})
marks["Amit"] = 85
print(marks)  # {'Rohit': 95, 'Shivam': 90, 'Amit': 85, 'Suresh': 75, 'Onkar': 70}

# get method : to get the value of a key in the dictionary
print(marks.get("Rohit"))  # 95

# what is difference between get and [] operator to access the value of a key in the dictionary
# if the key is not present in dictionary in [] gives error whereas 
# in get method it returns None if key is not present 
print(marks.get("Rahul"))  # None because Rahul is not present in the dictionary


# to clear the dictionary
marks.clear()
print(marks)  # {} because we cleared the dictionary

# to create a copy of the dictionary
marks_copy = marks.copy()
print(marks_copy)  # {} because we copied the empty dictionary

