import random
# wrt find graete number among 3 numbers
def greatest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# how to prevent the endline in print statement
print("4",end="");
print("5");


# program to sum of n 

def sum_of(n):

    if n < 0:
        return "Negative numbers not allowed"

    if n == 0:
        return 0

    return n + sum_of(n - 1)

print(sum_of(8))


# 3rd qs

def pattern(n):
    if(n==0):
        # out of curosity worte pass to check will it stuck in rec or not
        # as expected it stuck and get into infinit loop
        
       # pass
       
       #instead just write return as it says exit the function call and 
       # dont go next from here or do no function call 
       return 
    
    
    #instead u should write return coz pass means
    # do nothing and get ahead
    pattern(n-1)
    print("*"*n)
    
pattern(5)


# to choose bwetween give set of numbers
print(random.choice([1,2,3])) 