#Version 1 by MrPurple666
#Codename = DragonMushroomGray
#Creation date = 03/09/2021 03:35

i = input('digite seu numero:')
l = i.split(',')

#l = sorted(l)
l = l.sort(reverse = True)
print(l)

j = 0
for i in l:
 j = j + int(i)
 
print("media=",j/len(l))
