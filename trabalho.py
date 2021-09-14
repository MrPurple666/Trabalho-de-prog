#Version 2 by MrPurple666
#Codename = RoyaleNight
#Creation date = 10/09/2021 05:32

i = input('digite seu numero:')
l = i.split(',')

#l = sorted(l)
l = l.sort(reverse = True)
print(l)

j = 0
for i in l:
 j = j + int(i)
 
print("media=",j/len(l))
