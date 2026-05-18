

# function declaration 
def func1():
    print("This is function 1")
    

# function with parameters
def fun2(a,b):
    print(f"the sum is : {a+b}");
    
    
# function call
func1()
fun2(5, 10)

# function with return type 
# if nothing is return then it will return None 

def func3(a,b):
    return a*b
result = func3(5, 10)

print(f"The result is : {result}")


# default parameter value
def func4(a,b=10):
    return a+b
result = func4(5)
print(f"The result is : {result}")


