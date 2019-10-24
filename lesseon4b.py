'''
Formated otput
=============
Date:17/10/2019
--------------
'''

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

print(motorcycles[1])

motorcycles[0]='hero'
print(motorcycles)


fruits=[]
fruits.append('Apple')
fruits.append('Mango')
fruits.append('Banana')

fruits.insert(1,'Orange')
print(fruits)


fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

fruits.remove('Apple')
print(fruits)