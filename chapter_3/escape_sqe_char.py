a="hey how are you\ndoing today ?"
print(a)    

# to include double quotes in a string we can use escape character \"
b = "She said, \"Hello!\""
print(b)  # She said, "Hello!"

# can do the same thing using single quotes to define the string and use the double quotes
# wherever is needed without using escape character

# dynamic strings using f-strings
# reduces headache of concatenating strings using + operator and also makes the code more readable
name = "Alice"
age = 30
message = f"My name is {name} and I am {age} years old."
print(message)  # My name is Alice and I am 30 years old.


letter='''Dear <NAME>,
I hope this letter finds you well.'''
print(letter.replace('<NAME>', 'Alice') )
# Dear Alice,
# I hope this letter finds you well.


# Note : string are immutable in python which means we cannot change the value of a string once it is created 
# but we can create a new string by concatenating or slicing the original string.

# means whenever we do perfrom any operation on a string which changes its value 
# then a new string is created in memory and the original string remains unchanged.

