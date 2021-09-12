#Version 1 by MrPurple666
#Codename = DragonMushroomGray
#Creation date = 03/09/2021 03:35

l = []

for _ in range (10):
  l.append(int(input('digite seu numero:')))

a = sorted(l)

print ('organizado:',a)

j = 0
for i in l:
    j = j + i

media = j/len(l)
print (media,'media:')
    
