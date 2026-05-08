a=input("enter name: ")
name="onkar"

# use case of in keyword
if (a in name):
    print("Matching names")
else:
    print("Not matching names")

# use case of not in keyword
if (a not in name):
    print("Not Matching names")

# can be used in list
names=["onkar","satyarth","pratik"]
if (a in names):
    print("Matching names")
else:    
    print("Not matching names")
