# -------------------------------
# 1. Numeric Types
# Used to store numbers (int, float, complex)
# -------------------------------

a = 10          # int
b = 3.14        # float
c = 2 + 3j      # complex

print("Numeric Types:", a, b, c)


# -------------------------------
# 2. String (str)
# Used to store text (sequence of characters)
# -------------------------------

name = "Onkar"
print("String:", name)


# -------------------------------
# 3. Boolean (bool)
# Used for True/False values (conditions)
# -------------------------------

is_active = True
print("Boolean:", is_active)


# -------------------------------
# 4. List
# Ordered, mutable (can change), allows duplicates
# -------------------------------

fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print("List:", fruits)


# -------------------------------
# 5. Tuple
# Ordered, immutable (cannot change)
# -------------------------------

coordinates = (10, 20)
print("Tuple:", coordinates)


# -------------------------------
# 6. Set
# Unordered, no duplicate values
# -------------------------------

numbers = {1, 2, 3, 3, 4}
print("Set:", numbers)


# -------------------------------
# 7. Dictionary (dict)
# Key-value pairs, mutable
# -------------------------------

student = {
    "name": "Onkar",
    "age": 22,
    "course": "CSE"
}
print("Dictionary:", student)


# -------------------------------
# 8. NoneType
# Represents absence of value
# -------------------------------

x = None
print("NoneType:", x)