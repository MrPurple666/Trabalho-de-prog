l = []

for _ in range (10):
  l.append(int(input('digite seu numero:')))

a = sorted(l)

print (a,'organizado:')

j = 0
for i in l:
    j = j + i

media = j/len(l)
print (media,'media:')
    
