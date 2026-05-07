# ----------------------------------------
# TYPE CHECKING USING type()
# type() is used to find the data type of a variable
# ----------------------------------------

# a = 90
# t = type(a)

# print(type(a))          # <class 'int'>
# print("Value of a:", a)
# print("Type of a:", t)


# ----------------------------------------
# STRING TYPE
# ----------------------------------------

# b = '34.4'
# print("Value of b:", b)
# print("Type of b:", type(b))   # <class 'str'>


# ----------------------------------------
# TYPE CONVERSION (TYPE CASTING)
# Converting one data type to another
# ----------------------------------------

# a = 32.2
# b = int(a)   # converts float → int (decimal part removed)

# print("Value of a:", a)
# print("Type of a:", type(a))   # float

# print("Value of b:", b)
# print("Type of b:", type(b))   # int


# ----------------------------------------
# MORE TYPE CONVERSIONS
# ----------------------------------------

# print(int(b))     # already int → remains same
# print(str(b))     # int → string
# print(float(32))  # int → float

# int("34.4")  # ValueError: invalid literal for int() with base 10: '34.4'



# taking input from user and converting to int
# by deafult the input() function returns a string,  so we need to 
# convert it to int if we want to perform numerical operations
user_input = input("Enter a number: ")  
print("User input:", user_input)
print("Type of user input:", type(user_input))  
user_input_int = int(user_input)  

#correct way to convert string to int when the string represents a float

a = "34.4"
b = int(float(a))

print(b)   # 34