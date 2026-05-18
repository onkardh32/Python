
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
num = 5
result = factorial(num)

# explain the functon call and return value of above code
print(f"The factorial of {num} is : {result}")
# how the function call works in above code explain the function call and return value of above code
# When factorial(5) is called, it checks if 5 is 0 or 1. Since it's neither, it returns 5 * factorial(4).
# Then factorial(4) is called, which returns 4 * factorial(3), and so on until it reaches factorial(1), which returns 1.
# The return values are then combined as follows:
# factorial(1) returns 1
# factorial(2) returns 2 * 1 = 2
# factorial(3) returns 3 * 2 = 6
# factorial(4) returns 4 * 6 = 24
# factorial(5) returns 5 * 24 = 120


# used the below term to find factorial of a number
# fact(n)= n*fact(n-1) 
