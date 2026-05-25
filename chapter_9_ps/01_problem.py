import random
f=open("poem.txt");

lines=f.readlines()

if("twinkle" in lines):
    print("the wrod twinkle is present")
else :
    print("its not there")
f.close()


# to get the random integer we use below steps:
# import the random module

print(random.randint(1,62))
