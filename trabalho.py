#Version 3 by MrPurple666
#Codename = PokemonXDLugia
#Creation date = 14/09/2021 23:05

i = input()
l = i.split(',')
lInt = []

for i in l:
 lInt.append(int(i))

print(sorted(lInt,reverse=True))

j = 0
for i in l:
 j = j + int(i)
 
print("media=",j/len(l))
