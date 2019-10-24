'''
Formated otput
=============
Date:17/10/2019
--------------
'''

a,b,c= 5,3.2, "\"Hello\""
print(a)
print(b)
print(c)

print ("%s\t%s\t%s" % (a,b,c))
print ("%s\n%s\n%s" % (a,b,c))

print('I Love {} and {}'.format('bread','butter'))
print('I Love {0} and {1}'.format('bread','butter'))
print('I Love {1} and {0}'.format('bread','butter'))

age=23
message= "Happy " +str(age)+ "rd Birthday!"
print(message)

y=10
x = "Happy {}th Birthday!".format(y)
print(x)
print ("Happy {}th Birthday!".format(y))
