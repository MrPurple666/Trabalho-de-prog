#Version 4 by MrPurple666
#Codename = Final
#Creation date = 15/09/2021 01:45

print("escreva 10 numeros:")
x = input()
y = x.split(' ')
IInt = []
pares = []
impares = []

for x in y
IInt.append(int(x))

print ("Lista em ordem decrescente:")
print(sorted(IInt,reverse=True))

z = 0
for x in y:
z = z + int(x)

for f in IInt:
if f % 2 == 0:
pares.append(f)
else:
impares.append(f)

print("impares:")
print(impares)
print("media=",z/len(y))
