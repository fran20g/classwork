magicians=['okiver','meem','sazid']
for magician in magicians:
 print(magician,end='\t')

print("\n")

for value in range(1,5):
     print(value)

numbers=list(range(1,6))
print(numbers)

number = list(range(1,10,2))
print(number)

digits=[11,2,3,4,5,26,7,18,90]
print("The minimum value is:{}".format(min(digits)))
print("The maximum value is:{}".format(max(digits)))
print("The sum value is:{}".format(sum(digits)))

players=['Torun','Raj','Joy','Rakib','Roy']
print(players[0:2])
print(players[2:4])
print(players[-1])
print(players[2:])
print(players[:2])
print(players[:])

#copy to my_players
my_players = players[:]
print (my_players)