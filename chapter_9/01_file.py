'''
a= "a very long string with  emails"
'''

# open is funtion used to open file
# there are diff types of mode in files 

# if we dont mention anything by def it is considered as read "r"
f=open("file.txt")
# above is same as f=open("file.txt","r")

# if we want to write then mention "w" like below
# f=open("file.txt","w")

# read is used to read content from file
data =f.read()

print(data)


# close file when the work is done
f.close()