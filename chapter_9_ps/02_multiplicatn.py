f=open("table.txt","w")


for i in range (2,21):
    table=""
    for j in range (1,11):
        table+=f"{i} X {j} = {i*j}\n"
       
    # now write that content in file
    # creates the new table_1....table_5 files if not there 
    # and this is by def behavior of python write mode but we need to create
    # the tables before that
    with open(f"tables/table_{i}","w") as ff:
        ff.write(table)
        
    # we could've do with this line below 
   # f.write(table+"\n")
    
   
    

f.close()