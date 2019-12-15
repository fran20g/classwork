from os import system

students = [
    {'Id':1,'Name': 'Chand','Marks':123.99},
    {'Id':2,'Name': 'Nazmul','Marks':12.99},
    {'Id':3,'Name': 'Manuz','Marks':23.99}
    ]


print("%-5s %-30s %-20s"%("Id","Student Name","Marks"))
print("="* 50)
for std in students:
   

    print("%-5s %-30s %-20s"%(std['Id'],std['Name'],std['Marks']))
    
    
system('dir') 
