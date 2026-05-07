
# we can primarily write a string in three ways:
# 1. using single quotes
print('Hello, World!')
# 2. using double quotes
print("Hello, World!")
# 3. using triple quotes
print('''Hello, World!''')

# we can also use escape characters to include special characters in a string
print('I\'m learning Python.')  # I'm learning Python.
print("She said, \"Hello!\"")  # She said, "Hello!"
# we can also use raw strings to ignore escape characters
print(r'C:\Users\Username')  # C:\Users\Username



# we can concatenate strings using the + operator
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)  # Hello, Alice!
# we can also repeat strings using the * operator
echo = "Echo! "
print(echo * 3)  # Echo! Echo! Echo!
# we can access individual characters in a string using indexing
first_letter = name[0]
print(first_letter)  # A


# we can also slice strings to get a substring   
# here name = "Alice"                                               
substring = name[1:4]
print(substring)  # lic


# -ve slicing 
name= "Harry"
print(name[0:3])

print(name[-4:-2])

# trick to guess the output of -ve slicnig is to convet -ve index to corresponding +ve index and then apply slicing
# here name = "Harry"
print(name[-4:-2])  # ar
# -ve index of 'a' is -4 and -ve index of 'r' is -2, so we can convert them 
print(name[1:3])
# to +ve index which are 1 and 3 respectively and then apply slicing name[1:3] which gives us 'ar' 
   

# in below cases if start is not defind then it is considered as 0 and if end is not defined then it is considered as length of the string
print(name[:3])  # Harry
print(name[2:])  # rry


# string functoins 
# len() function to get the length of a string
name = "Alice"
length = len(name)
print(length)  # 5

print(name.endswith('e'))  # True
print(name.startswith('A'))  # True
# we can also use the in operator to check if a substring is present in a string
print('lic' in name)  # True
# we can also use the not in operator to check if a substring is not present in a string
print('xyz' not in name)  # True
# we can also use the upper() and lower() methods to convert a string to uppercase or lowercase
print(name.upper())  # ALICE
print(name.lower())  # alice
                
print("hello world".title())  # Hello World

# string.count() method to count the number of occurrences of a substring in a string
sentence = "The quick lazy brown fox jumps over the lazy dog."
count = sentence.count('o')
print(count)  # 4


# string.find() method to find the index of the first occurrence of a substring in a string
index = sentence.find('fox')    
print(index)  # 16

# replaces all occurences of 'lazy' with 'active'
# string replace() method to replace a substring with another substring in a string
new_sentence = sentence.replace('lazy', 'active')
print(new_sentence)  # The quick brown fox jumps over the active dog.


# Slicing with Skip value
name="shrink"
print(name[0:6:3])  
print(name[1:6:2])
 

