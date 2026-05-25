st=" glex maxx"
f=open("myfile.txt","a")

f.write(st)
f.close()


# sometimes you need some code/logic so that thing can be easily be done
# using this with statement

# the same things can be written using the with statement like this :-
with open("file.txt") as f:
   print(f.read())
   
# with above we dont have to manually close the file 
# you dont have to explicitly close the file
