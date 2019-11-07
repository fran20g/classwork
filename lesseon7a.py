Dict={'ali':18,'rahim':12,'karim':22,'joya':25}
print('All Item: ')
print(Dict)
print('print by key rahim: ')
print(Dict['rahim'])



boys={'ali':18,'rahim':12,'karim':22}
girls={'joya':25,'rittika':18,'bristy':19}

studentx=boys.copy()
studenty=girls.copy()

print('all boys: ')
print(studentx)
print('girls: ')
print(studenty)


#we use the method Dict.update to
print('add sarah to our existing dictionory')
Dict.update({"sarah":9})
print(Dict)
print('if exist update dictionary')
Dict.update({'karim':12})
print(Dict)

print('Delete by key: ')
del Dict['ali']
print(Dict)

print(type(studentx))
print(dir(dict))


print('print Items : ')
print("students name:%s"% Dict.items())
print('convert dic to list: ')
print("students name:%s" % list(Dict.items()))


print('print only keys and value : ')
for  key in Dict.keys():
    print(key +"-"+ str (Dict[key]))


students=list(Dict.keys())
students.sort()
print("SORTED KEYS : "+ str(students))




