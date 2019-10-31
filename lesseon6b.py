"""
if test expression:
    statement(s)
 else:
     statement(s)   
"""

players=['Torun','Sourab','Ashik','Ragib','Pritom',]

for name in players:
    if name=='Sourab':
        print(name.upper())
    
    else:
        print(name.lower())


age = 17
if age>=18:
    print("You are old enough to vote!")
    print("Have you regester to vote yet?")

else:
    print("sorry, you are too young to vote.") 
    print("Please regester to vote as soon as you turn 18!")  

#m=1
m= int(input('Enter Month[1-3] :'))
if m==1:
     print('January')                
elif m==2:
     print('February')   
elif m==3:
     print('march')  
else:
     print('Invalid Month !!!')     
