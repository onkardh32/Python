f=open("file.txt")

# gives the list of lines
# lines=f.readlines() // reads everything and puts the cursor at end

# # Reset cursor to beginning
f.seek(0)


# print(lines,type(lines))

# ['This is a good boy\n', 'I am second line\n', 'This is nowhere matching']
# <class 'list'>

# the readline() function alone reads the individual lines
line1=f.readline() # readline()  → reads one line from current cursor position
print(line1,type(line1))

# here what readline does is read the one line at a time and move cursor to next line

# so now the cursor comes to next line and if we do f.readline()
# then the next line comes (this is logic behind it)
line2=f.readline();
print(line2,type(line2))

# whenever u do any readline or readlines make sure to bring cursor back to 
# its normal position coz in readlines() the cusros points to end of line
# 
line3=f.readline();
print(line3,type(line3))


line4=f.readline();
#if u do this after f.readlines() it gives true as at the end of file
# it prints the "" empty string
line5=f.readlines(); # at end the cursor is at end
print(""==f.readline()) # so when fetching it , gives true as its empty string


# to print using while
f.seek(0)
line=f.readline()
while(line!=""):
    print(line,end="")
    line=f.readline()

f.close()
