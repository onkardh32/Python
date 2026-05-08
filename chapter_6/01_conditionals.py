a=int(input("enter age :"))

# if elif ladder
if a>=18:
    print("you are eligible to vote")
    print("you can also contest in elections")
else:
    print("you are not eligible to vote")


# elif use case
if a>=18:
    print("you are eligible to vote")
    print("you can also contest in elections")
elif a>=16:
    print("you are not eligible to vote but you can drive")
else:
    print("you are not eligible to vote")

